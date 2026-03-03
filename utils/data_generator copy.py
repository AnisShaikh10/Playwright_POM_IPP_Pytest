import re
import random, string
from dataclasses import dataclass
from typing import Optional
from faker import Faker

COUNTRY_LOCALES = {
    "UK": "en_GB",
    "India": "en_IN",
    "US": "en_US",
    "Australia": "en_AU"
}

TITLES = ["Mrs", "Miss", "Mr", "Ms"]
GENDERS = ["Male", "Female"]
NAME_PREFIX = "UAT_"

@dataclass
class UserProfile:
    title: str
    first_name: str
    last_name: str
    gender: str
    dob: str           # DD/MM/YYYY
    email: str
    country: str       # the selected country key (e.g., "UK")

@dataclass
class ResidenceDetails:
    address_country: str
    postal_code: str
    address_line1: str
    country_of_birth: str
    legal_nationality: str
    passport_number: str
    country_of_residence: str
    residential_category: str
    require_student_visa: str

def generate_dob() -> str:
    year = random.randint(1993, 2006)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}/{month:02d}/{year:04d}"

def generate_residence_details(fee_status: str = "H") -> ResidenceDetails:
    if fee_status == "H":
        return ResidenceDetails(
            address_country = "United Kingdom",
            postal_code = "SO14 0YN",
            address_line1 = "Test Addr 34566",
            country_of_birth = "United Kingdom",
            legal_nationality = "UK national",
            passport_number = "GT65432179",
            country_of_residence = "England",
            residential_category = "UK Citizen - England",
            require_student_visa = "No"
        )
    else:
        return ResidenceDetails(
            address_country = "Australia",
            postal_code = "AU 22 T0S",
            address_line1 = "Test Addr 34566",
            country_of_birth = "Australia",
            legal_nationality = "Australian",
            passport_number = "GT65432179",
            country_of_residence = "Australia",
            residential_category = "Overseas",
            require_student_visa = "Yes"
        )
    
def clean_string(value: str) -> str:
    # Remove anything that is not letter or number
    return re.sub(r"[^A-Za-z0-9]", "", value)

def generate_user(fee_status: Optional[str] = None) -> UserProfile:
    """
    Create a user with locale-aware names and a consistent shape for POM consumption.
    Pass country in {"UK","India","US","Australia"} or leave None for random.
    """

    """
    Create a user based on fee status:
    H → UK
    O → Non-UK (random except UK)
    """
    # Decide country based on fee status
    if fee_status == "H":
        country = "UK"

    elif fee_status == "O":
        non_uk_countries = [c for c in COUNTRY_LOCALES.keys() if c != "UK"]
        country = random.choice(non_uk_countries)

    else:
        # Default behavior (random from all)
        country = random.choice(list(COUNTRY_LOCALES.keys()))

    fake = Faker(COUNTRY_LOCALES[country])

    title = random.choice(TITLES)
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(GENDERS)
    # Clean names for email
    clean_first = clean_string(first_name)
    clean_last = clean_string(last_name)
    email = f"{NAME_PREFIX}{clean_first}{clean_last}@mailinator.com"
    dob = generate_dob()

    return UserProfile(
        title=title,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        dob=dob,
        email=email,
        country=country
    )

# generate paragraph between 1001 to 3999 words
def generate_random_paragraph(min_chars=1001, max_chars=3999):
    words = []
    total_length = 0
    while total_length < min_chars:
        word_length = random.randint(3, 10)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
        total_length = sum(len(w) for w in words) + len(words) - 1
        if total_length >= max_chars:
            break
    paragraph = " ".join(words)
    return paragraph[:max_chars]