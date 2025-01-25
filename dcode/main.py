import time
import sys
import random
from hashing import md5, sha1, sha256

# ANSI escape codes for colors
def random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\033[38;2;{r};{g};{b}m"

def reset_color():
    """Reset color to default."""
    return "\033[0m"

def display_dcode_logo():
    """Display 'DCODE' with random RGB colors for each letter."""
    logo = "DCODE"
    for letter in logo:
        print(f"{random_color()}{letter}{reset_color()}", end="")
        sys.stdout.flush()
        time.sleep(0.2)  # Adds a delay for dramatic effect
    print("\n")

def spinner(message):
    """Display a spinner animation while processing."""
    chars = "|/-\\"
    sys.stdout.write(f"{message} ")
    sys.stdout.flush()
    for _ in range(10):
        for char in chars:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
    sys.stdout.write("Done!\n")

def menu():
    """Display the main menu for DCODE."""
    print("\n" + "=" * 30)
    display_dcode_logo()  # Show the DCODE logo
    print("=" * 30)
    print("Choose a hashing algorithm:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    print("4. Exit")
    print("=" * 30)

def main():
    """Main function to run DCODE."""
    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = input("Enter text to hash (MD5): ").strip()
            print("Calculating MD5 hash...")
            spinner("Processing")
            print(f"MD5 Hash: {md5(text)}")

        elif choice == "2":
            text = input("Enter text to hash (SHA-1): ").strip()
            print("Calculating SHA-1 hash...")
            spinner("Processing")
            print(f"SHA-1 Hash: {sha1(text)}")

        elif choice == "3":
            text = input("Enter text to hash (SHA-256): ").strip()
            print("Calculating SHA-256 hash...")
            spinner("Processing")
            print(f"SHA-256 Hash: {sha256(text)}")

        elif choice == "4":
            print("Thank you for using DCODE!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

