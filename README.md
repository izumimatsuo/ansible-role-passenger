# ansible-role-passenger

CentOS 7 に Phusion passenger の実行環境を構築する ansible role です。

* rbenv 1.1
* bundler 1.19
* ruby 2.5
* Phusion passenger 5.2

## 設定項目

以下の設定項目は上書き可能。

項目名             |デフォルト値  |説明
-------------------|--------------|---------------------------------------------
passenger_conf_file|passenger.conf|apache httpd との連携を定義する設定ファイル。
