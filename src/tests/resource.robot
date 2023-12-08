*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${BASE URL}  http://${SERVER}
${OPTIONS}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys

*** Keywords ***
Open And Configure Headless Browser
    Call Method    ${OPTIONS}    add_argument    --no-sandbox
    Call Method  ${OPTIONS}  add_argument  --headless
    Open Browser  ${BASE URL}  Chrome  options=${OPTIONS}
    Set Selenium Speed  ${DELAY}

Open And Configure Normal Browser
    Call Method    ${OPTIONS}    add_argument    --no-sandbox
    Open Browser  ${BASE URL}  Chrome  options=${OPTIONS}
    Set Selenium Speed  ${DELAY}