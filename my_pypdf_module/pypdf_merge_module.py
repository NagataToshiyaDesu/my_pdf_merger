import sys,os
try:
    import pypdf as pp
except  ModuleNotFoundError as MNFe:
    print(f"{MNFe}, \npypdfが見つかりませんでした。pip install -r requirements.txt を実行してください。")
from typing import List

def merge_pdfs(file_list: List[str], output_name: str) -> None:
    """
    PDFファイルのリストを結合して1つのPDFファイルにする。

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
    結合されたPDFの有効なファイル名をユーザーに入力させる。

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

def check_files_count(input_files: list) -> None:
    """
    入力されたpdfファイルが2個以上か調べる
    
    :param input_files: batからの引数
    """
    if len(input_files) <= 2:
        print("エラー: 結合には少なくとも2つのファイルが必要です。")
        exit(1)
    
    for ex in input_files[:4]:
        if not ex == ".pdf": 
            print("エラー: pdf以外のファイルが含まれています。")
            exit(1)