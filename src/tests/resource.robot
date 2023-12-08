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
Open And Configure Headless Browser
    ${OPTIONS}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${OPTIONS}    add_argument    --no-sandbox
    Open Browser  ${BASE URL}  HeadlessChrome  options=${OPTIONS}
    Set Selenium Speed  ${DELAY}

Open And Configure Normal Browser
    ${OPTIONS}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${OPTIONS}    add_argument    --no-sandbox
    Open Browser  ${BASE URL}  Chrome  options=${OPTIONS}
    Set Selenium Speed  0.5