import os

def split_vtt():
    filepath = input("Enter file Path: ")
    segment_time = float(input("Enter time in sec: "))
    release_file_path = rf"{filepath}"

    if not os.path.isfile(release_file_path):
        print("File not found:", release_file_path)
        return

    segments = []
    current_segment = ["WEBVTT\n\n"]
    segment_start_time = 0

    with open(release_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if "-->" in line:
                start, end = line.split("-->")
                start_time = parse_time(start.strip())
                end_time = parse_time(end.strip())

                if start_time - segment_start_time >= segment_time:
                    segments.append(current_segment)
                    current_segment = ["WEBVTT\n\n"]
                    segment_start_time = start_time

                # Adjust timecodes relative to segment start
                adjusted_start = format_time(start_time - segment_start_time)
                adjusted_end = format_time(end_time - segment_start_time)
                current_segment.append(f"{adjusted_start} --> {adjusted_end}\n")
            else:
                current_segment.append(line)

    if current_segment:
        segments.append(current_segment)

    for i, segment in enumerate(segments):
        with open(f"segment_{i}.vtt", 'w', encoding='utf-8') as segment_file:
            segment_file.writelines(segment)

def parse_time(time_str):
    time_parts = time_str.replace(',', '.').split(':')
    if len(time_parts) == 3:
        h, m, s = time_parts
    elif len(time_parts) == 2:
        h, m, s = 0, time_parts[0], time_parts[1]
    else:
        raise ValueError(f"Unexpected time format: {time_str}")
    return int(h) * 3600 + int(m) * 60 + float(s)

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.', ',')

# Run the script
split_vtt()
