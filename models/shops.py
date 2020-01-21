from . import db

inventory = db.Table('inventory',
                     db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id'), primary_key=True),
                     db.Column('shop_id', db.Integer, db.ForeignKey('shop.id'), primary_key=True)
                     )


class Shop(db.Model):

    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    published = db.Column(db.Boolean, unique=False, default=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    comment = db.Column(db.String(200), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    inventory = db.relationship('Inventory', secondary=inventory, lazy='subquery',
                                backref=db.backref('inventory', lazy=True))

    def __repr__(self):
        return '<Shop %r>' % self.name


class ShopInventory(db.Model):

    __tablename__ = 'shop_inventory'
    id = db.Column(db.Integer, primary_key=True)
