from elastic_api.AverageTimeWaitedLoader import AverageTimeWaitedLoader
import matplotlib.pyplot as plt

start_time = "2016-03-22 17:00"
end_time = "2016-03-23 17:00"
interval = 5
turbo = AverageTimeWaitedLoader(start_time, end_time, interval)

# this calculates the average time the patients have been waiting for triage, if they are waiting for triage
turbo.set_search_triage()

# this calculates the average time the patients have been waiting for a doctor, if they are waiting for a doctor
# turbo.set_search_doctor()

# this calculates the average time the patients have been at the emergency room
# turbo.set_search_removed()

v = turbo.load_vector()

plt.plot(v)
plt.title(start_time + " to " + end_time)
plt.show()
