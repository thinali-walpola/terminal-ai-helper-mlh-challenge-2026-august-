import subprocess


def translate_request(request):
    """
    Convert simple English requests into Windows terminal commands.
    """

    request = request.lower().strip()

    commands = {

        "show files": "dir",

        "show files in this folder": "dir",

        "list files": "dir",

        "show current directory": "cd",

        "where am i": "cd",

        "show running processes": "tasklist",

        "show processes": "tasklist",

        "show network information": "ipconfig",

        "show ip address": "ipconfig",

        "check python version": "python --version",

        "check java version": "java --version",

        "check node version": "node --version",

        "show environment variables": "set",

    }


    # Check exact matches first

    if request in commands:
        return commands[request]


    # Handle Java file search

    if "find all java files" in request:
        return 'dir /s /b *.java'


    # Handle Python file search

    if "find all python files" in request:
        return 'dir /s /b *.py'


    # Handle files larger than 100MB

    if "files larger than 100mb" in request:
        return 'powershell -Command "Get-ChildItem -Recurse -File | Where-Object {$_.Length -gt 100MB} | Select-Object FullName,Length"'


    # Handle files larger than 1GB

    if "files larger than 1gb" in request:
        return 'powershell -Command "Get-ChildItem -Recurse -File | Where-Object {$_.Length -gt 1GB} | Select-Object FullName,Length"'


    return None


def ask_for_confirmation(command):

    print()
    print("=" * 60)
    print("⚠️  HUMAN APPROVAL REQUIRED")
    print("=" * 60)

    print()
    print("The agent wants to execute:")
    print()

    print(f"    {command}")

    print()

    answer = input(
        "Do you want to run this command? (y/n): "
    ).lower().strip()


    if answer == "y" or answer == "yes":
        return True

    return False


def execute_command(command):

    print()
    print("🚀 Executing command...")
    print()

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )


        if result.stdout:
            print(result.stdout)


        if result.stderr:
            print(result.stderr)


        print()
        print(f"Exit code: {result.returncode}")


    except Exception as error:

        print()
        print("❌ Error while executing command:")
        print(error)


def main():

    print("=" * 60)
    print("🤖 TERMINAL AI HELPER")
    print("=" * 60)

    print()
    print("Describe what you want to do in plain English.")
    print()
    print("Examples:")
    print("  • Show files")
    print("  • Find all Java files")
    print("  • Find files larger than 100MB")
    print("  • Show running processes")
    print("  • Check Python version")
    print()
    print("Type 'exit' to quit.")
    print()


    while True:

        request = input("You: ").strip()


        if request.lower() == "exit":
            print()
            print("Goodbye! 👋")
            break


        if not request:
            print("Please enter a request.")
            continue


        command = translate_request(request)


        if command is None:

            print()
            print("❓ I don't know how to translate that request yet.")
            print("Try one of the example commands.")
            print()

            continue


        print()
        print("🤖 Agent generated:")
        print()
        print(f"    {command}")


        approved = ask_for_confirmation(command)


        if approved:

            execute_command(command)

        else:

            print()
            print("🛑 Command cancelled.")
            print("The agent did NOT execute the command.")

        print()


if __name__ == "__main__":
    main()
