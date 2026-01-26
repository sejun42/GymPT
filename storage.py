import os

import boto3
from botocore.config import Config
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


def get_r2_client():
    return boto3.client(
        service_name="s3",
        endpoint_url=f"https://{os.getenv('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=os.getenv('R2_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('R2_SECRET_KEY'),
        region_name="auto",
        config=Config(signature_version="s3v4"),
    )


def upload_to_r2(local_file_path, file_name, delete_local=True):
    client = get_r2_client()
    bucket_name = os.getenv('R2_BUCKET_NAME')
    public_url = os.getenv('R2_PUBLIC_URL')

    try:
        # R2에 업로드
        client.upload_file(local_file_path, bucket_name, file_name)
        # 업로드 성공 시 로컬 파일 삭제 (옵션)
        if delete_local:
            os.remove(local_file_path)
        # 접근 가능한 최종 URL 반환
        return f"{public_url}/{file_name}"
    except Exception as e:
        print(f"R2 Upload Error: {e}")
        return None
