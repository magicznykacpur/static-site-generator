import os
import shutil


def copy_static_content_recursive(from_path, to_path):
    if not os.path.exists(from_path):
        print(f"Cannot copy from {from_path}, directory doesn't exist...")
        return
    if not os.path.exists(to_path):
        print(f"Cannot copy to {to_path}, directory doesn't exist...")
        return

    to_dir_list = os.listdir(to_path)
    for item in to_dir_list:
        to_remove_path = f"{to_path}/{item}"
        if os.path.isfile(to_remove_path):
            os.remove(to_remove_path)
        else:
            shutil.rmtree(to_remove_path)

    dir_list = os.listdir(from_path)
    for item in dir_list:
        src_path = os.path.join(from_path, item)
        target_path = os.path.join(to_path, item)

        if os.path.isfile(src_path):
            print(f"copying from {src_path} to {target_path}")

            shutil.copy(src_path, os.path.join(to_path))
        else:
            print(f"creating {target_path}")

            os.mkdir(target_path)
            copy_static_content_recursive(src_path, target_path)


def main():
    copy_static_content_recursive("static", "public")


if __name__ == "__main__":
    main()
