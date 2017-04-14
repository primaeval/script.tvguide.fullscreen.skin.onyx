import xbmc,xbmcgui,xbmcaddon

d = xbmcgui.Dialog()
ok = d.ok("TV Guide Fullscreen","Set this Skin as default?")
if ok:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.deco/')
        tvgf.setSetting('skin.user', 'Deco')
        tvgf.setSetting('epg.focus.color', '[COLOR ffd3d3d3]lightgray[/COLOR]')
        tvgf.setSetting('epg.nofocus.color', '[COLOR ffffffff]white[/COLOR]')
        tvgf.setSetting('timebar.color', '[COLOR ff008000]green[/COLOR]')
        tvgf.setSetting('epg.video.pip', 'true')