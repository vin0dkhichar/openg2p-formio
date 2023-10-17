# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenG2P Formio",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "summary": "Form builders allow you to create, manage, and use dynamic forms with ease.",
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["formio","g2p_programs","formio_storage_filestore"],
    "data": [
        "views/formio_builder.xml",
        "views/program_view.xml",
    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
        "web.assets_frontend":[],
        "web.assets_common":[],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
