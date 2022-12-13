from PIL import Image
from pathlib import Path


def main():
    dir = Path.cwd()
    files = dir.glob('*.png')
    im_dict = dict()

    for i in files:
        cl_name = i.stem.replace('_', ' ').split()[0]
        if cl_name not in im_dict:
            im_dict[cl_name] = im_dict.get(cl_name, []) + [str(i)]
        else:
            im_dict[cl_name].append(str(i))

    for i in im_dict.keys():
        im_list = []
        for png in im_dict[i]:
            image = Image.open(png)
            im_list.append(image)

        im_list[0].save(f'results/{i}.gif', save_all=True, append_images=im_list[1:], optimize=False, 
                        duration=2000, loop=0)


if __name__ == "__main__":
    main()