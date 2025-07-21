# 読書履歴検索サービス
import json
from google.cloud import bigquery

from book_concierge.prompt import RE_READ_INSTR, ROOT_AGENT_INSTR

class BookConciergeService:
    """
    BigQueryを使用して、読者の過去の書籍履歴を検索するサービスです。
    このサービスは、読者が過去に読んだ書籍の情報をBigQueryから取得し、
    生成AIがその情報を元に書籍を推薦するためのデータを提供します。
    """
    def __init__(self):
        """
        コンストラクタ
        BigQueryのクライアントを初期化します。
        """
        self.client = bigquery.Client()

    def get_read_books(self, user_id: str = "1") -> str:
        """
        指定されたユーザーIDに基づいて、過去に読んだ書籍の情報をBigQueryから取得し,
        生成AIが読み取りやすいようにJSON形式で返します。
        
        Args:
            user_id (str): ユーザーの一意の識別子
        
        Returns:
            list: 過去に読んだ書籍の情報のリスト
        """
        query = """
            SELECT book_title, author, read_date
            FROM `book_recommendations.read_books`
            WHERE user_id = @user_id
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("user_id", "STRING", user_id)
            ]
        )
        query_job = self.client.query(query, job_config=job_config)
        results = query_job.result()

        return json.dumps([{
            "book_title": row.book_title,
            "author": row.author,
            "read_date": row.read_date.isoformat()
        } for row in results], ensure_ascii=False)

    def build_root_prompt(self) -> str:
        sql_result_json = self.get_read_books()
        return ROOT_AGENT_INSTR + f"\n過去に読んだ本のリスト: {sql_result_json}\n"

    def build_re_read_prompt(self) -> str:
        sql_result_json = self.get_read_books()
        return RE_READ_INSTR + f"\n過去に読んだ本のリスト: {sql_result_json}\n" 
