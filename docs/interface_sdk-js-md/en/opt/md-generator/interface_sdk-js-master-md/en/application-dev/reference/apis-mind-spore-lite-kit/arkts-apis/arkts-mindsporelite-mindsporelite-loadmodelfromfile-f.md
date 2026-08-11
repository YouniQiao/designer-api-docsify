# loadModelFromFile

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context?: Context): Promise<Model>
```

Create a Model instance from file path

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Model&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000003 |
| 1000002 |
| 1000001 |
| 1000000 |

## Examples

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
  }
}).catch((error: Error) => {
  console.error(`Failed to load model from file. Model file: ${modelFile}, Error: ${error.message}`);
});
```


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000003 |
| 1000002 |
| 1000001 |
| 1000000 |

## Examples

```TypeScript
let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
  }
})
```


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000003 |
| 1000002 |
| 1000001 |
| 1000000 |

## Examples

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Context: ${JSON.stringify(context)}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, Context: ${JSON.stringify(context)}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
  }
})
```
