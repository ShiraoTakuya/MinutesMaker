
import os
from datetime import datetime

def create_minutes_file(input_text):
    # Get today's date in the format yyyymmdd
    today_date = datetime.now().strftime('%Y%m%d')

    # Create the file name
    file_name = f"議事録_{today_date}_{input_text}.txt"

    # Create and write to the file
    with open("minutes/"+file_name, 'w') as file:
        file.write(file_name[:-4] + '\n')  # Write the input text on the first line

    print(f"ファイル '{file_name}' を作成しました。")

def main():
	user_input = input("ファイル名に含めるテキストを入力してください: ")
	create_minutes_file(user_input)

main()
