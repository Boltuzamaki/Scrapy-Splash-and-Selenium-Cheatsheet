function main(splash, args)
    splash.private_mode_enabled = false
    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))
    splash:set_viewport_full()
    return splash:png()
end

