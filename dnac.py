import requests
import pprint

url = "https://sandboxdnac.cisco.com/api/v1/network-device"

payload = {}
headers = {
  'accept': 'application/json',
  'x-auth-token': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY3RpdmVSRCI6IjI3MjMxNTFhNjEwODFhYTgzMDMzYTdiYTQ3NWE0YmFjYjQxN2VjOTQiLCJhdWQiOiJDRE5BIiwiYXV0aFNvdXJjZSI6ImxlZ2FjeSIsImNsaWVudElkIjoiZGV2bmV0dXNlciIsImVtYWlsIjoiZGV2bmV0dXNlckBsb2NhbHVzZXIuY29tIiwiZXhwIjoxNzQzODgxNDQwLCJpYXQiOjE3NDM4Nzc4NDAsImlzcyI6ImRuYWMiLCJyZHMiOlsiMjcyMzE1MWE2MTA4MWFhODMwMzNhN2JhNDc1YTRiYWNiNDE3ZWM5NCJdLCJyZXNvdXJjZUdyb3VwcyI6Ikg0c0lBQUFBQUFBQS80cXVWaW91U2c1S0xjNHZMVXBPOVV4UnNsTFNVdEpSS3Frc1NGV3lVaXJPTEVsVnFvMEZCQUFBLy8rY3ZYZktKUUFBQUE9PSIsInJvbGVzIjpbIk9CU0VSVkVSIl0sInNlc3Npb25JZCI6IjY3ZjZjZWM2LTI5NDMtNTVmZi04NjMwLWQ5Njk3NDcyMWY1NSIsInN1YiI6IjY3ZDA1NzMwZWEyYTE0MDA1NTg1Zjc1YyIsInRlbmFudElkIjoiNjczN2YyNjcwZWI5ZDQwMDEzMTM3ZDgzIiwidGVuYW50TmFtZSI6IlROVDAiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.15hWGD7Y2TKLRkIG_RBurakV3lCX4uDtupgPmPoskPKJmh3BHAAIWezl3feBOPMxSGJzlfAgMrSts2MXR8T7sA'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

pprint.pprint(response.text)
