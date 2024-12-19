import os
import subprocess
import sys

language_aliases: dict[str, str] = {
    "c++": "cpp",
    "py": "python",
    "rs": "rust",
}

def get_run_commands(language: str, language_dir: str, day: str) -> list[list[str]]:
    if language == "cpp":
        # Thankfully due to Python magic this works on both Windows and UNIX
        commands: list[list[str]] = [[os.path.join(language_dir, "main"), day]]
        if not os.path.isfile(os.path.join(language_dir, "main")) and not os.path.isfile(os.path.join(language_dir, "main.exe")):
            # Compile the source code first
            commands.insert(0, ["g++", "*.cpp", "-o", "main"])
        return commands
    elif language == "python":
        return [["python", day + ".py"]]
    elif language == "rust":
        return [["cargo", "run", "--", day]]
    elif language == "zig":
        return [["zig", "run", "src/main.zig", "--", day]]
    else:
        raise ValueError("unsupported language " + language)

def main(base_dir: str, year: str, language: str, day: str = "") -> None:
    if language in language_aliases:
        language = language_aliases[language]
    if not day:
        day = "all"
    elif day.isdigit() and len(day) <= 2:
        day = "day" + day.zfill(2)
    language_dir: str = os.path.join(base_dir, year, language)
    if not os.path.isdir(language_dir):
        raise NotADirectoryError(language + " is not supported in year " + year)
    run_commands: list[list[str]] = get_run_commands(language, language_dir, day)
    for command in run_commands:
        subprocess.run(command, cwd=language_dir)

if __name__ == "__main__":
    main(os.path.dirname(__file__), *sys.argv[1:])
