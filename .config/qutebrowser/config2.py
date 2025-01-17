# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Directory to save downloads to. If unset, a sensible OS-specific
c.downloads.location.directory = '$HOME/Downloads'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
c.url.default_page = 'about:blank'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'http://scholar.google.ch/scholar?hl=en&q={}'}

# Page(s) to open at the start.
c.url.start_pages = 'https://scholar.google.com'

# Privacy-harden everything

## Disable cookies
config.set("content.cookies.accept", "no-3rdparty")
config.set("content.cookies.store", False)

## Disable HTML5 cache
config.set("content.cache.appcache", False)

## Disable HTML Storage and Web SQL cache
config.set("content.local_storage", False)

## Enable private browsing
config.set("content.private_browsing", True)

# Bindings for normal mode
# I like to bind semicolon to search to make it easier to reach:
config.bind(';', 'set-cmd-text /')
config.bind('/', 'set-cmd-text ?')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('X', 'hint links yank')
