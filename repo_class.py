class Repo:
	# constructor:
	def __init__(self, name):
		self.stars = name.rstrip()
		self.contributors = 0
		self.watchers = 0
		self.issues = 0
		self.url = ""

	def get_name(self):
		return self.name

	def get_contributors(self):
		return self.contributors

	def get_watchers(self):
		return self.watchers

	def get_issues(self):
		return self.issues

	def get_url(self):
		return self.url

	def add_info(self, s, c, w, i, u):
		if((s is not None) and  (c is not None) and  (w is not None) and  (i is not None) and  (u is not None)):
			self.stars = int(s)
			self.contributors = int(c)
			self.watchers = int(w)
			self.issues = int(i)
			self.url = string(u)
			return True
		else:
			return False

	def format_output(self):
		output = self.name
		output += ":\n\tstars: "
		output += self.get_stars()
		output += "\n\tcontributors: "
		output += self.get_contributors()
		output += "\n\watchers: "
		output += self.get_watchers()
		output += "\n\turl: "
		output += self.get_url()
		return output

name = raw_input("Enter repo info in the format (name, stars, contributors, watchers, url: ")