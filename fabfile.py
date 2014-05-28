from fabric.api import local, settings


def screenshot():
    local("casperjs ./js/screenshots.js http://google.com")
