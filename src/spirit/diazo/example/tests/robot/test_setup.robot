*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show how to activate the add-on
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/prefs_install_products_form
    Page should contain element  id=spirit.diazo.example
    Assign id to element
    ...  xpath=//*[@id='spirit.diazo.example']/parent::*
    ...  addons-spiritdiazoexample
    Assign id to element
    ...  xpath=//*[@id='spirit.diazo.example']/ancestor::form
    ...  addons-enabled

    Highlight  addons-spiritdiazoexample
    Capture and crop page screenshot
    ...  setup_select_add_on.png
    ...  id=addons-enabled
