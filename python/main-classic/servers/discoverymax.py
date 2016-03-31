# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para discoverymax
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

from core import logger

import youtube_dl, urllib

# Some helper methods
def safe_unicode(value):
    """ Generic unicode handling method to parse the titles """
    from types import UnicodeType
    if type(value) is UnicodeType:
        return value
    else:
        try:
            return unicode(value, 'utf-8')
        except:
            return unicode(value, 'iso-8859-1')


def get_video_url( page_url , premium = False , user="" , password="", video_password="", page_data="" ):
    logger.info("[discoverymax.py] get_video_url(page_url='%s')" % page_url)

    ydl = youtube_dl.YoutubeDL({'outtmpl': u'%(id)s%(ext)s', 'no_color': True})
    result = ydl.extract_info(page_url, download=False)

    video_urls = []
    if 'formats' in result:
        for entry in result['formats']:
            video_urls.append([safe_unicode(entry['format']).encode('utf-8'), safe_unicode(entry['url']).encode('utf-8')])

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    return devuelve
