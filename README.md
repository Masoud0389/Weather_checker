
# Weather checker
This code, checks the weather using API and if it's rainy, sends an SMS using Twilio virtual number. You can run this code on the cloud every morning at 7 AM to inform you about the weather before you go out.

## API Reference

#### Get all items

```http
  Weather forcast: https://pro.openweathermap.org/data/2.5/forecast/hourly 
  Current weather: https://api.openweathermap.org/data/2.5/weather
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |




## Deployment

To deploy this project run:

```bash
  python main.py
```

## FAQ

#### 1: Is sending SMS by Twilio free?

Yes, you can sign up in the https://www.twilio.com and after creating an account, you will get $15 credit. You can use your credit to buy a phone number.

#### 2: How can I run my app on the cloud?

The easiest way is using https://www.pythonanywhere.com website and its free subscription to run your code once a day.

