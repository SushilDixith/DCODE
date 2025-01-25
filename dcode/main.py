import random
import time
from hashing import md5, sha1, sha256

def colorful_dcode():
    """Displays 'DCODE' with each letter in a random color."""
    dcode_text = "DCODE"
    colors = [f"\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m" for _ in dcode_text]
    return "".join(colors[i] + dcode_text[i] for i in range(len(dcode_text))) + "\033[0m"

def calculate_hash(algorithm, message):
    """Calculate the hash using the selected algorithm."""
    if algorithm == "MD5":
        return md5(message)
    elif algorithm == "SHA-1":
        return sha1(message)
    elif algorithm == "SHA-256":
        return sha256(message)
    else:
        raise ValueError("Unsupported algorithm!")

def main():
    """Main entry point for the DCODE tool."""
    while True:
        # Display DCODE logo with horizontal lines
        print("=" * 50)
        print(f"{colorful_dcode().center(50)}")
        print("=" * 50)

        print("Welcome to DCODE - Native Hashing Tool!\n")

        print("Select a hashing algorithm:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "4":
            print("Exiting DCODE. Goodbye!")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Please select a valid option.\n")
            continue

        algorithms = {"1": "MD5", "2": "SHA-1", "3": "SHA-256"}
        algorithm = algorithms[choice]

        message = input(f"Enter the message to hash using {algorithm}: ")
        print("Calculating...")
        time.sleep(1)  # Simulating processing time
        hash_value = calculate_hash(algorithm, message)
        print(f"The {algorithm} hash of your message is:\n{hash_value}\n")

if __name__ == "__main__":
    main()
