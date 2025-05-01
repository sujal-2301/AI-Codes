import time


def simulate_typing(text, delay=0.03):
    """
    Simulate a typing effect by printing each character with a slight delay.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline after the message


def show_main_menu():
    simulate_typing("\nWelcome to Business CatBot!")
    simulate_typing("How can I assist you today?")
    simulate_typing("Please choose one of the following options:")
    simulate_typing("1. Product Information")
    simulate_typing("2. Pricing")
    simulate_typing("3. Technical Support")
    simulate_typing("4. Speak to an Agent")
    simulate_typing("5. Exit")


def product_information():
    simulate_typing("\n[Product Information]")
    simulate_typing(
        "Our products are designed to be efficient, reliable, and easy to integrate into your business.")
    simulate_typing(
        "For detailed specs, please visit our website or contact our sales team.")
    input("Press Enter to return to the main menu...")


def pricing_information():
    simulate_typing("\n[Pricing Information]")
    simulate_typing("We offer competitive pricing tailored to your needs.")
    simulate_typing("Would you like to:")
    simulate_typing("1. Receive a custom quote")
    simulate_typing("2. View standard pricing plans")
    simulate_typing("3. Return to Main Menu")

    choice = input("Please enter your choice (1-3): ")
    if choice == '1':
        simulate_typing(
            "\nTo receive a custom quote, please email our sales team at sales@example.com.")
    elif choice == '2':
        simulate_typing(
            "\nOur standard pricing plans start at $99 per month. More details are available on our website.")
    else:
        simulate_typing("\nReturning to the main menu...")

    input("Press Enter to return to the main menu...")


def technical_support():
    simulate_typing("\n[Technical Support]")
    simulate_typing("Our technical support team is here to help 24/7.")
    simulate_typing("Please describe the issue you're experiencing:")
    issue = input("Your issue: ")
    simulate_typing("Thank you for reporting the issue.")
    simulate_typing(
        "Our support team will review your concern and get back to you shortly.")
    input("Press Enter to return to the main menu...")


def speak_to_agent():
    simulate_typing("\n[Speak to an Agent]")
    simulate_typing("An agent will be with you shortly.")
    simulate_typing("Please wait while we connect you...")
    time.sleep(2)
    simulate_typing("All agents are currently busy.")
    simulate_typing(
        "Please leave your contact details and we will call you back as soon as possible.")
    name = input("Your Name: ")
    phone = input("Your Phone Number: ")
    simulate_typing(f"Thank you, {name}. We will contact you at {phone} soon.")
    input("Press Enter to return to the main menu...")


def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            product_information()
        elif choice == '2':
            pricing_information()
        elif choice == '3':
            technical_support()
        elif choice == '4':
            speak_to_agent()
        elif choice == '5':
            simulate_typing("\nThank you for using Business CatBot. Goodbye!")
            break
        else:
            simulate_typing("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
