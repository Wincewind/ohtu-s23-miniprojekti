*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${BASE URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  ${BASE URL}  Chrome  options=${options}
    Set Selenium Speed  ${DELAY}