import cv2
import os

# === CONFIG ===
video_files = {
    'NZ10': r'testing_video\NZD10_resized_video_640x640.mp4',
    'NZ20': r'testing_video\NZD20_resized_video_640x640.mp4',
    'NZ50': r'testing_video\NZD50_resized_video_640x640.mp4'
}

output_root = 'extracted_frames'
frame_interval = 50  # Save every Nth frame

os.makedirs(output_root, exist_ok=True)

for bill_type, video_path in video_files.items():
    print(f"\n📹 Processing {bill_type}: {video_path}")
    
    save_dir = os.path.join(output_root, bill_type)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_id = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % frame_interval == 0:
            filename = f"{bill_type}_{frame_id:05d}.jpg"
            cv2.imwrite(os.path.join(save_dir, filename), frame)
            print(f"Saved: {filename}")
            saved_count += 1

        frame_id += 1

    cap.release()
    print(f"✅ Done: {saved_count} frames saved to {save_dir}")

print("\n🎉 All videos processed!")
