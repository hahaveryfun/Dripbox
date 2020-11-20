from flask_restx import Resource, Namespace
from flask import send_from_directory
from app.service import Drip as DripService
from app.app import api
import os
from app.utils.constants import FILE_STORAGE_PATH

api = Namespace('drip', description='Drip operations')

@api.route('/<string:file_uuid>')
class Drip(Resource):
	def get(self, file_uuid):
		drip = DripService().getDrip(file_uuid)
		return send_from_directory(
			FILE_STORAGE_PATH,
			drip.source_identifier,
			as_attachment=True,
			attachment_filename=".".join([drip.file_name, drip.file_extension]))
