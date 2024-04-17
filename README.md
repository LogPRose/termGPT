# Hello, welcome to termGPT!

I've found myself frequently tabbing between my terminal editor, [NVIM](https://github.com/LogPRose/nvim), and my browser in order to use chatGPT for help with syntax or boilerplate code! I decided to make a Python script that would use the chatGPT API in order to access chatGPT with a split terminal window.

This JSON response returned will be output to the terminal itself but will also be written into a log-file for ease of yanking.

For ease of setup, I will leave all of the code available. All you will need to do is set up your own `.env` file with your keys!

Run the command:
   > pip install openai

Next, you'll want to head over to OpenAI and sign in to your account, then proceed to the dashboard in order to generate your API key for the next step.

In the template `.env` file, you'll want to set `OPEN_API_KEY` to the key you generated in the last step.

After your API key has been set up, you can proceed to run the command:
   > python3 termGPT.py

   There are some options of boot up to configure your experience:
    * Mode - You can use a contiguous file for successive prompts or you can have the logfile be replaced on each prompt
    * File type - This describes what type of file you would like the logfile to be in for the sake of your LSP
   You can now start typing away! You can safely exit by using `Ctrl+C`.

## Additional Resources

* [OpenAI Docs](https://platform.openai.com/docs/api-reference/introduction)
* [pip Docs](https://pip.pypa.io/en/stable/)

