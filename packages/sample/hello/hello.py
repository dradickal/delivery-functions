def main(event, context):
      print(f'{{ requestId: {context.request_id}, function: {context.namespace}/{context.function_name}, version: {context.function_version} }}')
      return {
            "body": {
                  "event": event,
                  "context": {
                        "activationId": context.activation_id,
                        "apiHost": context.api_host,
                        "apiKey": context.api_key,
                        "deadline": context.deadline,
                        "functionName": context.function_name,
                        "functionVersion": context.function_version,
                        "namespace": context.namespace,
                        "requestId": context.request_id,
                  },
            },
            "statusCode": 200,
		"headers": {
			"Content-Type": "application/json"
		}
      }
