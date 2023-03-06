{
    'name': 'Product Rating In POS',
    'version': '16.0.1.0.0',
    'sequence': '-8',
    'category': 'pos',
    'summary': 'Show Product Rating In POS',
    'description': 'Show Product Rating In POS',

    'installation': True,
    'application': True,

    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/product_rating.xml',
    ],
    'assets': {
       'point_of_sale.assets': [
           'pos_rating/static/src/xml/pos_screen.xml',
           'pos_rating/static/src/xml/pos_order_receipt.xml',
           'pos_rating/static/src/js/pos_receipt.js',

       ],
}
}