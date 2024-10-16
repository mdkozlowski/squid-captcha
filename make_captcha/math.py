import numpy as np
import scipy.stats as stats
import pandas as pd

N_ITEMS = 7
N_GROUPS = 4
DIRICHLET_ALPHA = 5.0
N_STEPS = 4


def base_generate(base_seed: int, seed_offset=0):
	_random_state = np.random.default_rng(seed=base_seed + seed_offset)

	probs = _random_state.dirichlet(alpha=[DIRICHLET_ALPHA] * N_GROUPS).tolist()
	entropy = [
		stats.bernoulli.entropy(p=prob) for idx, prob in enumerate(probs)
	]
	correct_index = np.argmax(entropy)

	rvs = [
		stats.bernoulli.rvs(p=prob, size=N_ITEMS, random_state=_random_state).tolist()
		for idx, prob in enumerate(probs)
	]
	return correct_index, entropy, rvs


def validate(input_seed: int, user_inputs: list[int]):
	solutions = [
		base_generate(base_seed=input_seed,
					  seed_offset=offset)[0] for offset in range(N_STEPS)
	]
	input_is_correct_list = [
		int(user_inputs[idx]) == int(k) for idx, k in enumerate(solutions)
	]

	return sum(input_is_correct_list)


def get_step(input_seed: int, offset: int):
	_, _, rvs = base_generate(base_seed=input_seed, seed_offset=offset)
	return rvs


def get_all_steps(seed: int):
	seq = [
		base_generate(seed, seed_offset=idx) for idx in range(N_STEPS)
	]

	all_steps = [
		rvs
		# dict(
		# correct_index=correct_index,
		# entropy=entropy,
		# rvs=rvs
		for correct_index, entropy, rvs in seq
	]
	return all_steps
