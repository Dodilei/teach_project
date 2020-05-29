import sys
import os

if __name__ == "__main__":
    args = sys.argv[1:]
    cwd = os.getcwd().replace(" ", "\\ ")
    if ".py" in args[0]:
        args[0] = os.path.join(cwd, args[0])
    if not "--hold-default-dir" in args:
        args = args + [
            "--media_dir", os.path.join(cwd, "media"),
            "--video_dir", os.path.join(cwd, "video"),
        ]
    else:
        args.remove("--hold-default-dir")

    os.system("cd ~/Documents/GitHub/cloned_repos/manim ;python -m manim " + " ".join(args))
