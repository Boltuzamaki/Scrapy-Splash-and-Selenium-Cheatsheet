function main(splash, args)
    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))
    return{
        image = splash:png(),
        html = splash:html()
    }
end