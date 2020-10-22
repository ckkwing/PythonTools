import os
from common import utility
from common.file_helper import FileHelper
import shutil


class FolderCleaner:
    @staticmethod
    def delete_files_by_suffix(folder_path, suffix_list):
        if not os.path.exists(folder_path):
            return
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                if FileHelper.is_suffix(file_path, *suffix_list):
                    os.remove(file_path)
                    print("###########" + os.path.join(root, name) + " removed######")

    @staticmethod
    def delete_files_except_suffix(folder_path, suffix_list):
        if not os.path.exists(folder_path):
            return
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                if not FileHelper.is_suffix(file_path, *suffix_list):
                    os.remove(file_path)
                    print("###########" + os.path.join(root, name) + " removed######")

    @staticmethod
    def clean_folder(folder_path, delete_self=True):
        if not os.path.exists(folder_path):
            return
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
                print("###########" + os.path.join(root, name) + " removed######")
            for name in dirs:
                print(os.path.join(root, name))
                shutil.rmtree(os.path.join(root, name))
        if delete_self:
            shutil.rmtree(folder_path)

