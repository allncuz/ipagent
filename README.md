# ipagent

**ipagent** is a FastAPI dependency for extracting client IP address, device, browser, and geo-location data
effortlessly.

---

## Project Description

`ipagent` makes it simple to access detailed client metadata in your FastAPI endpoints, including:

- Automatically detects client IP
- Fetches geolocation info using the IP address
- Device and browser information
- Operating system
- Geolocation (city and country)
- Minimal and easy-to-use FastAPI dependency

This package provides a plug-and-play `Depends` function that integrates smoothly into any FastAPI project.

---

## Installation

```bash
pip install ipagent
```

## How to Use

```python
from ipagent import get_client_info, ClientInfo
from fastapi import FastAPI, Depends

app = FastAPI()


@app.get('/')
async def user_data(user: ClientInfo = Depends(get_client_info)):
    return user
```

## Example Response

```json
{
  "ip_client": "31.110.210.10",
  "device_type": "Desktop",
  "browser": "Safari",
  "browser_version": "18.1",
  "os": "Mac OS X",
  "os_version": "10.15.7",
  "country": "Uzbekistan",
  "region": "Tashkent",
  "city": "Tashkent",
  "latitude": 49.2615,
  "longitude": 61.2177,
  "timezone": "Asia/Tashkent",
  "postal": null,
  "org": "UNITEL LLC"
}
```

## 💡 Ideas for Future Improvements

We believe `ipagent` can grow into a powerful, flexible client metadata toolkit. Here are some feature ideas and
improvements we’re excited about — and if you’d like to contribute, we’d be happy to collaborate!

## 🙌 Contribute a New Feature

We’d love to see your ideas in action! Here’s how you can fork the project, add a new feature, and open a pull request:

### 1. Fork the Repository

Go to [github.com/allncuz/ipagent](https://github.com/allncuz/ipagent) and click the **Fork** button to create your own
copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/ipagent.git
cd ipagent
```

Together, let’s make `ipagent` the most useful and elegant client metadata tool for FastAPI developers.