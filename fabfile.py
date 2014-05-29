from fabric.api import local, settings


def screenshot(url):
    """ generate screenshot for given url """
    local("casperjs ./js/screenshots.js %s" % url)
