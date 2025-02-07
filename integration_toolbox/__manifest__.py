{
    "name": "Integration ToolBox",
    "version": "17.0.0.1.0",
    "category": "ToolBox",
    "sequence": 350,
    "summary": """The Integration ToolBox module integrates Odoo with
    various marketplaces and inventory 3PL services.It includes data
    synchronization, security settings, and views for managing
    bindings and orders.""",
    "author": "MoonSun PTY LTD",
    "company": "MoonSun",
    "website": "https://github.com/MoonsunSoft/connector",
    "depends": [
        "connector_base",
        "connector_bigw",
        "connector_crossdocks",
        "connector_harvey_norman",
        "connector_marketplacer",
        "connector_mirakl",
        "connector_sps",
    ],
    "data": [],
    "license": "OPL-1",
    "application": True,
}
