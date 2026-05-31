{
    'name': 'Auto Out-of-Stock Ribbon for eCommerce',
    'version': '17.0.1.0.0',
    'summary': 'Automatic out-of-stock badge on product images when qty = 0',
    'description': """
        <h2>Auto Out-of-Stock Ribbon for eCommerce</h2>
        <p>Automatically displays a red badge <strong>"Out of Stock"</strong>
        on product images in the eCommerce shop when stock quantity is zero or below.</p>
        <h3>Features</h3>
        <ul>
            <li>Automatic badge — no manual action needed</li>
            <li>Works on all storable products</li>
            <li>Compatible with Odoo 17 Community</li>
            <li>Lightweight — one XML template only</li>
        </ul>
        <h3>How it works</h3>
        <p>When <strong>qty_available &lt;= 0</strong>, a red ribbon appears
        automatically on the product image in the shop grid.</p>
    """,
    'category': 'Website/Website',
    'author': 'Akremjs',
    'website': 'https://github.com/Akremjs/Auto-Out-of-Stock-Ribbon-for-eCommerce',
    'license': 'LGPL-3',
    'depends': ['website_sale'],
    'data': ['views/badge.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'EUR',
}
