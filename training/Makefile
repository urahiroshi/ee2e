create_model:
	./training.py

# to install tensorflowjs[wizard] for M1 Mac, it calls customized command:
# https://stackoverflow.com/questions/51046150/how-to-ignore-the-dependencies-of-a-specific-package-when-installing-it-with-pip
install:
	pipenv run install

tfjs_wizard:
	pipenv run tensorflowjs_wizard

convert:
	pipenv run tensorflowjs_converter \
		--input_format=keras_saved_model \
		./saved_model/ \
		./output/
