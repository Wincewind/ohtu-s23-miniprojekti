*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
@{FORM ELEMENTS}  authors  title  year  publisher  publisher_address
@{EXPECTED VALUES}  Mariot Tsitoara  Beginning Git and GitHub  2019  APress  One New York Plaza, Suite 4600 New York, NY
${DELAY}  0.5 seconds

*** Test Cases ***
Add Reference Test
    Input Form Values  ${FORM ELEMENTS}  ${EXPECTED VALUES}
    Submit Form
    Handle Alert

*** Keywords ***
Input Form Values
    [Arguments]  ${form_elements}  ${values}
    FOR  ${index}  IN RANGE  ${form_elements.__len__()}
        Input Text  name=${form_elements[${index}]}  text=${values[${index}]}
    END

Submit Form
    Click Button  //button[@type='submit']
