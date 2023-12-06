*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Test Setup    Reset Application And Reload Page
Suite Teardown  Close Browser

*** Variables ***
@{FORM ELEMENTS}  authors  title  year  publisher  publisher_address
@{EXPECTED VALUES 1}  Mariot Tsitoara  Beginning Git and GitHub  2019  APress  One New York Plaza, Suite 4600 New York, NY
@{EXPECTED VALUES 2}  Hawking, Stephen  A Brief History of Time: From the Big Bang to Black Holes  1988  Bantam  Random House Academic Marketing, 1745 Broadway, 20th Floor, New York
${DELAY}  0.005 seconds  # set this to 0.3-0.5 if you disabled --headless in resource.robot

*** Test Cases ***
User Can Add Reference To The App
    Compare Row Count To Expected    0
    Input Form Values  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
    Submit Form
    Handle Alert
    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${EXPECTED VALUES 1}    2

User Cannot Input Reference With Missing Data
    Submit Form
    ${message} =    Handle Alert    LEAVE   # Leave alert open and get its message.
    Should Be Equal As Strings    ${message}    Submit failed.
    Handle Alert
    Compare Row Count To Expected    0

User Can See The Latest Reference First
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 2}
    Compare Row Count To Expected    2
    Compare Row Values To Expected    ${EXPECTED VALUES 1}    2
    Compare Row Values To Expected    ${EXPECTED VALUES 2}    3

User Can Delete One Reference
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 2}
    Select And Delete Reference  2  # delete second reference
    Compare Row Count To Expected    1
    Compare Row Values To Expected    ${EXPECTED VALUES 1}    1

User Can Delete All References
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
    Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 2}
    Select All References
    Delete References
    Compare Row Count To Expected    0

*** Keywords ***
Input Form Values
    [Arguments]  ${form_elements}  ${values}
    FOR  ${index}  IN RANGE  ${form_elements.__len__()}
        Input Text  name=${form_elements[${index}]}  text=${values[${index}]}
    END

Submit Form
    Click Button  id:referenceFormSubmitButton

Submit Form And Handle Alert
    [Arguments]  ${form_elements}  ${values}
    Input Form Values  ${form_elements}  ${values}
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
    [Arguments]  ${expected_values}  ${row_num}
    FOR  ${index}  IN RANGE  ${expected_values.__len__()}
        ${index}=    Evaluate    ${index} + 2
        ${value}=    Get Table Cell    locator=//table[1]    row=${row_num}    column=${index}
    END

Select One Reference
    [Arguments]  ${row_index}
    ${adjusted_index}=   Evaluate    ${row_index}
    ${locator}=    Set Variable    //table[1]//tr[${adjusted_index}]//input[@type='checkbox']
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