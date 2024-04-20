lint:
	poetry run flake8 get_image_script

install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl
