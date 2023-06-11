# png4tweet

ツイート用にpng画像を8bit(256色)カラー形式に変換するプログラム

inputフォルダに変換したい画像を入れてRUN.batを実行するとoutputフォルダに内に変換された画像が出力されます。複数可

# 環境構築

python(プログラム言語)を下記のURLを押してしてインストールしてください。インストールだけで済むので簡単です！

python https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe

次に、上にリストのように並べられている、変換するためのファイル構成と変換プログラムをダウンロードします。

画像のようにクリックするとダウンロードできます。自分がわかりやすい所に解凍してください。
![image](https://github.com/keimaruO/png4tweet/assets/91080250/eb4aa156-f9c9-4293-b57e-dfc352a29b9b)


無事解凍できたら次にffmpegを下記のURLからダウンロードしてきます。

https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest

画像のをダウンロードしたら解凍します
![image](https://github.com/keimaruO/png4tweet/assets/91080250/31c255f5-9170-4479-a6d2-424633b8f212)


解凍したファイル内にffmpeg.exeがあるので先程解凍したフォルダ内に画像のように配置してください。
![image](https://github.com/keimaruO/png4tweet/assets/91080250/99f6f7bd-abf3-46c6-b16d-3a397735b9fa)


# 使い方

inputフォルダ内に変換したい元画像をぶちこんでください。

そしてRUN.pyをダブルクリックで実行して、数秒すると黒い画面が閉じて、outputフォルダ内に出力されます。

2回目以降使う場合はinput,outputフォルダ内の画像を空にしておいてください。別の場所に保存だー！
