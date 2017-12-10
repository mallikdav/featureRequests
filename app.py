# -*- coding: utf-8 -*-

from flask import Flask
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

# Create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True


# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/feature_request_db.db'
db = SQLAlchemy(app)


# Create data storage
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)


class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('Client', backref=db.backref('feature_request'))
    client_priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
    client_priority = db.relationship('Priority', backref=db.backref('feature_request'))
    target_date = db.Column(db.Date)
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'))
    product_area = db.relationship('ProductArea', backref=db.backref('feature_request'))

db.create_all()


# Create logical data abstraction (same as data storage for this first example)
class ClientSchema(Schema):
    class Meta:
        type_ = 'client'
        self_view = 'client_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'client_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(requried=True)


class ProductAreaSchema(Schema):
    class Meta:
        type_ = 'product_area'
        self_view = 'product_area_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'product_area_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(requried=True)


class PrioritySchema(Schema):
    class Meta:
        type_ = 'priority'
        self_view = 'priority_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'priority_list'

    id = fields.Integer(as_string=True, dump_only=True)
    priority = fields.Integer(requried=True)


class FeatureRequestSchema(Schema):
    class Meta:
        type_ = 'feature_request'
        self_view = 'feature_request_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'feature_request_list'

    id = fields.Integer(as_string=True, dump_only=True)
    title = fields.Str(requried=True)
    description = fields.Str(requried=True)
    client = Relationship(attribute='client',
                         self_view='client_detail',
                         self_view_kwargs={'id': '<id>'},
                         schema='ClientSchema',
                         type_='client')
    client_priority = Relationship(attribute='client_priority',
                         self_view='priority_detail',
                         self_view_kwargs={'id': '<id>'},
                         schema='PrioritySchema',
                         type_='priority')
    target_date = fields.Date(requried=True)
    product_area = Relationship(attribute='product_area',
                         self_view='product_area_detail',
                         self_view_kwargs={'id': '<id>'},
                         schema='ProductAreaSchema',
                         type_='product_area')


# Create resource managers
class ClientList(ResourceList):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Client}


class ClientDetail(ResourceDetail):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Client}


class ProductAreaList(ResourceList):
    schema = ProductAreaSchema
    data_layer = {'session': db.session,
                  'model': ProductArea}


class ProductAreaDetail(ResourceDetail):
    schema = ProductAreaSchema
    data_layer = {'session': db.session,
                  'model': ProductArea}


class PriorityList(ResourceList):
    schema = PrioritySchema
    data_layer = {'session': db.session,
                  'model': Priority}


class PriorityDetail(ResourceDetail):
    schema = PrioritySchema
    data_layer = {'session': db.session,
                  'model': Priority}


class FeatureRequestDetail(ResourceDetail):
    schema = FeatureRequestSchema
    data_layer = {'session': db.session,
                  'model': FeatureRequest}


class FeatureRequestList(ResourceList):
    schema = FeatureRequestSchema
    data_layer = {'session': db.session,
                  'model': FeatureRequest}


# Create endpoints
api = Api(app)
api.route(ClientList, 'client_list', '/clients')
api.route(ClientDetail, 'client_detail', '/clients/<int:id>')
api.route(ProductAreaList, 'product_area_list', '/product_areas')
api.route(ProductAreaDetail, 'product_area_detail', '/product_areas/<int:id>')
api.route(PriorityList, 'priority_list', '/priorities')
api.route(PriorityDetail, 'priority_detail', '/priorities/<int:id>')
api.route(FeatureRequestList, 'feature_request_list', '/feature_requests')
api.route(FeatureRequestDetail, 'feature_request_detail', '/feature_requests/<int:id>')

if __name__ == '__main__':
    # Start application
    app.run(debug=True)