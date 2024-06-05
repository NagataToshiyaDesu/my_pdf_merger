import sys
from my_pypdf_module import pypdf_merge_module as pmm

def main() -> None:
    # 結合するPDFファイルが少なくとも2つあることを確認
    if len(sys.argv) <= 2:
        print("エラー: 結合には少なくとも2つのファイルが必要です。")
        sys.exit(1)

    # コマンドライン引数からPDFファイルのパスを取得
    file_list = sys.argv[1:]
    
    # ユーザーから有効な出力ファイル名を取得
    output_filename = pmm.get_valid_filename()

    # PDFを結合
    pmm.merge_pdfs(file_list, output_filename)

if __name__ == "__main__":
    main()
