def main(args):
    print(args)
    subject = args.get("subject", "life")
    return {
        "body": {
            "answer": subject+ " is suffering"
        }
    }