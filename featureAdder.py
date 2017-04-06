from features import *

def featureAdd(url):
    secur = url.count("secur")
    login = url.count("login")
    signin = url.count("signin")
    webscr = url.count("webscr")
    ebayisapi = url.count("ebayisapi")
    banking = url.count("bank")
    confirm = url.count("confirm")
    ultimate = secur + login + signin + webscr + ebayisapi + banking + confirm

    reslist = [domainCheck(url), urlChar(url), urlDot(url), urlCharHash(url), urlLength(url), urlHttps(url), ultimate, ipcheck(url), chardash(url)]
    return reslist
