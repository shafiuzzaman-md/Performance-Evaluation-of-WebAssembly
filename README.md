# Compiling C module to WebAssembly
Prerequisites: A program is needed that can compile C source codes to WebAssembly module. For this, we will use Emscripten’s emcc compiler. Get the Emscripten SDK, using these instructions: https://emscripten.org/docs/getting_started/downloads.html

Use following command to compile the C file. 
emcc hello.c -s WASM=1 -o hello.html

-s WASM=1 — Specifies the wasm output.
-o hello.html — Specifies it will generate an HTML page to run our code

After running the command following fle will be generated:
hello.wasm - The binary wasm module code
hello.js - A JavaScript file containing glue code to translate between the native C functions, and JavaScript/wasm
hello.html - An HTML file to load, compile, and instantiate your wasm code, and display its output in the browser

# Hosting the app with a web server
We will need a web server to display the HTML page in a web browser. For this, we may use the http.server module from Python 3 to host all files in the current directory on port 8000 using the following command:
python -m http.server 8000
