# Typescript commands

- tsc --init -> Creates a tsconfig.json file to manage the whole project
- tsc -> When tsconfig.json is created, this command compiles the entire project
- tsc -w -> The -w flag means watch mode, so it will keep running and updating when you do changes to the project
- "exclude": [
    "**/*.dev.ts"
]
- ts automatically exclude node_modules to faster the compilation, since this files are big.
- "include": [
    "app.ts"
]
- Include will only include the specified files, you can also set folders

- OutDir for generated js files

- rootDir for my source ts files

- removeComments for removing comments in the compiled js files