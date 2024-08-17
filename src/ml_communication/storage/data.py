import os
from pathlib import Path
from abc import ABC, abstractmethod
import polars as pl


class DataStorage(ABC):
	@abstractmethod
	def get(self, path: Path) -> pl.DataFrame | None:
		pass


class LocalDataStorage(DataStorage):
	def get(self, path: Path) -> pl.DataFrame | None:
		extension = path.suffix

		if extension == '.json':
			return pl.read_json(path)

		elif extension == '.parquet':
			return pl.read_parquet(path)
		else:
			print(f'Unsupported file extension: {extension}')


class AwsBucketStorage(DataStorage):
	def __init__(self):
		self.storage_options = {
			'aws_access_key_id': os.environ.get('AWS_ACCESS_KEY_ID', None),
			'aws_secret_access_key': os.environ.get('AWS_SECRET_ACCESS_KEY', None),
			'aws_region': os.environ.get('REGION', None),
		}

	def get(self, path: Path) -> pl.DataFrame | None:
		extension = path.suffix
		if extension == '.parquet':
			return pl.read_parquet(path, storage_options=self.storage_options)
		else:
			print(f'Unsupported file extension: {extension}')
