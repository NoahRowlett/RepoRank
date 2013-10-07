class Repo:
	# constructor:
	def __init__(self, name):
		self.name = name.rstrip()
		self.stars = 0
		self.contributors = 0
		self.watchers = 0
		self.issues = 0
		self.url = ""

	def get_name(self):
		return self.name

	def get_stars(self):
		return self.stars

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
			self.url = str(u)
			return True
		else:
			return False

	def format_output(self):
		output = self.get_name()
		output += ":\n\tstars: "
		output += str(self.get_stars())
		output += "\n\tcontributors: "
		output += str(self.get_contributors())
		output += "\n\twatchers: "
		output += str(self.get_watchers())
		output += "\n\tissues: "
		output += str(self.get_issues())
		output += "\n\turl: "
		output += str(self.get_url())
		return output

# name = raw_input("Enter repo name: ")
# stars = raw_input("Enter number of stars: ")
# contributors = raw_input("Enter number of contributors: ")
# watchers = raw_input("Enter number of watchers: ")
# issues = raw_input("Enter number of issues: ")
# url = raw_input("Enter number of url: ")
# repo = Repo(name)
# repo.add_info(stars, contributors, watchers, issues, url)
# print repo.format_output()