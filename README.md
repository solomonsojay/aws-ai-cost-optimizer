# ☁️ AWS AI Cost Optimizer

**AI-Powered Cloud Cost Reduction Solution**  
*Reduce AWS bills by 25-40% with generative AI recommendations*

## 🚀 Live Demo
[![Open Demo](https://img.shields.io/badge/Demo-Live%20Site-brightgreen)](https://staging.dnxvuwy2sif3a.amplifyapp.com/)

## 📂 Source Code
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/solomonsojay/aws-ai-cost-optimizer)

## 🌟 Overview
The AWS AI Cost Optimizer leverages generative AI through AWS Bedrock to analyze your cloud infrastructure costs and provide actionable optimization recommendations. This solution helps businesses reduce AWS spending by 25-40% through AI-powered insights.

## ⚙️ How AWS Lambda Powers This Solution
AWS Lambda serves as the **core processing engine** of our application:

1. **AI Gateway**: Receives requests from the frontend and communicates with AWS Bedrock
2. **Prompt Engineering**: Generates optimized prompts for Claude AI based on cost data
3. **Response Processing**: Formats AI output into structured markdown recommendations
4. **Error Handling**: Manages timeouts and Bedrock API exceptions
5. **Security Layer**: Validates requests before processing

**Lambda Configuration**:
- Runtime: Python 3.10
- Memory: 512MB
- Timeout: 30 seconds
- Permissions: `AWSBedrockFullAccess`
- Trigger: Lambda Function URL (HTTPS endpoint)

## 🧪 Testing Instructions for Judges

### Option 1: Live Demo Testing (Recommended)
1. Visit our live demo: [https://staging.dnxvuwy2sif3a.amplifyapp.com/](https://staging.dnxvuwy2sif3a.amplifyapp.com/)
2. Click the **"Analyze My AWS Costs"** button
3. Observe the AI processing stages:
   - Connecting to AWS Lambda
   - Authenticating with AWS Bedrock
   - Analyzing with Claude AI
4. View generated recommendations (appears in 5-10 seconds)

### Option 2: Manual Backend Testing
Test the Lambda function directly using curl:

```bash
curl -X POST "https://ebagyvsks5l3rtryodwdzfihte0iolgi.lambda-url.us-east-1.on.aws/" \
  -H "Content-Type: application/json" \
  -d '{}'

