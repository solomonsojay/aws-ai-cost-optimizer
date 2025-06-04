import json
import boto3
from botocore.config import Config

def lambda_handler(event, context):
    # Configure Bedrock client with longer timeout
    bedrock_config = Config(
        region_name='us-east-1',
        connect_timeout=10,
        read_timeout=30
    )
    bedrock = boto3.client('bedrock-runtime', config=bedrock_config)
    
    # Sample AWS cost data
    aws_cost_data = {
        "Services": {
            "EC2": {"MonthlyCost": 1200, "InstanceCount": 8},
            "S3": {"MonthlyCost": 500, "StorageGB": 2500},
            "RDS": {"MonthlyCost": 800, "InstanceCount": 3}
        },
        "TotalMonthly": 2500
    }
    
    # Claude 2.1 Prompt
    prompt = """\n\nHuman: Analyze this AWS cost data and provide:
1. Top 3 cost-saving recommendations
2. Estimated monthly savings for each
3. Specific AWS services to modify
4. Implementation steps

Format as markdown with bold headings.

Data:
{data}

\n\nAssistant:""".format(data=json.dumps(aws_cost_data, indent=2))

    try:
        # Call Claude 2.1
        response = bedrock.invoke_model(
            modelId='anthropic.claude-v2:1',
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 1500,
                "temperature": 0.3
            })
        )
        
        # Get AI response
        result = json.loads(response['body'].read())
        
        # Return properly formatted JSON
        return {
            "status": "success",
            "message": "Analysis complete",
            "recommendations": result['completion']
        }
        
    except Exception as e:
        # Return error in consistent JSON format
        return {
            "status": "error",
            "message": str(e),
            "tip": "Check Bedrock permissions and network connectivity"
        }