RepoRank
	Matt Bullock
	Noah Rowlett
	
========================================================================================

GitHub has an extensive database of public repositories. Wouldn't it be interesting to find out which are the most active and gain insights into which are the highest quality?

Our ranking algorithm will be based on the number of Stars, Contributors, Watchers, and Issues for a repo.

========================================================================================



#watchers = watchers_count
#issues = open_issues_count
#stars = count(http://developer.github.com/v3/activity/starring/)
#contributors = count(http://developer.github.com/v3/repos/#list-contributors) 
	Optional flag. Set to 1 or true to include anonymous contributors in results.