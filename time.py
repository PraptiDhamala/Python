import time
now= time.time()
print(now)

print ("Waiting")
time.sleep(2)
print("Done")

print(time.ctime())

local=time.localtime()
print(local.tm_year,local.tm_mon,local.tm_mday)
print(local.tm_hour,local.tm_min,local.tm_sec)

print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%A, %d %B %Y"))

t = time.strptime("2026-10-11 09:15:00", "%Y-%m-%d %H:%M:%S")
print(t.tm_hour)  

print(time.mktime(t))

start = time.perf_counter()
total = sum(i * i for i in range(1_000_000))
end = time.perf_counter()
print(f"Elapsed: {end - start:.4f} seconds")