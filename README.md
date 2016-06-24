# vcdat
vCDAT 2.0

# Front-end
<img src=http://js.devexpress.com/Content/Images/features/html5-css-javascript-logos.png height="120px">
<img src=http://red-badger.com/blog/wp-content/uploads/2015/04/react-logo-1000-transparent.png height="150px">
<img src=https://raw.githubusercontent.com/reactjs/redux/master/logo/logo.png height="130px">

## Installation
1. Install [node](https://docs.npmjs.com/getting-started/installing-node). Homebrew can be used for this step.

2. Clone repo

3. `cd` into the Front-end directory and run `npm install`.

4. Commands:  
 - To run local server on port 3000: `npm run server`   
 - To build bundle.js file: `npm run build`


Tips:  
* `$(npm bin)` points you to the bin folder in the node_modules/ directory allowing you easier access to commands from npm modules without global installation.  
Example:


    > $(npm bin)/webpack --watch

### Naming Convention
* newfolder
* NewFile
* NewClass
* newFunction
* new_variable  

Filenames should correspond to the class exported by default.  
Example: `import CoolClass from './cool/CoolClass.js'`
