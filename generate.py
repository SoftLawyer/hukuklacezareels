import os
import sys
import json
import subprocess
from playwright.sync_api import sync_playwright

def generate_reel(data_json_path, output_mp4_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, 'templates', 'reel_template.html')
    
    with open(data_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    with open(template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Replace placeholders
    html_content = html_content.replace('{hook_line1}', data.get('hook_line1', 'ÇOĞU'))
    html_content = html_content.replace('{hook_line2}', data.get('hook_line2', 'HUKUKÇU'))
    html_content = html_content.replace('{hook_line3}', data.get('hook_line3', 'BUNU'))
    html_content = html_content.replace('{hook_line4}', data.get('hook_line4', 'ÇÖZEMİYOR:'))
    html_content = html_content.replace('{question_text}', data.get('question_text', 'Soru metni buraya gelecek.'))
    html_content = html_content.replace('{option_a}', data.get('option_a', 'Seçenek A'))
    html_content = html_content.replace('{option_b}', data.get('option_b', 'Seçenek B'))
    html_content = html_content.replace('{option_c}', data.get('option_c', 'Seçenek C'))
    html_content = html_content.replace('{option_d}', data.get('option_d', 'Seçenek D'))
    
    temp_html_path = os.path.join(base_dir, "temp_render.html")
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    output_png = os.path.join(base_dir, "temp_image.png")
    
    print("Generating image via Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        page.goto(f"file://{temp_html_path}", wait_until="networkidle")
        page.wait_for_timeout(2000) # Wait for fonts and tailwind
        page.screenshot(path=output_png)
        browser.close()
        
    print(f"Generated PNG: {output_png}")
    
    print("Generating static 5-second Reel video from image...")
    # Generate 5 second video from the static image using ffmpeg
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1',
        '-i', output_png,
        '-c:v', 'libx264',
        '-t', '5',
        '-pix_fmt', 'yuv420p',
        output_mp4_path
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully generated final Reel video at: {output_mp4_path}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed with error:\n{e.stderr.decode()}")
        
    # Cleanup temps
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    if os.path.exists(output_png):
        os.remove(output_png)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate.py <data_json_path> <output_mp4_path>")
        sys.exit(1)
        
    generate_reel(sys.argv[1], sys.argv[2])
