import time

def load_data():
    time.sleep(0.02)

def transform_data():
    time.sleep(0.06)

def process():
    for _ in range(5):
        load_data()
        transform_data()

if __name__ == "__main__":
    process()
