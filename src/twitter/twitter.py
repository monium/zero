import argparse

class Twitter:

	def __init__(self, path):
		try:
			with open(path, 'r') as f:
				credentials = []
				for line in f.readlines():
					print(line)

		except FileNotFoundError:
			print(f'{path} does not exist')

	def get_followers(self, user):
		return ["001","9990","666"]

	def get_following(self, user):
		pass

	def get_num_tweets(self, start_date, end_date):
		pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', type = str, required = True)
	args = parser.parse_args()
	test = Twitter(args.f)
