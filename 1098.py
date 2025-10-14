i = 0.2
j = 1.2

print(f"I={0} J={1}")
print(f"I={0} J={2}")
print(f"I={0} J={3}")

while i <= 0.8:
    print(f"I={i:.1f} J={j:.1f}")
    print(f"I={i:.1f} J={j+1:.1f}")
    print(f"I={i:.1f} J={j+2:.1f}")
    i += 0.2
    j += 0.2


print(f"I={1} J={2}")
print(f"I={1} J={3}")
print(f"I={1} J={4}")

i += 0.2
j += 0.2

while i < 1.8:
    print(f"I={i:.1f} J={j:.1f}")
    print(f"I={i:.1f} J={j+1:.1f}")
    print(f"I={i:.1f} J={j+2:.1f}")
    i += 0.2
    j += 0.2

print(f"I={2} J={3}")
print(f"I={2} J={4}")
print(f"I={2} J={5}")