import redis
import time
import random

# Connect to Redis (assuming Redis is running locally on the default port)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_redis_memory_usage():
    # Use the INFO command to get memory information
    info = redis_client.info("memory")
    memory_used = int(info['used_memory']) / (1024 ** 2)  # Memory usage in MB
    return memory_used

def add_data_to_redis():
    # Generate a random key and value for demonstration purposes
    key = f"key_{random.randint(1, 10000000000000)}"
    value = f"value_{random.randint(1, 100000000000000)}"

    # Add the key-value pair to Redis
    redis_client.set(key, value)

    # Print Redis memory usage after each addition

if __name__ == "__main__":
    try:
        p = 0
        # Run the script indefinitely, adding data to Redis and printing Redis memory usage
        while True:
            p = p + 1
            add_data_to_redis()
            if p%1000 == 0:
                redis_memory_usage = get_redis_memory_usage()
                print(f"set-get Redis Memory Usage: {redis_memory_usage:.2f} MB for {p} data")

    except KeyboardInterrupt:
        print("Script terminated by user.")