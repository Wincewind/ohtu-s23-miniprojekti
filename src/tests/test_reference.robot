*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
@{FORM ELEMENTS}  authors  title  year  publisher  publisher_address
@{EXPECTED VALUES 1}  Mariot Tsitoara  Beginning Git and GitHub  2019  APress  One New York Plaza, Suite 4600 New York, NY
@{EXPECTED VALUES 2}  Hawking, Stephen  A Brief History of Time: From the Big Bang to Black Holes  1988  Bantam  Random House Academic Marketing, 1745 Broadway, 20th Floor, New York
${DELAY}  0.5 seconds

*** Test Cases ***
# Add Reference Test
#     Input Form Values  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
#     Submit Form
#     Handle Alert

User Can See All The Added References In The UI
    #Should Be Equal As Strings    Mariot Tsitoara    ${EXPECTED VALUES 1}[0]
    #Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 1}
    #Submit Form And Handle Alert  ${FORM ELEMENTS}  ${EXPECTED VALUES 2}
    #${row1_author}=  Get Table Cell    locator=//table[@class='MuiTable-root css-1q7lp8d']    row=2    column=2
    ${row1_author}=  Get Table Cell    locator=//table[1]    row=2    column=2
    Should Be Equal As Strings    ${row1_author}    ${EXPECTED VALUES 1}[0]
    #Table Should Contain    //table[1]    ${EXPECTED VALUES 1}[0] ${EXPECTED VALUES 1}[1]

*** Keywords ***
Input Form Values
    [Arguments]  ${form_elements}  ${values}
    FOR  ${index}  IN RANGE  ${form_elements.__len__()}
        Input Text  name=${form_elements[${index}]}  text=${values[${index}]}
    END

Submit Form
    Click Button  //button[@type='submit']

Submit Form And Handle Alert
    [Arguments]  ${form_elements}  ${values}
    Input Form Values  ${form_elements}  ${values}
    Submit Form
    Handle Alert