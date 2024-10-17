import os
import random

from flask import Flask, request, jsonify, render_template
from make_captcha.generate import validate, get_all_steps

app = Flask(__name__)


@app.route("/")
def index():
	random_seed = random.randint(0, 2 ** 32 - 1)
	return render_template("base.html",
						   seed=random_seed,
						   steps=get_all_steps(random_seed))


@app.route("/secret", methods=('POST',))
def secret():
	params = dict(request.form)
	seed = int(params["seed"])

	choices = [-1] * 4
	for key, val in params.items():
		if 'step_' in key:
			split_key = key.split('_')
			step_idx = int(split_key[1])
			choice_idx = int(split_key[2])

			choices[step_idx] = choice_idx

	score = validate(seed, choices)

	params_dict = dict(params)
	params_dict.update({ "score": score })

	return render_template("secret.html",
						   score=score)


if __name__ == '__main__':
	port = int(os.environ.get('FLASK_PORT', 5000))
	host = os.environ.get('FLASK_HOST', "0.0.0.0")

	app.run(debug=True, host=host, port=port)
