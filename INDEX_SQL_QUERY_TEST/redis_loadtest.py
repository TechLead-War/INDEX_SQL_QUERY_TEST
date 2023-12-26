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
    
    # Determine the hash bucket based on the key
    hash_bucket = int(key.split('_')[1]) // 1000
    hash_key = f"mediabucket:{hash_bucket}"

    # Add the key-value pair to the Redis Hash
    redis_client.hset(hash_key, key, value)


if __name__ == "__main__":
    try:
        p = 0
        # Run the script indefinitely, adding data to Redis Hash and printing Redis memory usage
        while True:
            p = p + 1
            add_data_to_redis()

            # Print Redis memory usage after every 1000 additions
            if p% 1000 == 0:
                redis_memory_usage = get_redis_memory_usage()
                print(f"H-Set Redis Memory Usage: {redis_memory_usage:.2f} MB for {p} data")

    except KeyboardInterrupt:
        print("Script terminated by user.")


