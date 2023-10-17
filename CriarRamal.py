import time
import sys
import requests, json

ramal = sys.argv[1]
nome = sys.argv[2]
ticket = sys.argv[3]
email = sys.argv[4]

from playwright.sync_api import sync_playwright
def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    # Go to http://172.61.2.26/admin/config.php
    page.goto("http://172.61.2.26/admin/config.php")

    # Click #login_admin
    page.click("#login_admin")
    # assert page.url == "http://172.61.2.26/admin/config.php#"

    # Click text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder="username"]
    page.click("text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder=\"username\"]")

    # Fill text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder="username"]
    page.fill("text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder=\"username\"]", "jerson.junior")
    #time.sleep(1)
    # Click text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder="password"]
    page.click("text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder=\"password\"]")

    # Fill text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder="password"]
    page.fill("text=Login Close To get started, please enter your credentials: ContinueCancel >> [placeholder=\"password\"]", "@#in4008@#")
    #time.sleep(1)
    # Click text=Continue
    page.click("text=Continue")
    # assert page.url == "http://172.61.2.26/admin/config.php#"

    # Click text=Applications
    page.click("text=Applications")
    #time.sleep(1)
    # Click :nth-match(:text("Extensions"), 2)
    page.click(":nth-match(:text(\"Extensions\"), 2)")
    # assert page.url == "http://172.61.2.26/admin/config.php?display=extensions"

    # Click text=Add Extension
    page.click("text=Add Extension")
    #time.sleep(1)
    # Click text=Add New Chan_SIP Extension
    page.click("text=Add New Chan_SIP Extension")
    # assert page.url == "http://172.61.2.26/admin/config.php?display=extensions&tech_hardware=sip_generic"
    #time.sleep(1)
    # Click input[name="extension"]
    page.click("input[name=\"extension\"]")
    #time.sleep(1)
    # Fill input[name="extension"]
    page.fill("input[name=\"extension\"]", str(ramal))
    #time.sleep(1)
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    #time.sleep(1)
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", str(nome))

    # Click input[name="devinfo_secret"]
    page.click("input[name=\"devinfo_secret\"]")
    #time.sleep(1)
    # Fill input[name="devinfo_secret"]
    page.fill("input[name=\"devinfo_secret\"]", "central@123")
    #time.sleep(1)
    # Click a[role="tab"]:has-text("Advanced")
    page.click("a[role=\"tab\"]:has-text(\"Advanced\")")

    # 0× click
    page.click("select[name=\"devinfo_nat\"]")

    # Click #advanced >> :nth-match(div:has-text("Endpoint port number to use, usually 5060. Some 2 ports devices such as ATA may "), 5)
    page.click("#advanced >> :nth-match(div:has-text(\"Endpoint port number to use, usually 5060. Some 2 ports devices such as ATA may \"), 5)")
    #time.sleep(1)
    # 0× click
    page.click("select[name=\"devinfo_nat\"]")
    page.select_option("select[name=\"devinfo_nat\"]", "yes")
    #time.sleep(1)
    # Click div:nth-child(14) div div .col-md-12 .row
    page.click("div:nth-child(14) div div .col-md-12 .row")
    #time.sleep(1)
    # Click div:nth-child(14) div:nth-child(1) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)
    page.click("div:nth-child(14) div:nth-child(1) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)")
    #time.sleep(1)
    # Click div:nth-child(14) div:nth-child(2) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)
    page.click("div:nth-child(14) div:nth-child(2) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)")
    #time.sleep(1)
    # Click div:nth-child(14) div:nth-child(3) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)
    page.click("div:nth-child(14) div:nth-child(3) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)")
    #time.sleep(1)
    # Click div:nth-child(14) div:nth-child(4) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)
    page.click("div:nth-child(14) div:nth-child(4) div .col-md-12 .row .form-group .col-md-8 .radioset label:nth-child(4)")
    #time.sleep(1)
    # Click text=Submit
    # with page.expect_navigation(url="http://172.61.2.26/admin/config.php?display=extensions"):
    with page.expect_navigation():
        page.click("text=Submit")
    #time.sleep(1)
    # Click text=Apply Config
    page.click("text=Apply Config")
    time.sleep(15)
      # Go to http://172.61.2.26:8080/queuemetrics/autenticazione.jsp
    page.goto("http://172.61.2.26:8080/queuemetrics/autenticazione.jsp")
    # Click input[name="AUTH_logon"]
    page.click("input[name=\"AUTH_logon\"]")
    # Fill input[name="AUTH_logon"]
    page.fill("input[name=\"AUTH_logon\"]", "jerson.junior")
    #time.sleep(1)
    # Click input[name="AUTH_password"]
    page.click("input[name=\"AUTH_password\"]")
    # Fill input[name="AUTH_password"]
    page.fill("input[name=\"AUTH_password\"]", "@#18Setembro@#")
    #time.sleep(1)
    # Click text=Log In »
    page.click("text=Log In »")
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_homepage_load.do"
    # Click [aria-label="Open settings menu"] svg
    page.click("[aria-label=\"Open settings menu\"] svg")
    time.sleep(1)
    # Click text=Users
    page.click("text=Users")
    #time.sleep(1)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_users_list.jsp"
    # Click text=Create New
    page.click("text=Create New")
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_users_edit.jsp"
    # Click input[name="TABUSERS_login"]
    page.click("input[name=\"TABUSERS_login\"]")
    #time.sleep(1)
    # Fill input[name="TABUSERS_login"]
    page.fill("input[name=\"TABUSERS_login\"]", "Agent/" + ramal)
    #time.sleep(1)
    # Click input[name="TABUSERS_password_new"]
    page.click("input[name=\"TABUSERS_password_new\"]")
    # Fill input[name="TABUSERS_password_new"]
    page.fill("input[name=\"TABUSERS_password_new\"]", "central@123")
    #time.sleep(1)
    # Click input[name="TABUSERS_password_confirm"]
    page.click("input[name=\"TABUSERS_password_confirm\"]")
    # Fill input[name="TABUSERS_password_confirm"]
    page.fill("input[name=\"TABUSERS_password_confirm\"]", "central@123")
    #time.sleep(1)
    # Click input[name="TABUSERS_real_name"]
    page.click("input[name=\"TABUSERS_real_name\"]")
    # Fill input[name="TABUSERS_real_name"]
    page.fill("input[name=\"TABUSERS_real_name\"]", nome)
    #time.sleep(1)
    # Click span[role="textbox"]:has-text("ADMIN")
    page.click("span[role=\"textbox\"]:has-text(\"ADMIN\")")
    # Click li[role="option"]:has-text("AGENTS")
    page.click("li[role=\"option\"]:has-text(\"AGENTS\")")
    #time.sleep(1)
    # Click text=Save
    page.click("text=Save")
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_users_edit.jsp"
    # Click text=Home
    #page.click("text=Início")
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_homepage_load.do"
    #time.sleep(2)
       # Click text=Usuários
    #page.click("text=Usuários")
    #time.sleep(2)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_users_list.jsp"
    # Click text=Agentes
    page.click("text=Agents")
    #time.sleep(1)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_agents_list.jsp"
    # Click text=Criar Novo
    page.click("text=Create New")
    #time.sleep(1)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_agents_edit.jsp"
    # Click input[name="TABAGENTI_NOTI_nome_agente"]
    page.click("input[name=\"TABAGENTI_NOTI_nome_agente\"]")
    # Fill input[name="TABAGENTI_NOTI_nome_agente"]
    page.fill("input[name=\"TABAGENTI_NOTI_nome_agente\"]", "Agent/" + ramal)
    #time.sleep(1)
    # Click input[name="TABAGENTI_NOTI_descr_agente"]
    page.click("input[name=\"TABAGENTI_NOTI_descr_agente\"]")
    # Fill input[name="TABAGENTI_NOTI_descr_agente"]
    page.fill("input[name=\"TABAGENTI_NOTI_descr_agente\"]", nome)
    #time.sleep(1)
    # Click input[name="TABAGENTI_NOTI_current_terminal"]
    page.click("input[name=\"TABAGENTI_NOTI_current_terminal\"]")
    # Fill input[name="TABAGENTI_NOTI_current_terminal"]
    page.fill("input[name=\"TABAGENTI_NOTI_current_terminal\"]", ramal)
    #time.sleep(1)
    # Click text=Salvar
    page.click("text=Save")
    #time.sleep(1)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_adm/cfg2_agents_edit.jsp"
    # Click text=Início
    page.click("text=Home")
    #time.sleep(1)
    # assert page.url == "http://172.61.2.26:8080/queuemetrics/qm_homepage_load.do"
    #r = requests.post('http://172.61.2.203:5000/finaliza', verify=False,
    ##requests.post('https://prod-135.westus.logic.azure.com:443/workflows/8366a533565b4760bfccb11651c851e5/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=LOY6_tGA0RkQO6fksxuOEh-Z4gZEvCZNxM9nXJbwaLg', verify=False,
    ##data=json.dumps({'userName':'cit.local\\jerson.junior','password':'@#18Setembro@#','platform':'Telefonia'}),
    #data=json.dumps({'Email': str(email), 'Ticket': ticket, "Ramal": ramal}),
    #headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
    #print(r.text)
    #print(r.status_code)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

#page.select_option("select[name=\"devinfo_nat\"]", "yes")


#time.sleep(10000)

