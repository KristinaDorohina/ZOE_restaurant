"""Конфигурация (SECRET_KEY, DB_URL)"""
import os
import secrets
from pathlib import Path


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))

    BASE_DIR = Path(__file__).parent.parent
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "instance" / "zoe_restaurant.db"}')
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_timeout': 20}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = BASE_DIR / 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB лимит

    DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() in ('true', '1', 't')