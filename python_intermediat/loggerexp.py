import logging,time,threading

"""-------------------------------------------"""

# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO
# )
# for i in range(1,20):
#     logging.info("Application started")
#     logging.error("Database not found")
#     time.sleep(1)

"""-------------------------------------------"""

logging.basicConfig(
    filename="button.log",
    level=logging.INFO,
    format="%(levelname)s - %(threadName)s - %(message)s"
)

def work():
    for i in range(6):
        logging.info(f"Step {i}")
        time.sleep(2)

t1 = threading.Thread(target=work, name="Worker-1")
t2 = threading.Thread(target=work, name="Worker-2")

t1.start()
t2.start()

t1.join()
t2.join()