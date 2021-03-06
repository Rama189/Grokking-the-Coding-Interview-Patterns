#mycode, completely failed to write! Ouch

def length_of_longest_substring(str, k):
		window_start, max_length = 0, 0
		max_repeat_letter_count = 0
		repeating_char_dict = {}

		for window_end in range(len(str)):
				right_char = str[window_end]

				if right_char not in repeating_char_dict:
						repeating_char_dict[right_char] = 0

				repeating_char_dict[right_char] += 1
				max_repeat_letter_count = max(max_repeat_letter_count, repeating_char_dict[right_char])

				if (window_end - window_start + 1 - max_repeat_letter_count) > k:
						left_char = str[window_start]
						repeating_char_dict[left_char] -= 1
						window_start += 1
				
				max_length = max(max_length, window_end - window_start + 1)
		return max_length

#answer
def length_of_longest_substring(str, k):
	window_start, max_length, max_repeat_letter_count = 0, 0, 0
	frequency_map = {}

	# Try to extend the range [window_start, window_end]
	for window_end in range(len(str)):
		right_char = str[window_end]
		if right_char not in frequency_map:
			frequency_map[right_char] = 0
		frequency_map[right_char] += 1
		max_repeat_letter_count = max(
			max_repeat_letter_count, frequency_map[right_char])

		# Current window size is from window_start to window_end, overall we have a letter which is
		# repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
		# repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
		# if the remaining letters are more than 'k', it is the time to shrink the window as we
		# are not allowed to replace more than 'k' letters
		if (window_end - window_start + 1 - max_repeat_letter_count) > k:
			left_char = str[window_start]
			frequency_map[left_char] -= 1
			window_start += 1

		max_length = max(max_length, window_end - window_start + 1)
	return max_length


def main():
		print(length_of_longest_substring("aabccbb", 2))
		print(length_of_longest_substring("abbcb", 1))
		print(length_of_longest_substring("abccde", 1))

main()