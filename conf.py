from recommonmark.transform import AutoStructify

project = 'Frontend Developer Handbook'
copyright = 'ZEIT ONLINE'

extensions = ['recommonmark']

master_doc = 'toc'

html_theme = "sphinx_zon_theme"
html_theme_options = {
    'elasticsearch_host': None,
    'elasticsearch_index': 'docs',
    'editme_link': (
        'https://github.com/ZeitOnline/frontend-developer-handbook/edit/master/{page}')
}
html_last_updated_fmt = '%b %d, %Y'


# app setup hook, needed for recommonmark
def setup(app):
    app.add_config_value('recommonmark_config', {
        'enable_auto_toc_tree': True,
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
