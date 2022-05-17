
import math
def find_substring(str, pattern):
	unique_pattern_chars = set(pattern)
	frequency_dict = {}
	window_start, min_length, dict_keys, m = 0, math.inf, 0, 0

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in unique_pattern_chars:
			if right_char not in frequency_dict:
				frequency_dict[right_char] = 0
				dict_keys += 1

			frequency_dict[right_char]  += 1
		
		while dict_keys == len(unique_pattern_chars):
			min_length = min(min_length, window_end - window_start + 1)

			left_char = str[window_start]
			if left_char in unique_pattern_chars:
				frequency_dict[left_char] -= 1
				if frequency_dict[left_char] == 0:
					dict_keys -= 1
			# else:
			window_start += 1

	if min_length != math.inf:
		m = window_end - window_start + 1
		return m
	else:
		return 0


def main():
	print(find_substring("aabdec", "abc"))
	print(find_substring("abdabca", "abc"))
	print(find_substring("adcad", "abc"))

main()