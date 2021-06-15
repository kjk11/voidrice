# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Directory to save downloads to. If unset, a sensible OS-specific
c.downloads.location.directory = '$HOME/Downloads'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
c.url.default_page = 'https://searx.info/'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://searx.info/?q={}'}

# Page(s) to open at the start.
c.url.start_pages = 'https://searx.info'

# Set dark mode
config.set("colors.webpage.darkmode.enabled", True)

# Bindings for normal mode
# I like to bind semicolon to search to make it easier to reach:
config.bind(';', 'set-cmd-text /')
config.bind('/', 'set-cmd-text ?')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
