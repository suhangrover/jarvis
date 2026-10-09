import platform
def main():
    print("="*40)
    print("             Jarvis-PY")
    print("="*40)
    print()
    print(f"Operating System:",{platform.system()})
    print(f"OS Version:",platform.release())
    print(f"Architecture:",{platform.machine()})
    print(f"Python Version:",{platform.python_version()})
    return
main()