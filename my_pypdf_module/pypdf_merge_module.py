import sys,os
import pypdf as pp
from typing import List
def merge_pdfs(file_list: List[str], output_name: str) -> None:
    """
    PDFファイルのリストを結合して1つのPDFファイルにします。

    :param file_list: 結合するファイルのパスリスト
    :param output_name: 出力する結合PDFファイルの名前
    """
    pdf_merger = pp.PdfWriter()
    for file in file_list:
        try:
            pdf_merger.append(file)
        except FileNotFoundError:
            print(f"ファイルが見つかりませんでした: {file}")
            sys.exit(1)
    pdf_merger.write(output_name)
    pdf_merger.close()
    print("結合成功。")

def get_valid_filename() -> str:
    """
    結合されたPDFの有効なファイル名をユーザーに入力させます。

    :return: 有効なファイル名
    """
    while True:
        pdf_name = input("結合後のPDF名を入力してください => ").strip()
        if not pdf_name:
            print("エラー: ファイル名には少なくとも1文字必要です。")
            continue
        merged_pdf_name = f"{pdf_name}.pdf"
        if os.path.exists(merged_pdf_name):
            overwrite = input("この名前は既に使用されています。上書きしますか？ (Y/n) => ").strip().upper()
            if overwrite == 'Y':
                return merged_pdf_name
        else:
            return merged_pdf_name
