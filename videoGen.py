from moviepy import VideoFileClip, concatenate_videoclips
import glob

# 获取所有MP4文件（按需修改路径）
video_files = glob.glob("assets/*.mp4")

clips = []
for file in video_files:
    # 截取前4秒（如果视频不足4秒会报错，添加异常处理按需）
    clip = VideoFileClip(file).subclipped(0, 3)
    
    # 统一为相同分辨率（可选）
    
    clips.append(clip)

# 合并视频（自动处理fps不一致问题）
final_clip = concatenate_videoclips(clips)

# 输出文件（调整参数优化体积/画质）
final_clip.write_videofile(
    "combined_output.mp4",
    codec="libx264",
    audio_codec="aac",
    threads=4,  # 多线程加速
    preset="fast",  # 编码速度与质量的平衡
    ffmpeg_params=["-crf", "18"]  # 画质参数（18-28，越小质量越高）
)

# 释放资源（避免某些系统报错）
for clip in clips:
    clip.close()
final_clip.close()
