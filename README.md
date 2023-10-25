## メール送信自動化スクリプト

このスクリプトは、指定されたCSVファイルとテンプレートテキストファイルを使用して、大量のメールを自動送信するためのものです。

### 使用方法

1. `sample_data/csvfile.csv`を編集して、送信先の情報を入力します。CSVファイルのフォーマットは以下の通りです:
```
email@example1.com,John,Company A
email@example2.com,Jane,Company B
```

2. `sample_data/templatefile.txt`を編集して、メールのテンプレートを作成します。テキストには`<<n>>`のようなプレースホルダーを使用して、CSVファイルのデータで置き換えることができます。

3. スクリプトを実行して、メールを送信します。

### 注意点
- GmailのSMTPを使用してメールを送信していますので、Gmailのアカウントとパスワードが必要です。
- 送信の間隔は約0.9秒となっています。この間隔や他の設定は、必要に応じてスクリプト内で変更することができます。

---

## Email Automation Script

This script is for automatically sending out a large number of emails using a specified CSV file and a template text file.

### How to Use

1. Edit `sample_data/csvfile.csv` to input the recipient information. The format of the CSV file is as follows:
```
email@example1.com,John,Company A
email@example2.com,Jane,Company B
```

2. Edit `sample_data/templatefile.txt` to craft your email template. You can use placeholders like `<<n>>` in the text which will be replaced by the data from the CSV file.

3. Run the script to send the emails.

### Points to Note
- The script uses Gmail's SMTP for sending emails, so you will need a Gmail account and password.
- There's a sleep interval of about 0.9 seconds between sending emails. You can change this interval or other settings as needed within the script.