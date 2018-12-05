import re
import html
import urllib.request as req
from urllib.error import HTTPError
from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'token.txt',
    api_base_url = 'https://botsin.space/'
)

title_regex = re.compile('(<a data-click-id="body" class="SQnoC3ObvgnGjWt90zD9Z" href=")(\/r\/Showerthoughts\/comments\/[a-z0-9]+\/[a-z0-9-_]+\/)("><h2 class="imors3-0 iuScIP">)([^<]*)(<\/h2><\/a>)')

while True:
    try:
        fp = req.urlopen("https://www.reddit.com/r/Showerthoughts/top/?sort=top&t=hour")
        page = html.unescape(fp.read().decode("utf8"))
        fp.close()
        url, title = title_regex.search(page).group(2, 4)
        mastodon.toot(title + " #ShowerThoughts")
        break
    except HTTPError:
        pass
