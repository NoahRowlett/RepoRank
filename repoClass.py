class Repo:

	def __init__(self, name="", stars=0, contributors=0, watchers=0, issues=0, url=""):
		self.name = name.rstrip()
		self.stars = stars
		self.contributors = contributors
		self.watchers = watchers
		self.issues = issues
		self.url = url.rstrip()

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

	def set_name(self, name):
		self.name = name.rstrip()

	def set_stars(self, stars):
		self.stars = stars

	def set_contributors(self, contributors):
		self.contributors = contributors

	def set_watchers(self, watchers):
		self.watchers =  wat

	def set_issues(self, issues):
		self.issues =  issues

	def set_url(self, url):
		self.url = url.rstrip()


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