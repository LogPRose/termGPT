<h1>Hello, welcome to termGPT!</h1>
<p> I've found myself frequently tabbing between my terminal editor, <a href="https://github.com/LogPRose/nvim">NVIM</a> and my browser in order to use chatGPT for help with syntax or boilerplate code!
I decided to make a python script that would use the chatGPT API in order to access chatGPT with a split terminal window</p>
<p> This JSON response returned will be output to the terminal itself but will also be written into a log-file for ease of yanking</p>
<p> For ease of setup I will leave all of the code available, all you will need to do is setup your own .env file with your keys!</p>

<ul>
    <div>
        <p> First run the command </p>
        <div class="Boxed"> pip install openai </div> 
    </div>
    <p>Next you'll want to head over to OpenAI and sign in to your account, then proceed to the dashboard in order to generate your API key for the next step</p>
    <p>In the template .env file you'll want to set OPEN_API_KEY to the key you generated in the last step. </p>
    <div>
        <p>After your API key has been setup you can proceed to run the command</p>
        <div class="Boxed"> python3 termGPT.py</div>
        <p>You can now start typing away!</p>
        <p>You can safely exit by using c-C</p>
    </div>
</ul>


<h2> Additional Resources </h2>

<ul>
    <a href="https://platform.openai.com/docs/api-reference/introduction">OpenAI Docs</a>
    <a href="https://pip.pypa.io/en/stable/">pip Docs</a>
</ul>
