from subprocess import call
f = open("example1.json", "w")
call (["ffprobe","-i","example1.mp4","-print_format","json","-show_streams","-show_format","-show_data","-hide_banner"], stdout=f)