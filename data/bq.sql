CREATE TABLE book_recommendations.read_books (
  user_id    STRING NOT NULL,
  book_title STRING NOT NULL,
  author     STRING,
  read_date  DATE
);
INSERT INTO `book_recommendations.read_books` (user_id, book_title, author, read_date) VALUES
('1','SQLアンチパターン 第一版','Bill Karwin','2023-12-06'),
('1','エリック・エヴァンスのドメイン駆動設計','Eric Evans','2024-06-17'),
('1','プリンシプル オブ プログラミング 3年目までに身につけたい 一生役立つ101の原理原則','上田勲','2024-06-24'),
('1','手を動かしてわかるクリーンアーキテクチャ ヘキサゴナルアーキテクチャによるクリーンなアプリケーション開発','Tom Hombergs','2024-09-30'),
('1','Clean Architecture 達人に学ぶソフトウェアの構造と設計','Robert C.Martin','2024-09-30'),
('1','セキュア・バイ・デザイン 安全なソフトウェア設計','Dan Bergh Johnsson,Daniel Deogun,Daniel Sawano','2024-11-30'),
('1','エクストリームプログラミング','Kent Beck,Cynthia Andres','2024-12-04'),
('1','Tidy First? ―個人で実践する経験主義的ソフトウェア設計','Kent Beck','2025-02-07'),
('1','テスト駆動開発','Kent Beck','2025-03-02')
;
