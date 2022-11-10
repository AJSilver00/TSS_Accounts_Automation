# Before running this on a new computer/laptop,
# open Command Prompt and write the following:
# pip install pyautogui
# pip install pyperclip
# pip install os-sys
# pip install python-time
# pip install pillow
# pip install opencv-python

class processes:
    import pyautogui
    import time
    import os
    import pyperclip
    import keyboard

    def __init__(self):
        self.os.chdir(r'C:\Users\Aimee\Pictures\TSS Python Screenshots\proforma reminder')
        self.comments = []
        self.jobref = ''

    def print_comments_list(self):
        print('=======================================================================================================')
        print('COMMENTS LIST STARTS FROM HERE')
        print('-------------------------------')
        for line in  range(1, (len(self.comments))):
            if line < 10:
                updatedline = ('Comment {}:           '.format(line)) + self.comments[line]
                print(updatedline)
            else:
                updatedline = ('Comment {}:          '.format(line)) + self.comments[line]
                print(updatedline)
        print('------------------------')
        print('COMMENTS LIST ENDS HERE')
        print('=======================================================================================================')

    # Opens AllHire Tab.

    def open_allhiretab(self):
        processes().click_thisORthat_tab('allhiretabunsel.png',0.9,'allhiretabsel.png',0.9)

        # while True:
        #     location = self.pyautogui.locateOnScreen('allhiretabunsel.png', confidence=0.9)
        #     location2 = self.pyautogui.locateOnScreen('allhiretabsel.png', confidence=0.9)
        #     if location != None:
        #         print('I have located the allhire tab. It is not in focus.')
        #         location = self.pyautogui.center(location)
        #         x, y = location
        #         self.pyautogui.click(x, y)
        #         print('allhire tab is now in focus.')
        #         break
        #     elif location2 != None:
        #         print('I have located the allhire tab. It is already in focus')
        #         break
        #     else:
        #         print('Cannot locate all hire tab at all')
        #         if processes().check_iflocation_found('TSSicon.png', 0.9) == True:
        #             print('I have found the Remote Desktop icon on my taskbar and selected it')
        #         location = self.pyautogui.locateOnScreen('allhiretabunsel.png', confidence=0.9)
        #         location2 = self.pyautogui.locateOnScreen('allhiretabsel.png', confidence=0.9)
        #         if location != None:
        #             print('The Remote Desktop is now open and I can now see the allhire tab! It is currently out of focus.')
        #             location = self.pyautogui.center(location)
        #             x, y = location
        #             self.pyautogui.click(x, y)
        #             print('allhire tab is now in focus.')
        #             break
        #         elif location2 != None:
        #             print('The Remote Desktop is now open and I can now see the allhire tab! It is currently already in focus.')
        #             break

    def click_thisORthat_tab(self,mystr_1,c1,mystr_2,c2):
        while True:
            location1 = self.pyautogui.locateOnScreen(mystr_1, confidence=c1)
            location2 = self.pyautogui.locateOnScreen(mystr_2, confidence=c2)
            if location1 != None:
                processes().justclick(mystr_1, c1)
                break
            elif location2 != None:
                processes().justclick(mystr_2, c2)
                break
            else:
                pass

    # Opens any job.

    def open_job(self, jobref):
        print('PROCESS TO OPEN JOB REF {} STARTS NOW'.format(jobref))
        try:
            if processes().check_iflocation_found('findref.png', 0.8) == True:
                processes().locate_and_click('findref.png', 0.8)

                location = self.pyautogui.locateOnScreen('highlightref.png', confidence=0.8)
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.dragTo(x, y, button='left')
                self.pyautogui.press('backspace')
                self.pyautogui.typewrite(str(jobref))
                processes().justclick('searchref.png',0.9)
        except TypeError:
            processes().focusrefocus()
        processes().open_firmorquote_job(jobref)

    def open_firmorquote_job(self, jobref):
        while True:
            location = self.pyautogui.locateOnScreen('firmbooking.png', confidence=0.9)
            location2 = self.pyautogui.locateOnScreen('quotebooking.png', confidence=0.9)
            if location != None:
                print('Job ref, {}, has now loaded. It is FIRM.'.format(jobref))
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.moveTo(x, y)
                self.pyautogui.click(clicks=2)
                print('Job ref, {} will now open'.format(jobref))
                processes().isjob_open(jobref)
                break
            elif location2 != None:
                print('Job ref, {}, has now loaded. It is in QUOTE!!!'.format(jobref))
                my_reply = input('Reply with all lowercase, yes, if you want to continue. NOTE: Your reply is case-sensitive!')
                if 'yes' in my_reply:
                    my_reply = input('Are you sure? I will only continue if you reply with yes again.')
                    if 'yes' in my_reply:
                        location2 = self.pyautogui.center(location2)
                        x, y = location2
                        self.pyautogui.moveTo(x, y)
                        self.pyautogui.click(clicks=2)
                        print('Job ref, {} will now open'.format(jobref))
                        processes().isjob_open(jobref)
                        break
                    else:
                        print('Program has halted.')
                        exit(0)
                else:
                    print('Program has halted.')
                    exit(0)

    def isjob_open(self, jobref):
        loop_counter = 1
        while True:
            location = self.pyautogui.locateOnScreen('jobopened.png', confidence=0.9)
            if location != None:
                print('Job ref, {} has opened!'.format(jobref))
                location = self.pyautogui.locateOnScreen('readonly.png', confidence=0.9)
                if location != None:
                    print('Someone else is on the job!'.format(jobref))
                    processes().close_job()
                    break
                else:
                    break
            else:
                if loop_counter == 1:
                    # print('Loop {} : Job ref, {} has not opened yet.'.format(loop_counter, self.jobref))
                    print('Please wait.')
                    loop_counter = loop_counter + 1
                else:
                    # print('Loop {} : Job ref, {} has not opened yet.'.format(loop_counter, self.jobref))
                    loop_counter = loop_counter + 1

    # Minimizes any currently opened job.

    def minimizejob(self, jobref):
        location = self.pyautogui.locateOnScreen('minimizejob.png', confidence=0.9)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)
        print('I have now minimized job ref {}.'.format(jobref))

    # Closes any currently opened job.

    def close_job(self):
        print('I will now close this job.')
        closejob = self.pyautogui.locateOnScreen('closejob.png', confidence=0.9)
        x = closejob.left + closejob.width - 10
        y = closejob.top + 20
        self.pyautogui.click(x, y)
        while True:
            location = self.pyautogui.locateOnScreen('jobopened.png', confidence=0.9)
            if location != None:
                print('Please wait.'.format(jobref))
            else:
                print('Job ref, {}, has successfully closed.'.format(jobref))
                break

    # Reformats the windows on my screen.

    def issql_intheway_orisallhiretab_outoffocus(self):
        while True:
            location = self.pyautogui.locateOnScreen('sql.png', confidence=0.9)
            if location != None:
                processes().movesql_outtheway()
                print('Reformatting window sizes complete.')
                break
            elif location == None:
                processes().open_allhiretab()
                break
            else:
                print('SQL is not in the way and allhire tab is in focus! Error is somewhere else.')
                break

    def movesql_outtheway(self):
        location = self.pyautogui.locateOnScreen('sql.png', confidence=0.9)
        xdragfrom = location.left
        ydragfrom = location.top
        self.pyautogui.moveTo(xdragfrom, ydragfrom)
        location = self.pyautogui.locateOnScreen('lowersql.png', confidence=0.9)
        x = location.left
        y = location.top
        self.pyautogui.dragTo(x, y, button='left')
        processes().focusrefocus()

    def focusrefocus(self):
        if processes().check_iflocation_found('focusrefocus.png', 0.9) == True:
            processes().justclick('focusrefocus.png',0.9)
        elif processes().check_iflocation_found('allhiretabsel.png', 0.9) == True:
            processes().justclick('allhiretabsel.png', 0.9)
        elif processes().check_iflocation_found('allhiretabunsel.png', 0.9) == True:
            processes().justclick('allhiretabunsel.png', 0.9)
        elif processes().check_iflocation_found('focusrefocus2.png', 0.9) == True:
            processes().justclick('focusrefocus2.png', 0.9)
        else:
            pass

    # Going to different tabs inside a job.

    def goto_summarytab(self):
        while True:
            location = self.pyautogui.locateOnScreen('summarytabunsel.png', confidence=0.9)
            location2 = self.pyautogui.locateOnScreen('summarytabsel.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Summary tab')
                break

    def goto_prevraisedinvoicestab(self):
        while True:
            location = self.pyautogui.locateOnScreen('prevraisedinvoicestab.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Previously Raised Invoices tab')
                break

    def goto_detailstab(self):
        location = self.pyautogui.locateOnScreen('detailstab.png', confidence=0.9)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)
        print('I have selected the Details tab.')

        while True:
            location = self.pyautogui.locateOnScreen('jobref.png', confidence=0.9)
            if location != None:
                self.pyautogui.hotkey('ctrl', 'c')
                jobref = self.pyperclip.paste()
                break

    def goto_invoicingtab(self):
        while True:
            location = self.pyautogui.locateOnScreen('invoicingtabunsel.png', confidence=0.9)
            location2 = self.pyautogui.locateOnScreen('invoicingtabsel.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Invoicing tab')
                break

    def goto_invproductiontab(self):
        while True:
            location = self.pyautogui.locateOnScreen('invoiceproductionunsel.png', confidence=0.9)
            location2 = self.pyautogui.locateOnScreen('invoiceproductionsel.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Invoice Production tab.')
                break

    def goto_mainhireinvoicetab(self):
        while True:
            location = self.pyautogui.locateOnScreen('mainhireinvoicetabunsel.png', confidence=0.9)
            location2 = self.pyautogui.locateOnScreen('mainhireinvoicetabsel.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Main Hire Invoice tab.')
                break
            elif location2 != None:
                print('Main Hire Invoice tab is already selected.')
                break
            else:
                print('Please wait.')
                # just wait.

    def goto_depositinvoicetab(self):
        while True:
            location = self.pyautogui.locateOnScreen('depositinvtab.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Deposit Invoice tab.')
                break

    def goto_additionalinvtab(self):
        while True:
            location = self.pyautogui.locateOnScreen('addinvtab.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Additional Invoice tab.')
                break

    def goto_creditnotetab(self):
        while True:
            location = self.pyautogui.locateOnScreen('creditnotetab.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Credit Note tab.')
                break

    def goto_repeatinvoicingtab(self):
        while True:
            location = self.pyautogui.locateOnScreen('repeatinvoicingtab.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have selected the Repeat Invoicing tab.')
                break

    def goto_reportstab(self):
        location = self.pyautogui.locateOnScreen('reportstab.png', confidence=0.9)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)
        print('I have selected the Reports tab.')

    # Raising Invoices.
    def selectprinter_and_produce(self):
        if processes().check_iflocation_found('selectprinter.png', 0.9) == True:
            print('I have selected a printer to print invoice.')
        processes().justclick('printerproduce.png',0.9)

    def raisemainhire(self):
        processes().goto_mainhireinvoicetab()
        if processes().check_iflocation_found('invproductionproducebutton.png', 0.9) == True:
            print('I have selected the Produce invoice button.')
        processes().selectprinter_and_produce()

    def raiseaddinv(self):
        processes().goto_invoicingtab()
        processes().goto_invproductiontab()
        processes().goto_additionalinvtab()

    def raiseMIAI(self):
        processes().goto_invoicingtab()
        processes().goto_invproductiontab()
        processes().goto_additionalinvtab()

    def raiseTwoPercent(self):
        processes().goto_invoicingtab()
        processes().goto_invproductiontab()
        processes().goto_additionalinvtab()

    # Attaching invoices/receipts.

    def focuscurrentjob(self):
        processes().justclick('jobicon.png', 0.9)

    def attach_proformainv_orderconfirmation(self):
        while True:
            location = self.pyautogui.locateOnScreen('mainhireinvb4payment.png', confidence=0.9)
            if location != None:
                x = location.left + location.width - 20
                y = location.top + 20
                self.pyautogui.click(x, y)
                break
            else:
                print('Cannot locate Dropdown list. Please wait.')
        if processes().check_iflocation_found('orderconfprofinv.png', 0.9) == True:
            print('I have selected the Order Confirmation dropdown option')
        processes().locate_and_click('aspdfdropdown.png',0.9)
        if processes().check_iflocation_found('orderconfprofinv.png', 0.9) == True:
            print('I have selected the Email Proforma as PDF option.')

    def attach_vat_mainhireinv(self, jobref):
        while True:
            location = self.pyautogui.locateOnScreen('prevraised_cash.png', confidence=0.7)
            if location != None:
                while True:
                    location = self.pyautogui.locateOnScreen('mainhireinvraised.png', confidence=0.9)
                    if location != None:
                        location = self.pyautogui.center(location)
                        x, y = location
                        self.pyautogui.click(x, y)
                        break
                    else:
                        print('No Main Hire invoice raised.')
                break
        processes().prevraised_completeemail('prevraised_maininvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('PROFORMA - Main Hire Invoice', jobref)
        print('Main Hire Invoice attached.')
        processes().attach_TCs()
        print('T&Cs attached.')

    def locate_and_click(self,mystr,c):
        location = self.pyautogui.locateOnScreen(mystr, confidence=c)
        while True:
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                break
            else:
                print('Cannot locate {}'.format(mystr))

    def check_iflocation_found(self,mystr,c):
        while True:
            location = self.pyautogui.locateOnScreen(mystr, confidence=c)
            if location != None:
                return True

    def justclick(self,mystr,c):
        location = self.pyautogui.locateOnScreen(mystr, confidence=c)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)

    def attach_vat_mainhirereceipt(self, jobref):
        if processes().check_iflocation_found('prevraised_cash.png',0.7) == True:
            processes().locate_and_click('mainhireinvraised.png',0.9)
        processes().prevraised_completeemail('prevraised_maininvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Receipt', jobref)
        if processes().check_iflocation_found('receiptemailwindow.png',0.9) == True:
            print('Proforma email window has opened')
        print('Main Hire Invoice attached.')
        processes().focuscurrentjob()
        processes().locate_and_click('attachvatreceipt.png', 0.9)
        processes().prevraised_completeemail('prevraised_maininvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Main.2', jobref)
        print('Main Hire Receipt attached.')
        processes().focuscurrentjob()
        processes().goto_reportstab()
        processes().locate_and_click('reports_orderconf.png', 0.9)
        processes().reportstab_completeemail('orderconfirmationattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Main.3', jobref)
        print('Final Order Confirmation attached.')
        processes().attach_TCs()
        print('T&Cs attached.')

    def attach_vat_addinv(self, jobref):
        if processes().check_iflocation_found('prevraised_cash.png',0.7) == True:
            processes().justclick('addinvraised.png',0.9)
        processes().prevraised_completeemail('prevraised_addinvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Additional Invoice', jobref)
        print('Additional Invoice attached.')
        processes().attach_TCs()
        print('T&Cs attached.')

    def attach_vat_addinvreceipt(self, jobref):
        processes().attach_vat_addinv(jobref)
        processes().prevraised_completeemail('prevraised_addreceiptattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Additional Receipt', jobref)
        print('Additional Invoice attached.')
        processes().focuscurrentjob()
        processes().locate_and_click('attachaddreceipt.png', 0.9)
        processes().prevraised_completeemail('prevraised_addreceiptattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Add.2', jobref)
        print('Additional Receipt attached.')
        processes().focuscurrentjob()
        processes().goto_reportstab()
        processes().locate_and_click('reports_orderconf.png', 0.9)
        processes().reportstab_completeemail('orderconfirmationattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Add.3', jobref)
        print('Final Order Confirmation attached.')
        processes().attach_TCs()
        print('T&Cs attached.')

    # Email from TSS to Outlook.

    def prevraised_completeemail(self, type):
        processes().locate_and_click('prevraised_email.png', 0.9)
        processes().locate_and_click('prevraised_pdf.png', 0.9)
        if processes().check_iflocation_found(type, 0.9) == True:
            print('Invoice is attached.')
        processes().locate_and_click('prevraised_complete.png', 0.8)

    def selectallaccountsemails(self, num):

        def ACCOUNT_DIRECTOR():
            ACCOUNTDIRECTOR = self.pyautogui.locateOnScreen('ACCOUNTDIRECTOR.png', confidence=0.9)
            ACCOUNTDIRECTOR = self.pyautogui.center(ACCOUNTDIRECTOR)
            x, y = ACCOUNTDIRECTOR
            self.pyautogui.moveTo(x, y)
            self.pyautogui.click(clicks=2)

        def ACCOUNT_MANAGER():
            ACCOUNTMANAGER = self.pyautogui.locateOnScreen('ACCOUNTMANAGER.png', confidence=0.9)
            ACCOUNTMANAGER = self.pyautogui.center(ACCOUNTMANAGER)
            x, y = ACCOUNTMANAGER
            self.pyautogui.moveTo(x, y)
            self.pyautogui.click(clicks=2)

        def ACCOUNTANT_():
            ACCOUNTANT = self.pyautogui.locateOnScreen('ACCOUNTANT.png', confidence=0.9)
            ACCOUNTANT = self.pyautogui.center(ACCOUNTANT)
            x, y = ACCOUNTANT
            self.pyautogui.moveTo(x, y)
            self.pyautogui.click(clicks=2)

        def ppurchasing_email():
            ppurchasingemail = self.pyautogui.locateOnScreen('ppurchasingemail.png', confidence=0.9)
            ppurchasingemail = self.pyautogui.center(ppurchasingemail)
            x, y = ppurchasingemail
            self.pyautogui.moveTo(x, y)
            self.pyautogui.click(clicks=2)

        def PURCHASE_LEDGER():
            PURCHASELEDGER = self.pyautogui.locateOnScreen('PURCHASELEDGER.png', confidence=0.9)
            PURCHASELEDGER = self.pyautogui.center(PURCHASELEDGER)
            x, y = PURCHASELEDGER
            self.pyautogui.moveTo(x, y)
            self.pyautogui.click(clicks=2)

        mydict = {'ACCOUNT_DIRECTOR': ACCOUNT_DIRECTOR,
                  'ACCOUNT_MANAGER': ACCOUNT_MANAGER,
                  'ACCOUNTANT_': ACCOUNTANT_,
                  'ppurchasing_email': ppurchasing_email,
                  'PURCHASE_LEDGER': PURCHASE_LEDGER}
        keynames = ['ACCOUNT_DIRECTOR', 'ACCOUNT_MANAGER', 'ACCOUNTANT_', 'ppurchasing_email', 'PURCHASE_LEDGER']

        return mydict[keynames[num]]()

    def reportstab_completeemail(self, type):
        processes().justclick('reportsemail.png', 0.9)
        processes().locate_and_click('reportspdf.png', 0.9)
        if processes().check_iflocation_found(type, 0.9) == True:
            print('Invoice is attached.')
        processes().locate_and_click('reportscomplete.png', 0.8)

    def sendemail_fromtss(self):
        processes().locate_and_click('emailto.png', 0.7)
        while True:
            location = self.pyautogui.locateOnScreen('jobcontactemail.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.moveTo(x, y)
                self.pyautogui.click(clicks=2)
                print('I have selected the Main Job Contact email.')
                break
        num = 0
        x = 6
        while num < x:
            try:
                processes().selectallaccountsemails(num)
                num = num + 1
            except:
                num = num + 1
        print('I have checked for all accounts  emails and CCed them if found.')
        location = self.pyautogui.locateOnScreen('emailto_ok.png', confidence=0.9)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)
        processes().locate_and_click('displayasemail.png', 0.9)

    def email_tooutlook(self, mysubject, jobref):
        while True:
            location = self.pyautogui.locateOnScreen('emailsubject.png', confidence=0.9)
            if location != None:
                print('I will now enter subject of email.')
                x = location.left + (location.width*5)
                y = location.top + 5
                self.pyautogui.moveTo(x, y)
                self.pyautogui.click(clicks=3)
                self.pyautogui.typewrite(mysubject + ' Ref ' + jobref)
                location = self.pyautogui.locateOnScreen('emailsend.png', confidence=0.9)
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                break
        while True:
            location = self.pyautogui.locateOnScreen('allowaccessfor.png', confidence=0.9)
            if location != None:
                print('popup found')
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                while True:
                    location = self.pyautogui.locateOnScreen('allow.png', confidence=0.9)
                    if location != None:
                        location = self.pyautogui.center(location)
                        x, y = location
                        self.pyautogui.click(x, y)
                        print('I have selected the email-Allow access for 1 minute-popup.')
                        break
                break
            else:
                print('popup not found. lets see if outlook is flashing.')
                while True:
                    location = self.pyautogui.locateOnScreen('outlookflash.png', confidence=0.9)
                    if location != None:
                        print('outlook flash found.')
                        location = self.pyautogui.center(location)
                        x, y = location
                        self.pyautogui.click(x, y)
                        self.time.sleep(3)
                        location = self.pyautogui.locateOnScreen('openflashmain.png', confidence=0.6)
                        if location != None:
                            location = self.pyautogui.center(location)
                            x, y = location
                            self.pyautogui.click(x, y)
                            break
                        else:
                            break

    def attach_TCs(self):
        while True:
            location = self.pyautogui.locateOnScreen('proformaemailwindow.png', confidence=0.8)
            if location != None:
                location = self.pyautogui.locateOnScreen('attachfile.png', confidence=0.8)
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                break
        while True:
            location = self.pyautogui.locateOnScreen('TCs.png', confidence=0.8)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have now attached Terms & Conditions file.')
                break

    # Sending reminders/receipts.

    def r_proforma_rem(self, jobref):
        print('I will now send a Proforma Invoice')
        location = self.pyautogui.locateOnScreen('detailstab.png', confidence=0.9)
        location = self.pyautogui.center(location)
        x, y = location
        self.pyautogui.click(x, y)
        print('I have selected the Details tab.')
        while True:
            location = self.pyautogui.locateOnScreen('jobref.png', confidence=0.9)
            if location != None:
                self.pyautogui.hotkey('ctrl', 'c')
                jobref = self.pyperclip.paste()
                break
        processes().goto_invoicingtab()
        processes().goto_invproductiontab()
        processes().attach_proformainv_orderconfirmation()
        processes().sendemail_fromtss()
        processes().email_tooutlook('PROFORMA - Main Hire Invoice', jobref)
        processes().attach_TCs()

    def r_vat_mainhire_rem(self, jobref):
        print('I will now send a VAT Invoice')
        processes().goto_invoicingtab()
        processes().goto_prevraisedinvoicestab()
        processes().attach_vat_mainhireinv(jobref)
        processes().prevraised_completeemail('prevraised_maininvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('VAT Invoice', jobref)

    def r_vat_mainhire_receipt(self, jobref):
        print('I will now send a VAT receipt')
        processes().goto_invoicingtab()
        processes().goto_prevraisedinvoicestab()
        processes().attach_vat_mainhirereceipt(jobref)
        processes().prevraised_completeemail('prevraised_mainreceiptattached.png')


    def r_addinv_rem(self, jobref):
        print('I will now send an Additional Invoice reminder')
        processes().goto_invoicingtab()
        processes().goto_prevraisedinvoicestab()
        processes().attach_vat_addinv(jobref)
        processes().prevraised_completeemail('prevraised_addinvattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Additional Invoice', jobref)


    def r_addinv_receipt(self, jobref):
        print('I will now send an Additional Receipt')
        processes().goto_invoicingtab()
        processes().goto_prevraisedinvoicestab()
        processes().attach_vat_addinvreceipt(jobref)
        processes().prevraised_completeemail('prevraised_addreceiptattached.png')
        processes().sendemail_fromtss()
        processes().email_tooutlook('Additional Receipt', jobref)


    def findjobref_byinvnumber(self, invoicenumber):
        processes().focusrefocus()
        print('PROCESS TO FIND JOB REF BY INVOICE NUMBER STARTS NOW')
        location = self.pyautogui.locateOnScreen('searchbyinv.png', confidence=0.9)
        x = location.left + location.width - 10
        y = location.top + 10
        self.pyautogui.click(x, y)
        while True:
            location = self.pyautogui.locateOnScreen('invfind.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                break
            else:
                print('Please wait.')
        while True:
            location = self.pyautogui.locateOnScreen('invdragfrom.png', confidence=0.9)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                location = self.pyautogui.locateOnScreen('invdragto.png', confidence=0.9)
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.dragTo(x, y, button='left')
                self.pyautogui.press('backspace')
                self.pyautogui.typewrite(str(invoicenumber))
                location = self.pyautogui.locateOnScreen('searchinv.png', confidence=0.95)
                x = location.left + location.width - 10
                y = location.top + 10
                self.pyautogui.click(x, y)
                break
        while True:
            location = self.pyautogui.locateOnScreen('invclickjob.png', confidence=0.85)
            if location != None:
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('I have clicked on the job.')
                location = self.pyautogui.locateOnScreen('invopenjob.png', confidence=0.9)
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                print('Please wait for job to now open.')
                break
        while True:
            location = self.pyautogui.locateOnScreen('invclickjob.png', confidence=0.85)
            if location != None:
                print('Job is now open!')
                processes().goto_detailstab()
                self.pyautogui.hotkey('ctrl','c')
                jobref = self.pyperclip.paste()
                print('This job ref is {}.'.format(jobref))


    ############################################
    def tempreceipt(self):
        processes().isjob_open(jobref)
        processes().goto_prevraisedinvoicestab()
        while True:
            location = self.pyautogui.locateOnScreen('prevraisedinvtabopened.png', confidence=0.75)
            if location != None:
                print('Previously Raised Invoice tab is now open.')
                location = self.pyautogui.locateOnScreen('mainhireinvraised.png', confidence=0.9)
                location2 = self.pyautogui.locateOnScreen('addinvraised.png', confidence=0.9)
                if location != None:
                    if location2 != None:
                        print('The Main Hire Invoice and Additional Invoice is both already raised!')
                        processes().goto_detailstab()
                        jobref = self.pyperclip.paste()
                        processes().pay(amountpaid)
                        break
                elif location != None:
                    print('Main Hire Invoice is already raised.')
                    processes().goto_detailstab()
                    jobref = self.pyperclip.paste()
                    processes().pay(amountpaid)
                    break
                elif location2 != None:
                    print('Additional Invoice is already raised.')
                    processes().goto_detailstab()
                    jobref = self.pyperclip.paste()
                    processes().pay(amountpaid)
                    break
                else:
                    print('No invoice raised yet.')
                    processes().goto_detailstab()
                    jobref = self.pyperclip.paste()
                    processes().pay(amountpaid)
                    break
    ################################################
    def pay(self, amountpaid):
        while True:
            location = self.pyautogui.locateOnScreen('jobref.png', confidence=0.9)
            if location != None:
                print('Details tab is now open!')

            location1 = self.pyautogui.locateOnScreen('depositpay.png', confidence=0.8)
            location2 = self.pyautogui.locateOnScreen('finalbalance.png', confidence=0.8)
            location3 = self.pyautogui.locateOnScreen('addinvpay.png', confidence=0.8)
            location4 = self.pyautogui.locateOnScreen('addinv2pay.png', confidence=0.8)
            if location1 != None:
                print('I will now enter payment amount {} and show it as paid.'.format(amountpaid))
                break
            elif location2 != None:
                print('I will now enter payment amount {} and show it as paid.'.format(amountpaid))
                break
            elif location3 != None:
                print('I will now enter payment amount {} and show it as paid.'.format(amountpaid))
                break
            elif location4 != None:
                print('I will now enter payment amount {} and show it as paid.'.format(amountpaid))
                break
            else:
                print('ERROR! - All payment boxes are fully filled up! No space.')
                break

    # Opens multiple jobs.

    def open_multiplejobs(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().focusrefocus()

    # Sending multiple reminders/receipts.

    def sendmultipleproforma_reminders(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().r_proforma_rem(joblist[x])

    def sendmultiple_VAT_reminders(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().r_vat_mainhire_rem(joblist[x])

    def sendmultiple_VAT_receipts(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().r_vat_mainhire_receipt(joblist[x])

    def sendmultiple_ADDINV_reminders(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().r_addinv_rem(joblist[x])

    def sendmultiple_ADDINV_receipts(self, joblist):
        processes().issql_intheway_orisallhiretab_outoffocus()
        processes().focusrefocus()
        for x in range(len(joblist)):
            processes().open_job(joblist[x])
            processes().r_addinv_receipt(joblist[x])

processes().open_allhiretab()
#processes().sendmultiple_VAT_receipts([''])

# def cleanaccounts(self):


# def r_vat(self):
#
# def r_addinv(self):
#
# def r_baddebt(self):

#
# def miai(self):
#
# def r_receipt(self, invoicenumber, self.jobref, amountpaid):
# if self.jobref != 0:
# if invoicenumber == 0:
# then open job by self.jobref
# elif self.jobref == 0:
# if invoicenumber != 0:
# open job by invoicenumber
# else:
# print(please enter either 'invoicenumber, 0, amountpaid')
# print(or enter '0, self.jobref, amountpaid')

# if exact amount of invoice is recorded on the job:
# then send receipt email