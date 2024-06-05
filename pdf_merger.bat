@echo off
SET /P  PDF_PATH="D&D PDF's => "
python pdf_merger.py %PDF_PATH%
pause