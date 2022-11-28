
# twitter url
TWITTER_ADVANCED_URL = "https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&q={}&tweet_search_mode=live&count=20&query_source=typed_query&cursor={}&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2CvoiceInfo"
TWEET_URL = "https://twitter.com/i/api/graphql/4tzuTRu5-fpJTS7bDF6Nlg/TweetDetail?variables={}"
TWITTER_TOKEN_URL = "https://api.twitter.com/1.1/guest/activate.json"

# twitter header
TWITTER_DEFAULT_HEADER = {
    'authority': 'twitter.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'x-twitter-client-language': 'zh-cn',
    'x-csrf-token': '5be5776dc30ae96f4ac87b32afe12095',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'x-guest-token': '',
    'x-twitter-active-user': 'yes',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://twitter.com/search?q=%22Belt and Road%22%20(from%3Achinadaily)%20until%3A2021-09-30%20since%3A2019-01-01&src=typed_query&f=live',
    'accept-language': 'zh-CN,zh;q=0.9'
}

# twitter param
TWEET_PARAM = {
    "focalTweetId": "",
    # "cursor": "CgAAAKAcGQYlBBEVDgAA",
    "referrer": "tweet",
    "with_rux_injections": False,
    "includePromotedContent": True,
    "withCommunity": True,
    "withTweetQuoteCount": True,
    "withBirdwatchNotes": False,
    "withSuperFollowsUserFields": False,
    "withUserResults": True,
    "withBirdwatchPivots": False,
    "withReactionsMetadata": False,
    "withReactionsPerspective": False,
    "withSuperFollowsTweetFields": False,
    "withVoice": True
}