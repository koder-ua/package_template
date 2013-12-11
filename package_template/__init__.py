from paste.script import templates


class PackageTemplate(templates.Template):

    egg_plugins = ['package_template']
    summary = 'Template for creating a basic package'
    required_templates = ['basic_package']
    _template_dir = 'templates'
    use_cheetah = True
