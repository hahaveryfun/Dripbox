from flask_restx import abort
from typing import List
from app.model import FileModel, UserModel
from app.app import db
from app.app import app
import uuid
import datetime
from app.utils import get_digest, get_name, get_extension
import os
from flask import safe_join
from app.utils.constants import FILE_STORAGE_PATH
from flask_jwt_extended import jwt_required

class File():
	def getFile(self, file_uuid, username) -> FileModel:
		file = FileModel.query.filter_by(file_uuid=file_uuid).first()
		if username:
			user = UserModel.query.filter_by(username=username).first()
			if user.id == file.owner:
				return file
			else:
				abort(403, message="Forbidden")
		elif file.public:
			return file
		else:
			abort(401, message="Unauthenticated")

	def setFile(self, file, username, is_public) -> FileModel:
		digest = get_digest(file)
		f = FileModel(
			file_uuid=str(uuid.uuid4()),
			file_name=str(get_name(file)),
			file_extension=str(get_extension(file)),
			date_uploaded=datetime.datetime.now(),
			date_modified=datetime.datetime.now(),
			file_digest=str(digest),
			source_identifier=str(digest+'.dripbox'),
			owner=int(UserModel.query.filter_by(username=username).first().id),
			public=bool(is_public)
		)
		file.seek(0)
		file_path = os.path.abspath(safe_join(FILE_STORAGE_PATH, digest+'.dripbox'))
		file.save(file_path)
		db.session.add(f)
		db.session.commit()
		return f
	
	def updateFile(self, file_uuid, updated_file, username, is_public) -> FileModel:
		user = UserModel.query.filter_by(username=username).first()
		file = FileModel.query.filter_by(file_uuid=file_uuid).first()
		if user.id == file.owner:
			digest = get_digest(updated_file)
			if digest != file.file_digest:
				file.file_digest = str(digest)
				file.source_identifier = str(digest+'.dripbox'),
			file.file_name = str(get_name(updated_file))
			file.file_extension = str(get_extension(updated_file))
			file.date_modified = datetime.datetime.now()
			public=bool(is_public)
			updated_file.seek(0)
			updated_file.save(os.path.abspath(safe_join(FILE_STORAGE_PATH, digest+'.dripbox')))
			db.session.commit()
			return file
		abort(403, message="Forbidden")
