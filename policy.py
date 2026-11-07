import pytest
from playwright.sync_api import sync_playwright, Page

BASE_URL="https://www.testerrank.com/insurance"

@pytest.fixture
def page_context():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page=context.new_page()
        yield page
        context.close()
        browser.close()

def test_customer_login(page_context: Page):
    page=page_context
    page.goto(BASE_URL)
    page.locator('[data-testid="logout-btn"]').click()
    page.locator('[data-testid="navLogin"]').click()
    page.get_by_placeholder("Enter your email").fill("rajesh@insurance.com")
    page.get_by_placeholder("Enter your password").fill("Insure@123")
    page.locator("#loginBtn").click()

@pytest.fixture
def login_page(page_context: Page):
    page=page_context
    page.goto(BASE_URL)
    page.locator('[data-testid="logout-btn"]').click()
    page.locator('[data-testid="navLogin"]').click()
    page.get_by_placeholder("Enter your email").fill("rajesh@insurance.com")
    page.get_by_placeholder("Enter your password").fill("Insure@123")
    page.locator("#loginBtn").click()
    return page

def test_menu(login_page: Page):
    page=login_page

    menu1=["Dashboard","Buy Policy","Payments","Claims","Support","Renew"]

    menu2=["Calculator","Claims","Documents","Nominees"]

    for m1 in menu1:
        page.get_by_role("link", name=m1,exact=True).first.is_visible()
        print(m1, "is visible")

    page.get_by_role("link", name="Buy Policy", exact=True).first.click()

    for m2 in menu2:
        page.get_by_role("link", name=m2, exact=True).first.is_visible()
        print(m2, "is visible")

def test_calculator(login_page: Page):
    page=login_page

    page.get_by_role("link", name="Calculator").click()
    page.locator("#calcPolicyType").select_option(label="Health Insurance")
    page.locator('[data-testid="calc-plan"]').select_option(index=2)
    page.locator('[data-testid="calc-dob"]').fill("2002-02-09")
    page.locator('[data-testid="sum-insured"]').select_option(index=2)
    page.locator('[data-testid="coverage-term"]').select_option(index=4)
    page.locator('[data-testid="calc-smoker"]').check()
    page.locator("#calcCondDiabetes").check()
    page.locator('[data-testid="calculate-premium-btn"]').click()
    page.locator('[data-testid="buy-this-plan-link"]').click()
    page.locator("#policyType_health").click()
    page.locator("#policyType_health").click()
    page.locator("#plan_Basic_Health").click()
    page.locator("#continueBtn1").click()
    page.get_by_placeholder("Enter full name as per PAN").fill("Rahul XYZ")
    page.locator('[data-testid="gender-male"]').click()
    page.get_by_placeholder("12-digit Aadhaar").fill("321489063214")
    page.locator('[data-testid="applicant-email"]').fill("pamewos955@boffweb.com")
    page.locator("#annualIncome").select_option(index=2)
    page.locator("#applicantDob").fill("2001-01-01")
    page.get_by_placeholder("ABCDE1234F").fill("DFGAS1234F")
    page.locator("#applicantMobile").fill("4324352421")
    page.locator("#occupation").select_option(index=4)
    page.get_by_role("button", name="Continue").click()
    page.locator("#height").fill("172")
    page.locator("#weight").fill("67")
    page.get_by_role("checkbox", name="None of the above").check()
    page.get_by_role("button", name="Continue").click()
    page.locator("#nomineeName").fill("Mehul Awasthi")
    page.locator("#nomineeDob").fill("2001-02-28")
    page.locator('[data-testid="nominee-share-0"]').fill("50")
    page.locator("#nomineeRelation").select_option(index=3)
    page.locator("#nomineeAadhaar").fill("643431232134")
    page.get_by_role("button", name="Add Another Nominee").click()
    page.locator("#nomineeName_1").fill("Jeevan Awasthi")
    page.locator("#nomineeDob_1").fill("2002-01-28")
    page.locator('[data-testid="nominee-share-1"]').fill("50")
    page.locator("#nomineeRelation_1").select_option(index=2)
    page.locator("#nomineeAadhaar_1").fill("643431232134")
    page.get_by_role("button", name="Continue").click()
    page.locator("#paymentMethod_netbanking").click()
    page.get_by_role("button", name="Pay & Submit Application").click()
    page.locator("#confirmationDetails")
    page.locator('[data-testid="download-policy-doc"]').click()
    print("Policy Number:- ", page.locator('[data-testid="policy-number"]').inner_text())
    
def test_policy_clamis(login_page: Page):
    page=login_page
    page.locator('[data-testid="nav-claims"]').click()
    page.locator("#followUpDate").click()
    page.get_by_role("button", name="Schedule").click()
    page.get_by_role("button", name="File New Claim").click()
    page.locator('[data-testid="claimPolicy"]').select_option(index=1)
    page.locator('[data-testid="claimType"]').select_option(index=1)
    page.locator('[data-testid="incidentDate"]').fill("2026-11-01") 
    page.get_by_placeholder("Enter amount").fill("120000")
    page.locator('[data-testid="incidentDescription"]').fill("Testing insurance clamins")
    page.get_by_placeholder("Enter hospital, provider or location").fill("pune")
    page.get_by_role("button", name="Next").click()
    page.locator('[data-testid="docBills"]').set_input_files(r"C:\Users\CHINMAY\OneDrive\Pictures\Screenshots\Screenshot 2026-11-05 164452.png")
    page.locator('[data-testid="docDischarge"]').set_input_files(r"C:\Users\CHINMAY\OneDrive\Pictures\Screenshots\Screenshot 2026-09-18 140257.png")
    page.locator('[data-testid="docPrescription"]').set_input_files(r"C:\Users\CHINMAY\OneDrive\Pictures\Screenshots\Screenshot 2026-08-23 111836.png")
    page.locator("#docIdProof").set_input_files(r"C:\Users\CHINMAY\OneDrive\Pictures\Screenshots\Screenshot 2026-08-23 110701.png")
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Account holder name").fill("Rahul Bose")
    page.locator("#claimAccountNo").fill("4567 2341 0898 2523")
    page.locator("#claimAccountConfirm").fill("4567 2341 0898 2523")
    page.locator("#claimIfsc").fill("SBIN0001234")
    print(page.locator("#claimBankName").inner_text())
    page.locator("#acTypeCurrent").check()
    page.get_by_role("button", name="Next").click()
    page.locator("#claimDeclaration").check()
    page.get_by_role("button", name="Submit Claim").click()
    print("Claim Number:- ", page.locator('[data-testid="claimRefNumber"]').inner_text())
    page.locator("#claimSuccessClose").click()

def test_calculator1(login_page: Page):
    page=login_page
    page.get_by_role("link", name="Calculator").click()
    page.locator("#calcPolicyType").select_option(label="Health Insurance")
    page.locator('[data-testid="calc-plan"]').select_option(index=2)
    page.locator('[data-testid="calc-dob"]').fill("1996-11-06")
    page.locator('[data-testid="sum-insured"]').select_option(index=2)
    page.locator('[data-testid="coverage-term"]').select_option(index=4)
    page.locator('[data-testid="calculate-premium-btn"]').click()
    print("If the age is 30")
    print("Monthly:- ", page.locator('[data-testid="result-monthly"]').inner_text())
    print("Quarterly:- ", page.locator('[data-testid="result-quarterly"]').inner_text())
    print("Annual:- ", page.locator('[data-testid="result-annual"]').inner_text())

    page.locator('[data-testid="calc-dob"]').fill("1981-11-06")
    page.locator('[data-testid="calc-smoker"]').check()
    page.locator("#calcCondDiabetes").check()
    page.locator('[data-testid="calculate-premium-btn"]').click()
    print("If the age is above 45")
    print("Monthly:- ", page.locator('[data-testid="result-monthly"]').inner_text())
    print("Quarterly:- ", page.locator('[data-testid="result-quarterly"]').inner_text())
    print("Annual:- ", page.locator('[data-testid="result-annual"]').inner_text())

def test_upload_document(login_page: Page):
    page=login_page
    page.get_by_role("link", name="Documents").click()
    page.locator('[data-testid="document-upload"]').set_input_files(r"C:\Users\CHINMAY\OneDrive\Pictures\Screenshots\Screenshot 2026-10-05 135846.png")
    page.locator('[data-testid="document-type"]').select_option(index=1)
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(20000)

def test_nominees(login_page: Page):
    page=login_page
    page.get_by_role("link", name="Nominees").click()
    page.locator('[data-testid="add-nominee-btn"]').click()
    page.get_by_placeholder("Enter nominee name").fill("Chinmay")
    page.locator("#nomineeRelation").select_option(index=3)
    page.locator("#nomineeShare").fill("100")
    page.locator('[data-testid="nominee-dob"]').fill("2004-09-01")
    page.get_by_role("button", name="Save Nominee").click()
    page.locator("#editNomineeBtn0").click()
    page.locator('[data-testid="nominee-dob"]').fill("2002-01-02")
    page.locator('[data-testid="save-nominee-btn"]').click()
