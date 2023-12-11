*** Settings ***
Resource  resource.robot
Variables  AppLibrary.py
Suite Setup  Open And Configure Headless Browser
Test Setup    Reset Application And Reload Page
Suite Teardown  Close Browser

*** Variables ***
${DELAY}  0.005 seconds  # set this to 0.3-0.5 if you disabled --headless in resource.robot

*** Test Cases ***
User Can Add Book Reference To The App 
    Compare Row Count To Expected    0
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${TEST INPUT 1}    2    ${BOOK COL INDEXES}

User Can Add Article Reference To The App
    Compare Row Count To Expected    0
    Submit Form And Handle Alert  ${TEST INPUT 3}    article
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${TEST INPUT 3}    2    ${ARTICLE COL INDEXES}

User Cannot Input Reference With Missing Data
    Submit Form
    ${message} =    Handle Alert    LEAVE   # Leave alert open and get its message.
    Should Be Equal As Strings    ${message}    Submit failed.
    Handle Alert
    Compare Row Count To Expected    0

User Can See The Latest Reference First
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Submit Form And Handle Alert  ${TEST INPUT 3}    article
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    2
    Compare Row Values To Expected    ${TEST INPUT 1}    3    ${BOOK COL INDEXES}
    Compare Row Values To Expected    ${TEST INPUT 3}    2    ${ARTICLE COL INDEXES}

User Can Delete One Reference
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Submit Form And Handle Alert  ${TEST INPUT 2}    book
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    2
    Select And Delete Reference  1  # delete first row reference, at which point input 1 will rise to be first
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${TEST INPUT 1}    2    ${BOOK COL INDEXES}

User Can Delete All References
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Submit Form And Handle Alert  ${TEST INPUT 3}    article
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    2
    Select All References
    Delete References
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    0

User Can Generate A BibTex File From A Book Reference In Correct Format
    Remove File    ${PATH TO GENERATED BIBTEX}
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    1
    Select And Generate BibTex File From Reference    1
    Wait Until Keyword Succeeds    3    1    Check For File Existance    ${PATH TO GENERATED BIBTEX}
    Validate Generated Book Bibtex File
    Remove File    ${PATH TO GENERATED BIBTEX}

User Can Generate A BibTex File From Multiple References In Correct Format
    Remove File    ${PATH TO GENERATED BIBTEX}
    Submit Form And Handle Alert  ${TEST INPUT 1}    book
    Submit Form And Handle Alert  ${TEST INPUT 3}    article
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    2
    Select All References
    Generate BibTex File
    Wait Until Keyword Succeeds    3    1    Check For File Existance    ${PATH TO GENERATED BIBTEX}
    Validate Generated BibTex File For Multiple References
    Remove File    ${PATH TO GENERATED BIBTEX}

User Can Add References Using DOI Links
    Select From List By Value    //select    article
    Input Text    //input[@name='DOI']    ${DOI_3}
    Click Button    //button[contains(text(),'Get DOI')]
    Sleep    1s
    Submit Form
    Handle Alert
    Wait Until Keyword Succeeds    3    0.5    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${TEST INPUT 3}    2    ${ARTICLE COL INDEXES}

*** Keywords ***
Input Form Values
    [Arguments]  ${input_data}
    FOR    ${kvp}    IN    @{input_data}
        Input Text  name=${kvp}[0]  text=${kvp}[1]
        
    END

Submit Form
    Click Button  id:referenceFormSubmitButton

Submit Form And Handle Alert
    [Arguments]  ${values}    ${form_type}
    Select From List By Value    //select    ${form_type}
    Sleep    0.5s
    Input Form Values  ${values}
    Submit Form
    Handle Alert

Reset Application And Reload Page
    Reset Application
    Reload Page

Compare Row Count To Expected
    [Arguments]  ${expected_row_count}
    ${row_count}=    Get Element Count  //table[1]/tbody/tr
    Should Be Equal As Numbers    ${row_count}    ${expected_row_count}

Compare Row Values To Expected
    [Arguments]  ${expected_values}  ${row_num}    ${column_idxs}
    FOR    ${index}    ${col_idx}    IN ENUMERATE    @{column_idxs}
        ${col_idx}=    Evaluate    ${col_idx} + 1
        ${value}=    Get Table Cell    locator=//table[1]    row=${row_num}    column=${col_idx}
        Should Be Equal    ${value}    ${expected_values}[${index}][1]
    END

Select One Reference
    [Arguments]  ${row_index}
    ${adjusted_index}=   Evaluate    ${row_index}
    ${locator}=    Set Variable    //table[1]//tbody//tr[${adjusted_index}]//input[@type='checkbox']
    Select Checkbox   ${locator}

Select All References
    Select Checkbox    //table[1]//tr[1]//input[@type='checkbox']

Delete References
    ${delete_icon}=    Set Variable  xpath=//button[contains(@aria-label, 'Delete')]
    Wait Until Element Is Visible    ${delete_icon}
    Click Element    ${delete_icon}

Select And Delete Reference
    [Arguments]  ${row_index}
    Select One Reference    ${row_index}
    Delete References

Generate BibTex File
    ${download_icon}=    Set Variable  xpath=//button[contains(@aria-label, 'Download')]
    Wait Until Element Is Visible    ${download_icon}
    Click Element    ${download_icon}

Select And Generate BibTex File From Reference
    [Arguments]  ${row_index}
    Select One Reference    ${row_index}
    Generate BibTex File
    

Check For File Existance
    [Arguments]  ${file_path}
    File Should Exist    ${file_path}