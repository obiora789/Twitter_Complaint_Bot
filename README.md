<h1>Twitter Complaint Bot</h1>
This program uses Selenium to automatically run Internet speed tests, and inform the ISP when the link is below advertised/optimal performance. <br>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8 or higher.</li>
  <li>Pycharm 2022.3.2 or higher.</li>
  <li>Selenium Webdriver(Chrome)</li>
  <li>Install and import Selenium Web driver.</li>
</ul>
<hr>
<h3>What to do</h3>
<ol>
  <li>Fork this Git and clone to your local PC.</li>
  <li>Download the selenium webdriver for your browser(I use Chrome i.e., chromedriver).</li>
  <li>Ensure you have updated Pycharm or other good updated IDE. I used Pycharm 2022.3.2 (Community Edition).</li>
  <li>Install Selenium undetected chromedriver within Pycharm console. e.g., pip install selenium</li>
  <li>Install python-dotenv within Pycharm console to translate environment variables. e.g., pip install python-dotenv</li>
  <li>Populate the environment variable with the actual path of your Selenium Chrome Webdriver.</li>
  <li>Specify your twitter username and password as environment variables.</li>
  <li>Specify the twitter handles of your main ISP and backup ISP as environment variables.</li>
  <li>Specify the advertised/promised bandwidth(download/upload) in Mbps (just provide the digits, the "Mbps" will be appended automatically) as environment variables.</li>
  <li>Populate the environment variables as stated below</li>
  <ul>
    <li>CHROME_PATH=pathToChromeDriverOnYourPC</li>
    <li>TWITTER_USERNAME=twitterUsername</li>
    <li>TWITTER_PASSWORD=twitterPassword</li>
    <li>ISP1=twitterHandleOfYourMainInternetServiceProvider</li>
    <li>ISP2=twitterHandleOfYourBackupInternetServiceProvider</li>
    <li>ISP1_PROMISED_UP=advertisedInternetUploadSpeedForMainISP</li>
    <li>ISP1_PROMISED_DOWN=advertisedInternetDownloadSpeedForMainISP</li>
    <li>ISP2_PROMISED_UP=advertisedInternetUploadSpeedForBackupISP</li>
    <li>ISP2_PROMISED_DOWN=advertisedInternetDownloadSpeedForBackupISP</li>
  </ul>
  <li>That's all you need to do for now.😉</li>
</ol>
<p>Simply put, as long as the internet performance is better than the advertised/promised bandwidth, the twitter method will not trigger.</p>
<hr>
<h3>Results</h3>
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-2/Snap1.jpg" alt="speedTestResults.jpg">
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-2/Snap2.jpg" alt="evidenceOfScrappedSpeedTestData.jpg">
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-2/Snap3.png" alt="complainTweet.jpg">

<hr>
<h3>Bugs</h3>
<p>None as at the time of this report.</p>
