from os import listdir
from os.path import isfile, isdir, join
from datetime import datetime

# 時系列ファイル群をまとめる
def log_time_seriser(target_dir: str, outPath: str, headlessMode: bool = True):

	if not isdir(target_dir):
		return False

	_parse_log_files(target_dir)

	return True

# 時系列ファイル群を一括解析
def _parse_log_files(dir: str, encoding: str ='utf-8'):

	assert isdir(dir)

	files = [f for f in listdir(dir) if isfile(join(dir, f))]

	for file in files:
		_parse_one_log_file((file))

	return True

# 時系列ファイルを１件解析
def _parse_one_log_file(file_path: str, encoding: str ='utf-8'):

	fileio = open(file_path, mode="r", encoding=encoding )

	Lines = fileio.readlines()
  
	indx = 0
	for line in Lines:
		print("{}: {}".format(indx, line.strip()))
		indx += 1

		# タイムスタンプを解析
		date, text = _parse_timestamp(line)

		# 日付別に出力
		_export_to_daily_file(date, text)


	fileio.close()

# タイムスタンプを解析
def _parse_timestamp(line:str):

	print('_parse_timestamp:' + line + ' の解析が必要')

	# TODO: line の中にあるタイムスタンプを datetime に変換すること
	date = datetime
	# TODO: line からタイムスタンプを除いた文字列を返すこと
	text = line

	return date, text

# 日付単位のファイルへ出力
def _export_to_daily_file(date: datetime, text:str):

	print('_export_to_daily_file:' + date + ' で ' + text + ' を出力')

	# 書き込みは遅延するので、バックスレッドで実行したい



