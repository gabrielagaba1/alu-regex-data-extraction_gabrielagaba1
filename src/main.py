import re
import json

def get_emails(document_text):
    all_emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", document_text)
    staff_emails = re.findall(r"[\w\.-]+@alueducation\.com", document_text)
    alumni_emails = re.findall(r"[\w\.-]+@alumni\.alueducation\.com", document_text)
    intern_emails = re.findall(r"[\w\.-]+@si\.alueducation\.com", document_text)
    return {
        "all": all_emails,
        "staff": staff_emails,
        "alumni": alumni_emails,
        "interns": intern_emails
    }

def get_masked_cards(document_text):
    card_pattern = r"\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}"
    raw_cards = re.findall(card_pattern, document_text)
    masked_list = []
    for card in raw_cards:
        digits = card.replace("-", "").replace(" ", "")
        masked_list.append(digits[:4] + "-****-****-" + digits[-4:])
    return masked_list

def get_phone_numbers(document_text):
    return re.findall(r"\+250[\d\s]{12}|07[\d\s]{10}", document_text)

def get_links(document_text):
    return re.findall(r"https?://\S+", document_text)

def get_currencies_and_times(document_text):
    currencies = re.findall(r"[\d,]+\s?Rwf", document_text)
    times = re.findall(r"\d{1,2}:\d{2}\s?[AP]M", document_text)
    return currencies, times

def check_for_threats(document_text):
    return bool(re.search(r"<script|drop table", document_text, re.IGNORECASE))

def main():
    with open("../input/raw-text.txt", "r") as text_file:
        document_text = text_file.read()

    email_data = get_emails(document_text)
    card_data = get_masked_cards(document_text)
    phone_data = get_phone_numbers(document_text)
    link_data = get_links(document_text)
    currency_data, time_data = get_currencies_and_times(document_text)
    threat_detected = check_for_threats(document_text)

    final_output = {
        "emails": email_data,
        "credit_cards": card_data,
        "phone_numbers": phone_data,
        "web_links": link_data,
        "currencies": currency_data,
        "times": time_data,
        "security_threat_detected": threat_detected
    }

    with open("../output/sample-output.json", "w") as output_file:
        json.dump(final_output, output_file, indent=4)

    print("Data extraction complete! Results saved in output/sample-output.json")

if __name__ == "__main__":
    main()