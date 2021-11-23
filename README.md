# Compiling C module to WebAssembly
Prerequisites: A program is needed that can compile C source codes to WebAssembly module. For this, we will use Emscripten’s emcc compiler. Get the Emscripten SDK, using these instructions: https://emscripten.org/docs/getting_started/downloads.html

Use following command to compile the C file. 

**emcc hello.c -s WASM=1 -o hello.html**

emcc is the program you call to compile your C code
-s WASM=1 — Specifies the wasm output.
-o hello.html — Specifies it will generate an HTML page to run our code

After running the command following fle will be generated:
hello.wasm - The binary wasm module code
hello.js - A JavaScript file containing glue code to translate between the native C functions, and JavaScript/wasm. It is needed to allow JavaScript to call and "communicate" with WASM compiled code. Emscripten generates this automatically to run WASM modules.
hello.html - An HTML file to load, compile, and instantiate your wasm code, and display its output in the browser

You will need a web server to display the HTML page in a web browser. For this, we may use the http.server module from Python 3 to host all files in the current directory on port 8000 using the following command:

**python -m http.server 8000**

# Compiling C to WebAssembly without Emscripten

Although compiling a complex C application to WebAssembly using Emscripten is an effective approach, it comes at the cost of complexity. Because it produces a lot of JavaScript glue code and requires an external tool chain. We can compile C functions to WebAssembly without Emscripten using LLVM only.

*LLVM*
LLVM is a compiler framework that has a front-end compiler to compile the source code to an intermediate representation (IR). Then a back-end compiler translates the IR to the host’s machine code.

If you are on MacOS, you have to install [homebrew](http://google.com) first. Use following commands to install LLVM:

brew install llvm

brew link --force llvm

llc --version (Check the installation)

Turning C code into IR

add.c file contains a function. LLVM front-end compiler clang can compile it to IR using following command:

clang --target=wasm32 -emit-llvm -c -S add.c

A new file named add.II will be created with the intermadiate representation of C source code. 


# Memory

WebAssembly works in a protected environment (sandbox) and cannot directly access the memory out of it. It uses a JavaScript typed array (a single contagious address space) as its memory model (called as linear memory). When the JavaScript "glue code" is loaded, the array representing the WASM memory is automatically instantiated. 

This can be viewed through browser console. Type following command in the console:

**Module.HEAP8**

You can see following image like output.
![image](https://user-images.githubusercontent.com/10768241/140510614-21b53344-05bd-46e7-9ba7-ba3ff5da8141.png)

*HEAP8* shows memory as a composition of 8-bit signed integers. Memory can also be viewed as other memory model, such as, 16-bit signed memory (*HEAP1*), 32-bit unsigned memory (*HEAPU32*) or 64-bit float memory (*HEAPF64*). Though the array always contains the data in same manner, we can look at it in different ways in order to work with different data types. WASM memory is an expandable array of bytes that JavaScript and Wasm can synchronously read and modify.

# Resources

https://github.com/zandaqo/iswasmfast

https://github.com/plasma-umass/browsix-emscripten

# Papers

Not So Fast: Analyzing the Performance of WebAssembly vs. Native Code
https://www.usenix.org/conference/atc19/presentation/jangda



