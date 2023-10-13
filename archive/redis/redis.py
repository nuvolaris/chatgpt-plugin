def main(args):
    print(args)
    return {
        "body": {
            "redis_url": args.get("redis_url", "not found"),
            "redis_prefix": args.get("redis_prefix", "notfoud")
        }
    }