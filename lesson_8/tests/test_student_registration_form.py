import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.student_registration_page import StudentRegistrationPage


@pytest.fixture
def registration_page(driver):
    page = StudentRegistrationPage(driver)
    page.open_and_prepare()
    return page


# =========================
# ПОЗИТИВНЫЕ ТЕСТЫ
# =========================

# 1. Проверяем, что форма отправляется с обязательными полями:
@pytest.mark.parametrize(
    "first_name, last_name, gender, phone",
    [
        ("Петр", "Петров", 1, "9001234567"),
        ("Anna", "Ivanova", 2, "1112223344"),
        ("Ivan", "Sidorov", 3, "9998887766"),
    ]
)
def test_successful_submit_with_required_fields(registration_page, first_name, last_name, gender, phone):
    registration_page.fill_required_fields(first_name, last_name, gender=gender, phone=phone)

    registration_page.submit()
    registration_page.check_success_modal()

    for text in (first_name, last_name):
        registration_page.check_user_in_table(text)


# 2. После отправки формы ждём, пока в таблице результата появится название хобби (Fluent Wait)
@pytest.mark.parametrize(
    "hobby_number, expected_text",
    [
        (1, "Sports"),
        (2, "Reading"),
        (3, "Music"),
    ]
)
def test_fluent_wait_result_table_has_hobby_text(registration_page, driver, hobby_text):
    registration_page.fill_required_fields("Ivan", "Petrov", gender=1, phone="9049153045")
    registration_page.select_hobby(hobby_text)  # Sports
    registration_page.submit()

    wait = WebDriverWait(
        driver,
        timeout=6,
        poll_frequency=0.2,
        ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
    )

    wait.until(EC.text_to_be_present_in_element(registration_page.RESULT_TABLE, hobby_text))

    registration_page.check_user_in_table(hobby_text)


# 3. Проверяем отправку формы, где выбраны все доступные Subjects:
def test_positive_select_all_subjects(registration_page):
    registration_page.fill_required_fields("Ivan", "Petrov", gender=1, phone="9998887766")

    subjects = [
        "Maths", "Physics", "Chemistry", "Biology", "English",
        "Computer Science", "Economics", "History", "Hindi", "Civics", "Arts"
    ]

    for subject in subjects:
        registration_page.enter_subject(subject)

    registration_page.submit()
    registration_page.check_success_modal()

    for subject in subjects:
        registration_page.check_user_in_table(subject)


# 4. Проверяем отправку формы, где выбраны все доступные Hobbies:
def test_positive_select_all_hobbies(registration_page):
    registration_page.fill_required_fields("Anna", "Ivanova", gender=2, phone="1112223344")

    hobbies = [
        (1, "Sports"),
        (2, "Reading"),
        (3, "Music"),
    ]

    for hobby_number, _ in hobbies:
        registration_page.select_hobby(hobby_number)

    registration_page.submit()
    registration_page.check_success_modal()

    for _, hobby_name in hobbies:
        registration_page.check_user_in_table(hobby_name)


# =========================
# НЕГАТИВНЫЕ ТЕСТЫ
# =========================

# 1. Проверяем, что обязательные поля не пустые:
@pytest.mark.parametrize(
    "case, data",
    [
        ("empty_form", {}),
        ("missing_first_name", {"last_name": "Petrov", "gender": 1, "phone": "9001234567"}),
        ("missing_last_name", {"first_name": "Ivan", "gender": 1, "phone": "9001234567"}),
        ("missing_gender", {"first_name": "Ivan", "last_name": "Petrov", "phone": "9001234567"}),
        ("missing_phone", {"first_name": "Ivan", "last_name": "Petrov", "gender": 1}),
    ]
)
def test_negative_required_fields_not_submitted(registration_page, case, data):
    if "first_name" in data:
        registration_page.enter_first_name(data["first_name"])

    if "last_name" in data:
        registration_page.enter_last_name(data["last_name"])

    if "gender" in data:
        registration_page.select_gender(data["gender"])

    if "phone" in data:
        registration_page.enter_phone(data["phone"])

    registration_page.submit()

    assert registration_page.is_success_modal_opened() is False


# 2. Проверяем, что форма не отправляется с невалидным номером телефона:
@pytest.mark.parametrize(
    "case, phone",
    [
        ("empty", ""),
        ("too short", "8904"),
        ("with plus", "+79049153045"),
        ("only letters", "abcdefghij"),
        ("numbers and letters", "89049abcde"),
        ("numbers and special simbols", "89049153!@")
    ]
)
def test_negative_invalid_phone_not_submitted(registration_page, case, phone):
    registration_page.fill_required_fields("Ivan", "Petrov", gender=1, phone=phone)
    registration_page.submit()

    assert registration_page.is_success_modal_opened() is False