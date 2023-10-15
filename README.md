## This is Leonardo.ai API.

[![PyPI version](https://badge.fury.io/py/leonardo-api.svg)](https://badge.fury.io/py/leonardo-api) [![Linters](https://github.com/wwakabobik/leonardo_api/actions/workflows/master-linters.yml/badge.svg?branch=master)](https://github.com/wwakabobik/leonardo_api/actions/workflows/master-linters.yml)

This package contains Python API for [Leonardo.ai](https://leonardo.ai/) based on official [API documentation](https://docs.leonardo.ai/reference).

![Leonardo.ai interface](https://raw.githubusercontent.com/wwakabobik/leonardo_api/master/src/assets/leonardo_interface.jpg)

To install the package, please use package from [pypi](https://pypi.org/project/leonardo-api/):

```bash
pip install leonardo-api
```

This Python API provides access to Leonardo API using synchronous methods (based on requests library) as well as asynchronous (aiohttp). You can choose one of them - `Leonardo` or `LeonardoAsync`.

To start, you must have paid subscription and create an API access token from you [settings page](https://app.leonardo.ai/settings)->User API. Then, init manager class with using your access_token:

```python
from leonardo_api import Leonardo

leonardo = Leonardo(auth_token='abcd-1234-5678-90ef-deadbeef00000')
```

Now you can use all API methods, provided by Leonardo.ai API, i.e. starting getting user info and generating your first image:

```python
response = leonardo.get_user_info()  # get your user info
response = leonardo.post_generations(prompt="The quick brown fox jumps over the lazy dog", num_images=1,
                                           negative_prompt='schrodinger cat paradox',
                                           model_id='e316348f-7773-490e-adcd-46757c738eb7', width=1024, height=768,
                                           guidance_scale=7)
```

In according to API reference, you will get the json answer with content about pending job like following:

```json
{"sdGenerationJob": {"generationId": "123456-0987-aaaa-bbbb-01010101010"}}
```

To obtain your image you need to use additional method:

```python
response = leonardo.get_single_generation(generation_id)  # get it using response['sdGenerationJob']['generationId']
```

Or, optionally, you may wait for job completion using following method:

```python
response = leonardo.wait_for_image_generation(generation_id=response['sdGenerationJob']['generationId'])
```

Finally, you'll get your array of images:

```python
[{'url': 'https://cdn.leonardo.ai/users/abcd-1234-5678-90ef-deadbeef00000/generations/123456-0987-aaaa-bbbb-01010101010/Absolute_Reality_v16_The_quick_brown_fox_jumps_0.jpg', 'nsfw': False, 'id': 'aaaaaa-bbbb-cccc-dddd-ffffffffff', 'likeCount': 0, 'generated_image_variation_generics': []}]
```

![The quick brown fox jumps over the lazy dog](https://raw.githubusercontent.com/wwakabobik/leonardo_api/master/src/assets/fox.jpeg)

You'll find descriptions for rest of the methods in official [API reference](https://docs.leonardo.ai/reference).

---

As option, you may want to use preloaded dicts with models (nsfw/community/platform):

```python
from leonardo_api import platform_models, custom_models, nsfw_models
```

Which contains details of models like following:

```python
{
    "data": {
        "custom_models": [
            {
                "id": "f1929ea3-b169-4c18-a16c-5d58b4292c69",
                "name": "RPG v5",
                # rest of the model data
            }
            # rest models
        ]
    }
}
```

Have fun and enjoy!

## Donations
If you like this project, you can support it by donating via [DonationAlerts](https://www.donationalerts.com/r/rocketsciencegeek).
