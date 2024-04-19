#!/usr/bin/env python3
from get_image_script.parse_args import parse
from get_image_script.get_img_links import get_img_links
from get_image_script.download_images import download_images


def main():
    path_to_page, path_to_results = parse()
    img_links = get_img_links(path_to_page)
    download_images(img_links, path_to_results)


if __name__ == '__main__':
    main()
