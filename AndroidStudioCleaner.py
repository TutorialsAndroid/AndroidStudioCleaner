import os
import re
import shutil
from pathlib import Path

APPDATA = os.getenv("APPDATA")
LOCALAPPDATA = os.getenv("LOCALAPPDATA")

GRADLE_DIR = Path.home() / ".gradle"

GRADLE_FOLDERS = [
    "caches",
    "daemon",
    "wrapper",
    ".tmp",
    "workers",
    "notifications"
]


def format_size(size_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_folder_size(folder):
    total = 0

    try:
        for root, dirs, files in os.walk(folder):
            for file in files:
                try:
                    filepath = os.path.join(root, file)

                    if not os.path.islink(filepath):
                        total += os.path.getsize(filepath)

                except Exception:
                    pass

    except Exception:
        pass

    return total


def delete_folder(folder_path):
    if not os.path.exists(folder_path):
        return False, 0, "NOT_FOUND"

    try:
        size = get_folder_size(folder_path)
        shutil.rmtree(folder_path)
        return True, size, None

    except Exception as e:
        return False, 0, str(e)


def cleanup_gradle():
    print("\n========== GRADLE CLEANUP ==========\n")

    recovered = 0

    if not GRADLE_DIR.exists():
        print("Gradle directory not found.")
        return recovered

    for folder in GRADLE_FOLDERS:
        target = GRADLE_DIR / folder

        success, size, error = delete_folder(target)

        if success:
            recovered += size
            print(
                f"[DELETED] {folder:<15} "
                f"{format_size(size)}"
            )

        elif error == "NOT_FOUND":
            print(
                f"[SKIPPED] {folder:<15} "
                f"Not found"
            )

        else:
            print(
                f"[FAILED ] {folder:<15} "
                f"{error}"
            )

    return recovered


def parse_version(folder_name):
    match = re.search(r'AndroidStudio(.+)', folder_name)

    if not match:
        return ()

    version_string = match.group(1)

    numbers = re.findall(r'\d+', version_string)

    return tuple(int(x) for x in numbers)


def cleanup_android_studio_versions(base_path):
    recovered = 0

    if not os.path.exists(base_path):
        return recovered

    folders = []

    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)

        if (
            os.path.isdir(full_path)
            and item.startswith("AndroidStudio")
        ):
            folders.append(item)

    if not folders:
        return recovered

    if len(folders) == 1:
        print(
            f"[KEEPING] Only one Android Studio version found: "
            f"{folders[0]}"
        )
        return recovered

    folders.sort(key=parse_version)

    latest = folders[-1]

    print(f"\nLatest Version: {latest}")

    for folder in folders[:-1]:
        target = os.path.join(base_path, folder)

        success, size, error = delete_folder(target)

        if success:
            recovered += size
            print(
                f"[DELETED] {folder:<30} "
                f"{format_size(size)}"
            )

        elif error == "NOT_FOUND":
            print(
                f"[SKIPPED] {folder:<30} "
                f"Not found"
            )

        else:
            print(
                f"[FAILED ] {folder:<30} "
                f"{error}"
            )

    print(f"[KEPT   ] {latest}")

    return recovered


def cleanup_android_studio():
    print("\n========== ANDROID STUDIO CLEANUP ==========\n")

    recovered = 0

    roaming_google = os.path.join(APPDATA, "Google")
    local_google = os.path.join(LOCALAPPDATA, "Google")

    print("Scanning Roaming Google Directory...")
    recovered += cleanup_android_studio_versions(roaming_google)

    print("\nScanning Local Google Directory...")
    recovered += cleanup_android_studio_versions(local_google)

    return recovered

def scan_gradle_targets():
    targets = []

    if not GRADLE_DIR.exists():
        return targets

    for folder in GRADLE_FOLDERS:
        path = GRADLE_DIR / folder

        if path.exists():
            targets.append(str(path))

    return targets


def scan_android_studio_targets():
    delete_targets = []
    keep_targets = []

    google_paths = [
        os.path.join(APPDATA, "Google"),
        os.path.join(LOCALAPPDATA, "Google")
    ]

    for base_path in google_paths:

        if not os.path.exists(base_path):
            continue

        folders = []

        for item in os.listdir(base_path):
            full_path = os.path.join(base_path, item)

            if (
                os.path.isdir(full_path)
                and item.startswith("AndroidStudio")
            ):
                folders.append(item)

        if not folders:
            continue

        folders.sort(key=parse_version)

        if len(folders) == 1:
            keep_targets.append(folders[0])
            continue

        latest = folders[-1]

        keep_targets.append(latest)

        for folder in folders[:-1]:
            delete_targets.append(folder)

    return delete_targets, keep_targets


def show_preview(mode):
    print("\n" + "=" * 60)
    print("CLEANUP PREVIEW")
    print("=" * 60)

    if mode in ("1", "2"):
        gradle_targets = scan_gradle_targets()

        print("\nGradle folders to delete:\n")

        if gradle_targets:
            for target in gradle_targets:
                print(f"✓ {target}")
        else:
            print("No Gradle cleanup required.")

    if mode in ("1", "3"):
        delete_versions, keep_versions = scan_android_studio_targets()

        print("\nOld Android Studio versions to delete:\n")

        if delete_versions:
            for version in delete_versions:
                print(f"✗ {version}")
        else:
            print("No old Android Studio versions found.")

        print("\nAndroid Studio versions to keep:\n")

        if keep_versions:
            for version in keep_versions:
                print(f"✓ {version}")
        else:
            print("No Android Studio configuration found.")

    print("\n" + "=" * 60)

    choice = input(
        "Continue with cleanup? (Y/N): "
    ).strip().upper()

    return choice == "Y"

def select_cleanup_mode():
    print("\n" + "=" * 70)
    print("SELECT CLEANUP MODE")
    print("=" * 70)

    print("\n[1] Full Cleanup")
    print("    • Gradle caches")
    print("    • Old Android Studio versions")

    print("\n[2] Gradle Cleanup Only")
    print("    • caches")
    print("    • daemon")
    print("    • wrapper")
    print("    • .tmp")
    print("    • workers")
    print("    • notifications")

    print("\n[3] Android Studio Cleanup Only")
    print("    • Old Android Studio versions")
    print("    • Keep latest version")

    print("\n" + "=" * 70)

    while True:
        choice = input(
            "\nSelect an option (1-3): "
        ).strip()

        if choice in ("1", "2", "3"):
            return choice

        print("Invalid selection.")

def show_startup_warning():
    print("\n")
    print("=" * 70)
    print(" █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ ")
    print("██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗")
    print("███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║")
    print("██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║")
    print("██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝")
    print("╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ")
    print("=" * 70)

    print("\n⚠ IMPORTANT")
    print("\nBefore continuing, please close:")

    print("\n  • Android Studio")
    print("  • VS Code")
    print("  • IntelliJ IDEA")
    print("  • Any running Gradle builds")
    print("  • Any terminal using your Android project")

    print("\nKeeping these applications open may prevent")
    print("some files from being deleted successfully.")

    print("\n" + "=" * 70)

    choice = input(
        "\nHave you closed all development tools? (Y/N): "
    ).strip().upper()

    return choice == "Y"


def main():

    if not show_startup_warning():
        print("\nOperation cancelled.")
        input("\nPress Enter to exit...")
        return

    mode = select_cleanup_mode()

    print("=" * 60)
    print("AndroidStudioCleaner")
    print("=" * 60)

    if not show_preview(mode):
        print("\nCleanup cancelled.")
        input("\nPress Enter to exit...")
        return

    total_recovered = 0

    if mode == "1":
        total_recovered += cleanup_gradle()
        total_recovered += cleanup_android_studio()

    elif mode == "2":
        total_recovered += cleanup_gradle()

    elif mode == "3":
        total_recovered += cleanup_android_studio()

    print("\n" + "=" * 60)
    print("CLEANUP COMPLETED")
    print("=" * 60)

    print(
        f"Total Space Recovered: "
        f"{format_size(total_recovered)}"
    )

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()