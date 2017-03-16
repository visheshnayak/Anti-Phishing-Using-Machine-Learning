from features import domainCheck, urlChar, urlDot, urlSens, urlCharHash, urlLength, urlHttps

def featureAdd(url):
    secur = url.count("secur")
    login = url.count("login")
    signin = url.count("signin")
    webscr = url.count("webscr")
    ebayisapi = url.count("ebayisapi")
    banking = url.count("banking")
    confirm = url.count("confirm")

    reslist = [domainCheck(url), urlChar(url), urlDot(url), urlCharHash(url), urlLength(url), urlHttps(url)]
    return reslist
