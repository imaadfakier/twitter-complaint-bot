import config
import os
import bot

twitter_complaint_bot = bot.InternetSpeedTwitterBot(
    os.environ.get('CHROME_DRIVER_PATH'),
    config.PROMISED_DOWN_SPEED_IN_MBPS,
    config.PROMISED_UP_SPEED_IN_MBPS
)

down_speed_now, up_speed_now = twitter_complaint_bot.get_internet_speed()
twitter_complaint_bot.log_into_twitter()
twitter_complaint_bot.tweet_at_provider(down_speed_now, up_speed_now)
