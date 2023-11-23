*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections

*** Variables ***
${SERVER}         localhost:5000
${BROWSER}        Chrome
${BASE URL}       http://${SERVER}  
@{FORM ELEMENTS}  author  title  year  publisher  publisher_address
@{EXPECTED VALUES}  Mariot Tsitoara  Beginning Git and GitHub  2019  APress  One New York Plaza, Suite 4600 New York, NY
${DELAY}  0.5 seconds

*** Test Cases ***
Add Reference Test
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Open Browser  ${BASE URL}  ${BROWSER}  options=${options}
    Set Selenium Speed  ${DELAY}
    Input Form Values  ${FORM ELEMENTS}  ${EXPECTED VALUES}
    Submit Form
    Handle Alert
    Close Browser

*** Keywords ***
Input Form Values
    [Arguments]  ${form_elements}  ${values}
    FOR  ${index}  IN RANGE  ${form_elements.__len__()}
        Input Text  name=${form_elements[${index}]}  text=${values[${index}]}
    END

Submit Form
    Click Button  //button[@type='submit']
