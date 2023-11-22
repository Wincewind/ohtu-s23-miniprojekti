*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections

*** Variables ***
${SERVER}         localhost:5000
${BROWSER}        Chrome
${BASE URL}       http://${SERVER}  # Update with the correct URL if needed
@{FORM ELEMENTS}  author  title  year  publisher  publisher_address
@{EXPECTED VALUES}  a  a  2000  a  a
${DELAY}  0.5 seconds

*** Test Cases ***
Add Reference Test
    Open Browser  ${BASE URL}  ${BROWSER}
    Set Selenium Speed  ${DELAY}
    Input Form Values  ${FORM ELEMENTS}  ${EXPECTED VALUES}
    Submit Form
    Wait Until Page Contains  Reference added
    Close Browser

*** Keywords ***
Input Form Values
    [Arguments]  ${form_elements}  ${values}
    FOR  ${index}  IN RANGE  ${form_elements.__len__()}
        Input Text  name=${form_elements[${index}]}  text=${values[${index}]}
    END

Submit Form
    Click Button  //button[@type='submit']
