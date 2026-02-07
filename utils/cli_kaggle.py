import subprocess

def get_kagglke_data(kaggle_path: str, local_path: str):
    """
    As kagglehub doesn't work correctly let us get data through CLI
    
    Args:
        kaggle_path: path from kaggle which can be got from URL or kaggle download button
        local_path: destination path on your local machine 
    """
    return subprocess.run(f'kaggle datasets download {kaggle_path} -p {local_path} --unzip', shell=True)