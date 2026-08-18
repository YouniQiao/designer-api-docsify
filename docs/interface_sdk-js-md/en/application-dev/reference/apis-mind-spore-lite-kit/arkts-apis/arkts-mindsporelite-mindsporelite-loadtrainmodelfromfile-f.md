# loadTrainModelFromFile

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## loadTrainModelFromFile

```TypeScript
function loadTrainModelFromFile(
    model: string,
    trainCfg?: TrainCfg,
    context?: Context): Promise<Model>
```

Load train model from file

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadTrainModelFromFile(    model: string,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadTrainModelFromFile(    model: string,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model file path |
| trainCfg | [TrainCfg](arkts-mindsporelite-mindsporelite-traincfg-i.md) | No | model train configuration |
| context | Context | No | model build context |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | the promise of the built model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000009 | Failed to create native training model from path. Possible causes: 1. The model file is incorrect; 2. The training configuration is incorrect. |
| 1000008 | Invalid model path in training. Possible causes: 1. The model path is null; 2. The model path does not exist. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect. |

**Examples**

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

