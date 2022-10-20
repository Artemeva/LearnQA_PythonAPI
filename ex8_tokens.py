import requests
import time

# Start job, get token and waiting time
job_init = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
init_response = job_init.json()

wait_time = init_response["seconds"]
response_token = init_response["token"]

# We can add optional info for user (so he knows how long he will be waiting)
# print("The job will be done in ",wait_time,"seconds")

# checking if job in progress has correct status
job_in_progress = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":response_token})
progress_response = job_in_progress.json()

if progress_response["status"] != "Job is NOT ready":
    print("Job in progress has wrong status")

# Waiting for job to be done
time.sleep(wait_time)

# Get and check job results
job_done = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":response_token})
done_response = job_done.json()

job_result_key = "result"

if done_response["status"] == "Job is ready":
    if job_result_key in done_response:
# print result was not requested in exercise, but I think we need a least some output
        print("Job finished successfully in",wait_time,"seconds with result",done_response[job_result_key])
    else:
        print("Job has no result")
else:
    print("Job has wrong status")