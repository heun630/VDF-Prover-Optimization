import matplotlib.pyplot as plt
import numpy as np

T_values = np.array([21, 22, 23, 24, 25])
# Assumed evaluation and proof times for these T values


result1 = np.array([0.283, 0.587, 1.144, 3.047, 4.896])
result2 = np.array([0.768, 1.591, 3.175, 6.329, 13.475])
result3 = np.array([2.441, 5.117, 10.112, 20.191, 40.363])

result4 = np.array([0.344, 0.652, 1.272, 3.301, 4.983])
result5 = np.array([0.921, 1.805, 3.606, 7.051, 14.095])
result6 = np.array([3.007, 6.030, 12.066, 24.124, 48.181])

result7 = np.array([7.96, 30.66, 105.48, 412.51, 1720.31])
result8 = np.array([10.60, 38.17, 112.52, 463.04, 1758.72])
result9 = np.array([15.560, 40.78, 135.32, 480.67, 1812.67])

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(T_values, result1, marker='o', color="red", linestyle='-')
plt.plot(T_values, result2, marker='o', color="green", linestyle='-')
plt.plot(T_values, result3, marker='o', color="blue", linestyle='-')

plt.plot(T_values, result4, marker='o', color="red", linestyle='--')
plt.plot(T_values, result5, marker='o', color="green", linestyle='--')
plt.plot(T_values, result6, marker='o', color="blue", linestyle='--')

# plt.plot(T_values, result7, marker='o', color="red", linestyle=':')
# plt.plot(T_values, result8, marker='o', color="green", linestyle=':')
# plt.plot(T_values, result9, marker='o', color="blue", linestyle=':')

plt.plot([], [], label='λ = 512', color="red", linestyle='-')
plt.plot([], [], label='λ = 1024', color="green", linestyle='-')
plt.plot([], [], label='λ = 2048', color="blue", linestyle='-')
plt.plot([], [], label='Golang', color="black", linestyle='-')
plt.plot([], [], label='C++', color="black", linestyle='--')
# plt.plot([], [], label='Python', color="black", linestyle=':')


# 세부 그리드 설정 추가
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)


plt.xlabel('Number of Exponentiations', fontsize=14)
plt.ylabel('Time(s)', fontsize=14)
plt.title('Evaluation time(Golang, C++)', fontsize=16)
plt.xticks(T_values, labels=[f'{i}' for i in T_values])
# plt.yticks(np.arange(0, max(result1) + 10, 2))
plt.legend(loc='upper left')
# plt.grid(True)
plt.yscale('linear')

plt.show()
