# BEGIN
excluded_attrs = ['name', 'tag_type', 'body']


def build_attrs(tag):
    acc = []
    for attr in tag:
        if attr not in excluded_attrs:
            acc.append(f' {attr}="{tag[attr]}"')
    return ''.join(acc)


mapping = {
    'single': lambda tag: f"<{tag['name']}{build_attrs(tag)}>",
    'pair': lambda tag: f"<{tag['name']}{build_attrs(tag)}>{tag['body']}</{tag['name']}>",  # noqa: E501
}


def stringify(tag):
    build = mapping[tag['tag_type']]
    return build(tag)
# END
