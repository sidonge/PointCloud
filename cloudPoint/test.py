import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. 가짜 데이터 생성 함수
def generate_wave(frame):
    width, height = 50, 50 # 렉 걸리지 않게 점 개수 조절
    x = np.linspace(0, 10, width)
    y = np.linspace(0, 10, height)
    xv, yv = np.meshgrid(x, y)
    
    # 파도 움직임
    z = np.sin(xv + frame * 0.1) + np.cos(yv + frame * 0.1)
    
    # 1차원 배열로 펼치기 (scatter plot용)
    return xv.flatten(), yv.flatten(), z.flatten()

# 2. 그래프 설정
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-2, 2)
ax.set_title("Real-time Point Cloud Simulation (Matplotlib)")
ax.set_xlabel("X (Robot Base)")
ax.set_ylabel("Y (Robot Base)")
ax.set_zlabel("Z (Height)")

# 초기 점 찍기
x, y, z = generate_wave(0)
scat = ax.scatter(x, y, z, c=z, cmap='viridis', s=5)

# 3. 애니메이션 업데이트 함수
def update(frame):
    x, y, z = generate_wave(frame)
    
    # 점들의 위치(x,y)는 그대로고 높이(z)와 색상만 바뀜
    scat._offsets3d = (x, y, z)
    scat.set_array(z) # 색상 업데이트
    return scat,

# 4. 애니메이션 실행
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)
plt.show()