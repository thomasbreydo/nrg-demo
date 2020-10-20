import subprocess
import os
import joblib
import sklearn


GISTPATH = "https://gist.github.com/thomasbreydo/a5a47758c6dc382b5e8f264da856b2bc/raw/b6767e9764f1b6291ccef771b6df85ca7c04e1d6/model.joblib"
SAVEPATH = "model.joblib"


def download_gist_to_path(gistpath, savepath, force_redownload=False):
    if force_redownload or not os.path.exists(savepath):
        subprocess.run(("curl", "-L", gistpath, "-o", savepath))


def load_model_from_path(savepath):
    return joblib.load(savepath)


def load_model():
    return load_model_from_path(SAVEPATH)


if __name__ == "__main__":
    download_gist_to_path(GISTPATH, SAVEPATH, force_redownload=True)