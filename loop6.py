m_Array = ["one", "two", "three"];
print(m_Array[:])
for m in m_Array[:]:
    print(len(m))
    if len(m) > 3:
        m_Array.insert(0, m);
        print(m)
print(m_Array[0]);
print(m_Array[0:])
