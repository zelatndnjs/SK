time = 12345
hour = time//3600
minutes = time%3600//60
seconds = time%3600%60
print(f"12345초는 {hour}시간 {minutes}분 {seconds}초입니다.")