# BEGIN
MAPPING = {
    'a': 'href',
    'img': 'src',
    'link': 'href',
}


def get_links(tags):
    result = []
    for tag in tags:
        name = tag['name']
        if name in MAPPING:
            attr = MAPPING[tag['name']]
            result.append(tag[attr])
    return result
# END
