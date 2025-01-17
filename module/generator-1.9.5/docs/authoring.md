# Authoring templates

The AsyncAPI generator has been built with extensibility in mind. The package uses a set of default templates to let you generate documentation and code. However, you can create and use your own templates. In this section, you learn how to create your own one.

To work on a template, you need an AsyncAPI specification file that you can use for testing. For this purpose, you can use [this](../test/docs/dummy.yml) dummy file as it's purpose is to cover as many features of AsyncAPI as possible. Do not copy this file to your template but use it directly from this repo like this: `ag https://raw.githubusercontent.com/asyncapi/generator/master/test/docs/dummy.yml ./your-template`

> In case you find some features missing or other possible improvements in the dummy file, suggest changes. The goal is to build a file that all templates can use and check their specification features coverage.

## Common assumptions

1. A template is a directory in your file system.
1. The template can have own dependencies. Just create `package.json` for the template. The generator makes sure to trigger the installation of dependencies.
1. Templates can be configured. Configuration must be stored in the `package.json` file under custom `generator` property. [Read more about the configuration file](#configuration-file).
1. The template engine can be either [React](#react) (recommended) or [Nunjucks](#nunjucks) (default). This can be controlled with the `renderer` property in the [template configuration](#template-configuration).
1. Templates may contain `hooks` that are functions invoked during specific moment of the generation. In the template, they must be stored in the `hooks` directory under the template directory. They can also be stored in other modules and external libraries and configured inside the template [Read more about hooks](#hooks).
1. There are parameters with special meaning. [Read more about special parameters](#special-parameters).

## Special file names

We use NPM behind the scenes to download and install the templates. Since NPM will not fetch files like `.gitignore`, you should name them differently. Luckily, the Generator will take care of renaming them back for you. The following is a table of the special file names:

|Special file name|Output file name|
|---|---|
|`{.gitignore}`|`.gitignore`|
|`{.npmignore}`|`.npmignore`|

## File templates

It is possible to generate files for each specific object in your AsyncAPI documentation. For example, you can specify a filename like `$$channel$$.js` to generate a file for each channel defined in your AsyncAPI. The following file-template names and extra variables in them are available:

   - `$$channel$$`, within the template-file you have access to two variables [`channel`](https://github.com/asyncapi/parser-js/blob/master/API.md#Channel) and [`channelName`](https://github.com/asyncapi/parser-js/blob/master/API.md#AsyncAPIDocument+channels). Where `channel` contains the current channel being rendered.
   - `$$message$$`, within the template-file you have access to two variables [`message`](https://github.com/asyncapi/parser-js/blob/master/API.md#Message) and [`messageName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Message+uid). Where `message` contains the current message being rendered.
   - `$$schema$$`, within the template-file you have access to two variables [`schema`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema) and [`schemaName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema+uid). Where `schema` contains the current schema being rendered. Only schemas from [Components object](https://www.asyncapi.com/docs/specifications/2.0.0/#a-name-componentsobject-a-components-object) are used. 
   - `$$everySchema$$`, within the template-file you have access to two variables [`schema`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema) and [`schemaName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema+uid). Where `schema` contains the current schema being rendered. Every [Schema object](https://www.asyncapi.com/docs/specifications/2.0.0/#schemaObject) from the entire AsyncAPI file is used.
   - `$$objectSchema$$`, within the template-file you have access to two variables [`schema`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema) and [`schemaName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Schema+uid). Where `schema` contains the current schema being rendered. All the [Schema objects](https://www.asyncapi.com/docs/specifications/2.0.0/#schemaObject) with type object is used.
   - `$$parameter$$`, within the template-file you have access to two variables [`parameter`](https://github.com/asyncapi/parser-js/blob/master/API.md#ChannelParameter) and [`parameterName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Channel+parameters). Where `parameter` contains the current parameter being rendered.
   - `$$securityScheme$$`, within the template-file you have access to two variables [`securityScheme`](https://github.com/asyncapi/parser-js/blob/master/API.md#SecurityScheme) and [`securitySchemeName`](https://github.com/asyncapi/parser-js/blob/master/API.md#Components+securitySchemes). Where `securityScheme` contains the current security scheme being rendered.

The file name will be equal to `*Name` variable.

### Example

The file name is `$$schema$$.txt`, the content of this file is:
```
Schema name is '{{schemaName}}' and properties are:
{% for propName, prop in schema.properties() %}
- {{prop.uid()}}
{% endfor %}
```

With following AsyncAPI:
```
components:
  schemas: 
    peoplePayload:
      type: object
      properties:
        event:
          $ref: "#/components/schemas/people"
    people:
      type: object
      properties:
        id:
          type: integer
```

The generator creates two files `peoplePayload.txt` and `people.txt` with the following content:
```
Schema name is 'peoplePayload' and properties are:
- people
```

and
```
Schema name is 'people' and properties are:
- id
```

### React

The above way of rendering **file templates** works for both `nunjucks` and `react` render engines, but `react` also has another, more generic way to render multiple files. It is enough to return an array of `File` components in the rendering component. See the following example:

```tsx
export default function({ asyncapi }) {
  return [
    <File name={`file1.html`}>Content</File>,
    <File name={`file2.html`}>Content</File>
  ]
}
```

## Hooks

Hooks are functions called by the generator on a specific moment in the generation process. Hooks can be anonymous functions but you can also add function names. These hooks can have arguments provided to them or being expected to return a value.
The following types of hooks are currently supported:

|Hook type|Description| Return type | Arguments 
|---|---|---|---|
| `generate:before` | Called after registration of all filters and before generator starts processing of the template. | void : Nothing is expected to be returned. | [The generator instance](https://github.com/asyncapi/generator/blob/master/docs/api.md)
| `generate:after` | Called at the very end of the generation. | void : Nothing is expected to be returned. | [The generator instance](https://github.com/asyncapi/generator/blob/master/docs/api.md)
| `setFileTemplateName ` | Called right before saving a new file generated by [file template](https://github.com/asyncapi/generator/blob/master/docs/authoring.md#file-templates). | string : a new filename for the generator to use for the file template. | [The generator instance](https://github.com/asyncapi/generator/blob/master/docs/api.md) and object in the form of `{ "originalFilename" : string }`

The generator parses:
- All the files in the `.hooks` directory inside the template.
- All modules listed in the template configuration and triggers only hooks that names were added to the config. You can use the official AsyncAPI [hooks library](https://github.com/asyncapi/generator-hooks). To learn how to add hooks to configuration [read more about the configuration file](#configuration-file).

### Examples

> Some of examples have name of hook functions provided and some not. Keep in mind that hook functions kept in template in default location do not require a name. Name is required only if you keep hooks in non default location or in a separate library, because such hooks need to be explicitly configured in the configuration file. For more details on hooks configuration [read more about the configuration file](#configuration-file).

Most basic module with hooks looke like this:
```js
module.exports = {
  'generate:after': generator => console.log('This runs after generation is complete')
}
```

Below you have an example Hook that after generation creates an AsyncAPI file.

```js
const fs = require('fs');
const path = require('path');

module.exports = {
  'generate:after': generator => {
    const asyncapi = generator.originalAsyncAPI;
    let extension;

    try {
      JSON.parse(asyncapi);
      extension = 'json';
    } catch (e) {
      extension = 'yaml';
    }

    fs.writeFileSync(path.resolve(generator.targetDir, `asyncapi.${extension}`), asyncapi);
  }
};
```
And here an example Hook that before generation switches `publish` and `subscribe` operations for each channel.

```js
module.exports = {
  'generate:before': function switchOperations(generator) {
    const asyncapi = generator.asyncapi;
    for (let [key, value] of Object.entries(asyncapi.channels())) {
      let publish = value._json.publish;
      value._json.publish = value._json.subscribe;
      value._json.subscribe = publish;
      if (!value._json.subscribe) {
        delete value._json.subscribe;
      }
      if (!value._json.publish) {
        delete value._json.publish;
      }
    }
  };
};
```

Example hook for changing the filename of a template file. Replaces all '-' characters with '_'.
```js
module.exports = {
	'setFileTemplateName': (generator, hookArguments) => {
		const currentFilename = hookArguments.originalFilename ;
		return currentFilename.replace('-', '_')
	};
};
```

## Configuration File

The `generator` property from `package.json` file must contain a JSON object that may have the following information:

|Name|Type|Description|
|---|---|---|
|`renderer`| String | Its value can be either `react` or `nunjucks` (default).
|`supportedProtocols`| [String] | A list with all the protocols this template supports.
|`parameters`| Object[String, Object] | An object with all the parameters that can be passed when generating the template. When using the command line, it's done by indicating `--param name=value` or `-p name=value`.
|`parameters[param].description`| String | A user-friendly description about the parameter.
|`parameters[param].default`| Any | Default value of the parameter if not specified. Shouldn't be used for mandatory `required=true` parameters.
|`parameters[param].required`| Boolean | Whether the parameter is required or not.
|`conditionalFiles`| Object[String, Object] | An object containing all the file paths that should be conditionally rendered. Each key represents a file path and each value must be an object with the keys `subject` and `validation`. The file path should be relative to the `template` directory inside the template.
|`conditionalFiles[filePath].subject`| String | The `subject` is a [JMESPath](http://jmespath.org/) query to grab the value you want to apply the condition to. It queries an object with the whole AsyncAPI document and, when specified, the given server. The object looks like this: `{ asyncapi: { ... }, server: { ... } }`. If template supports `server` parameter, you can access server details like for example protocol this way: `server.protocol`. During validation with `conditionalFiles` only the server that template user selected is available in the specification file. For more information about `server` parameter [read about special parameters](#special-parameters).
|`conditionalFiles[filePath].validation`| Object | The `validation` is a JSON Schema Draft 07 object. This JSON Schema definition will be applied to the JSON value resulting from the `subject` query. If validation doesn't have errors, the condition is met, and therefore the given file will be rendered. Otherwise, the file is ignored. Check [JSON Schema Validation](https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6) document for a list of all possible validation keywords.
|`nonRenderableFiles`| [String] | A list of file paths or [globs](https://en.wikipedia.org/wiki/Glob_(programming)) that must be copied "as-is" to the target directory, i.e., without performing any rendering process. This is useful when you want to copy binary files.
|`generator`| [String] | A string representing the Generator version-range the template is compatible with. This value must follow the [semver](https://nodejs.dev/learn/semantic-versioning-using-npm) syntax. E.g., `>=1.0.0`, `>=1.0.0 <=2.0.0`, `~1.0.0`, `^1.0.0`, `1.0.0`, etc. [Read more about semver](https://docs.npmjs.com/about-semantic-versioning).
|`filters`| [String] | A list of modules containing functions that can be used as Nunjucks filters. In case of external modules, remember they need to be added as a dependency in `package.json` of your template.
|`hooks`| Object[String, String] or Object[String, Array[String]] | A list of modules containing hooks, except of the ones you keep locally in your template in default location. For each module you must specify exact name of the hook that should be used in the template. For single hook you can specify it as a string, for more you must pass an array of strings. In case of external modules, remember they need to be added as a dependency in `package.json` of your template.

### Example

```json
"generator":
{
  "renderer": "react",
  "supportedProtocols": ["amqp", "mqtt"],
  "parameters": {
    "server": {
      "description": "The server you want to use in the code.",
      "required": true
    },
    "dummyParameter": {
      "description": "Example of parameter with default value.",
      "default": "just a string",
      "required": false
    }
  },
  "conditionalFiles": {
    "path/to/file/that/is/relative/to/template/dir/test-amqp.js": {
      "subject": "server.protocol",
      "validation": {
        "const": "amqp"
      }
    },
    "path/to/file/that/is/relative/to/template/dir/support.html": {
      "subject": "info.contact",
        "validation": {
          "required": ["url"]
        }
    }
  },
  "nonRenderableFiles": [
    "src/api/middlewares/*.*",
    "lib/lib/config.js"
  ],
  "generator": "<2.0.0",
  "filters": [
    "@asyncapi/generator-filters"
  ],
  "hooks": {
    "@asyncapi/generator-hooks": "hookFunctionName"
  }
}
```

## Special parameters

There are some template parameters that have a special meaning:

|Name|Description|
|---|---|
|`server`| It is used to let the template know which server from the AsyncAPI specification file you want to use. In some cases, this may be required. For instance, when generating code that connects to a specific server. Use this parameter in case your template relies on users' information about what server from the specification file they want to use during generation. You also need this parameter if you want to use `server.protocol` notation within `conditionalFiles` configuration option. Once you decide to specify this parameter for your template, it is recommended you make it a mandatory parameter otherwise feature like `conditionalFiles` is not going to work if your users do not use this parameter obligatory.

## React

[React](https://reactjs.org) is the render engine that we strongly suggest you should use for any new templates. The only reason it is not the default render engine is to stay backward compatible.

* It enables the possiblity of [debugging](#debugging-react-template) your template (this is not possible with Nunjucks).
* It provides better error stack traces.
* Provides better support for separating code into more manageable chunks/components.
* The readability of the template is much better compared to Nunjucks syntax.
* Better tool support for development.
* Introduces testability of components which is not possible with Nunjucks.

When writing React templates you decide whether to use CommonJS, ES5, or ES6 modules since everything is bundled together before the rendering process takes over. We use our own React renderer which can be found in the [Generator React SDK](https://github.com/asyncapi/generator-react-sdk). 
There you can find information about how the renderer works or how we transpile your template files.

Your React template always require `@asyncapi/generator-react-sdk` as a dependency. `@asyncapi/generator-react-sdk` is required to access the `File` component which is required as a root component for a file to be rendered. Furthermore it provides some common components to make your development easier, like `Text` or `Indent`.

Let's consider a basic React template as the one below called `MyTemplate.js`:

```js
import { File, Text } from "@asyncapi/generator-react-sdk";

export default function({ asyncapi, params, originalAsyncAPI }) {
  return (
    <File name="asyncapi.md">
      <Text>Some text that should render as is</Text>
    </File>
  );
}
```

The exported default function returns a `File` component as a root component which the [Generator](https://github.com/asyncapi/generator) uses to figure out what file should be generated. In our case we overwrite the default functionality of saving the file as `MyTemplate.js` but instead use the filename `asyncapi.md`. It is then specified that we should render `Some text that should render as is\n` within that file. Notice the `\n` character at the end, this is something that is automatically added after the `Text` component. 

For further information about components, props etc. see the [Generator React SDK](https://github.com/asyncapi/generator-react-sdk)

### Common assumptions

1. Generator renders all files located in the `template` directory if they meet the following conditions:
    - `File` is the root component
    - The file is not in the list of `nonRenderableFiles` in the template configuration
1. New lines are automatically added after each `Text` component.
1. The props you have access to in rendering function is:
   - `asyncapi` that is a parsed spec file object. Read the [API](https://github.com/asyncapi/parser-js/blob/master/API.md#AsyncAPIDocument) of the Parser to understand to what structure you have access in this parameter.
   - `originalAsyncAPI` that is an original spec file before it is parsed. 
   - `params` that contains the parameters provided when generating.
1. All the file templates are supported where the variables are provided after the default props as listed above. 

### Debugging React template in VSCode

With React, it enables you to debug your templates. For Visual Studio Code, we have created a boilerplate [launch configuration](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) to enable debug in your template. Add the following launch configuration:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug template",
      "timeout": 10000,
      "sourceMaps": true,
      "args": [
        "./asyncapi.yml",
        "./template",
        "--output",
        "./output",
        "--install",
        "--force-write"
      ],
      "program": "ag"
    }
  ]
}
```

Now replace `./asyncapi.yml` with your document of choice. Replace `./template` with the path to your React template. You can now debug your template by adding any breakpoints you want and inspect your code.

## Nunjucks

[Nunjucks](https://mozilla.github.io/nunjucks) is the default render engine, however, we strongly recommend adopting the [React](#react) engine.

### Common assumptions

1. Templates may contain [Nunjucks filters or helper functions](https://mozilla.github.io/nunjucks/templating.html#builtin-filters). [Read more about filters](#filters).
1. Templates may contain `partials` (reusable chunks). They must be stored in the `.partials` directory under the template directory. [Read more about partials](#partials).
1. Templates may contain multiple files. Unless stated otherwise, all files will be rendered.
1. The default variables you have access to in any the template file are the following:
   - `asyncapi` that is a parsed spec file object. Read the [API](https://github.com/asyncapi/parser-js/blob/master/API.md#AsyncAPIDocument) of the Parser to understand to what structure you have access in this parameter.
   - `originalAsyncAPI` that is an original spec file before it is parsed. 
   - `params` that contains the parameters provided when generating.

### Partials

Files from the `.partials` directory do not end up with other generated files in the target directory. In this directory you should keep reusable templates chunks that you can [include](https://mozilla.github.io/nunjucks/templating.html#include) in your templates. You can also put there [macros](https://mozilla.github.io/nunjucks/templating.html#macro) to use them in templates, like in below example:

```html
{# tags.html #}
{% macro tags(tagList) %}
<div class="mt-4">
  {% for tag in tagList %}
    <span class="bg-grey-dark font-normal text-sm no-underline text-white rounded lowercase mr-2 px-2 py-1" title="{{tag.description()}}">{{tag.name()}}</span>
  {% endfor %}
</div>
{% endmacro %}

{# operations.html #}
{% from "./tags.html" import tags %}
{{ tags(operation.tags()) }}
```

### Filters

A filter is a helper function that you can create to perform complex tasks. They are JavaScript files that register one or many [Nunjuck filters](https://mozilla.github.io/nunjucks/api.html#custom-filters). The generator parses all the files in the `filters` directory. Functions exported from these files are registered as filters.

You can use the filter function in your template as in the following example:

```js
const {{ channelName | camelCase }} = '{{ channelName }}';
```

The generator also supports asynchronous filters. Asynchronous filters receive as last argument a callback to resume rendering. Asynchronous filters must be annotated with the `async` keyword. Make sure to call the callback with two arguments: `callback(err, res)`. `err` can be `null`. See the following example of how to use asynchronous filters:

```js
const filter = module.exports;

async function asyncCamelCase(str, callback) {
  try {
    const result = // logic for camel casing str
    callback(null, result);
  } catch (error) {
    callback(error);
  }
}
filter.renderAsyncContent = renderAsyncContent;

// using in template
{{ channelName | asyncCamelCase }}
```

Unfornatelly, if you need to use Promise, filter still must be annotated with the `async` keyword:

```js
async function asyncCamelCase(str, callback) {
  return new Promise((resolve, reject) => {
    // logic with callback
  });
}
```

In case you have more than one template and want to reuse filters, you can put them in a single library. You can configure such a library in the template configuration under `filters` property. You can also use the official AsyncAPI [filters library](https://github.com/asyncapi/generator-filters). To learn how to add such filters to configuration [read more about the configuration file](#configuration-file).

## TypeScript support 

The AsyncAPI generator has TypeScript support for [hooks](#hooks) and Nunjucks's [filters](#filters). Assumptions:

- Installing the `typescript` package and creating the` tsconfig.json` file isn't necessary.
- Source code of the hook/filter must have `.ts` extension.
- Each package related to the typings for TypeScript like `@types/node` must be installed in the template under `dependencies` array. This is because the Generator transpiles the TypeScript code on-the-fly while rendering the template, and cannot use packages under `devDependencies`.
- Each template should have `@types/node` package installed to enable support for typings for Node.
