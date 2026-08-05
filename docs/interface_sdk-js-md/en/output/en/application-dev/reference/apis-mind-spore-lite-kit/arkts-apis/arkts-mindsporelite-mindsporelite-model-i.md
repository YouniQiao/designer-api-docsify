# Model

Provides manages model function. Including get inputs, predict ,resize.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-mindSporeLite-interface Model--><!--Device-mindSporeLite-interface Model-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## exportModel

```TypeScript
exportModel(
      modelFile: string,
      quantizationType?: QuantizationType,
      exportInferenceOnly?: boolean,
      outputTensorName?: string[]): boolean
```

Export train model to file

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-exportModel(      modelFile: string,      quantizationType?: QuantizationType,      exportInferenceOnly?: boolean,      outputTensorName?: string[]): boolean--><!--Device-Model-exportModel(      modelFile: string,      quantizationType?: QuantizationType,      exportInferenceOnly?: boolean,      outputTensorName?: string[]): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modelFile | string | Yes | model file path. |
| quantizationType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the quantization type, default NO\_\_\_ESCAPED\_UNDERSCORE\_\_\_QUANT. |
| exportInferenceOnly | boolean | No | whether to export a inference only model, default true. |
| outputTensorName | string[] | No | the set of name of output tensor the exported inference model, |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - the boolean result if the operation is successful |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
let newPath = '/newpath/to';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  let ret = mindSporeLiteModel.exportModel(newPath + "/new_model.ms", mindSporeLite.QuantizationType.NO_QUANT, true);
  if (ret == false) {
    console.error('MS_LITE exportModel failed.')
  }
})
```

## exportWeightsCollaborateWithMicro

```TypeScript
exportWeightsCollaborateWithMicro(
      weightFile: string,
      isInference?: boolean,
      enableFp16?: boolean,
      changeableWeightsName?: string[]): boolean
```

Export model's weights, which can be used in micro only. Only valid for Lite Train

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-exportWeightsCollaborateWithMicro(      weightFile: string,      isInference?: boolean,      enableFp16?: boolean,      changeableWeightsName?: string[]): boolean--><!--Device-Model-exportWeightsCollaborateWithMicro(      weightFile: string,      isInference?: boolean,      enableFp16?: boolean,      changeableWeightsName?: string[]): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| weightFile | string | Yes | weight file path |
| isInference | boolean | No | whether to export weights from inference model, only support this is \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_for now, default true |
| enableFp16 | boolean | No | float-weight is whether to be saved in float16 format, default false |
| changeableWeightsName | string[] | No | changeable weights name |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean result if the operation is successful |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
let microWeight = '/path/to/xxx.bin';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let ret = mindSporeLiteModel.exportWeightsCollaborateWithMicro(microWeight);
  if (ret == false) {
    console.error('MSLITE exportWeightsCollaborateWithMicro failed.')
  }
})
```

## getInputs

```TypeScript
getInputs(): MSTensor[]
```

Get model input tensors.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-getInputs(): MSTensor[]--><!--Device-Model-getInputs(): MSTensor[]-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] | the MSTensor array of the inputs. |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

## getWeights

```TypeScript
getWeights(): MSTensor[]
```

Obtain all weights of the model

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-getWeights(): MSTensor[]--><!--Device-Model-getWeights(): MSTensor[]-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] | the weight tensors of the model |

**Example**

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        const weights = mindSporeLiteModel.getWeights();
        for (let i = 0; i < weights.length; i++) {
          let printStr = weights[i].name + ", ";
          printStr += weights[i].shape + ", ";
          printStr += weights[i].dtype + ", ";
          printStr += weights[i].dataSize + ", ";
          printStr += weights[i].getData();
          console.info("MS_LITE weights: ", printStr);
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## predict

```TypeScript
predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void
```

Infer model

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void--><!--Device-Model-predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | indicates the MSTensor array of the inputs. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;MSTensor[]&gt; | Yes | the callback of MSTensor array. |

**Example**

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile: string = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();

    modelInputs[0].setData(inputBuffer);
    mindSporeLiteModel.predict(modelInputs, (mindSporeLiteTensor: mindSporeLite.MSTensor[]) => {
      let output = new Float32Array(mindSporeLiteTensor[0].getData());
      for (let i = 0; i < output.length; i++) {
        console.info('MS_LITE_LOG: ' + output[i].toString());
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## predict

```TypeScript
predict(inputs: MSTensor[]): Promise<MSTensor[]>
```

Infer model

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-predict(inputs: MSTensor[]): Promise<MSTensor[]>--><!--Device-Model-predict(inputs: MSTensor[]): Promise<MSTensor[]>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | indicates the MSTensor array of the inputs. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MSTensor[]&gt; | the promise returned by the function. |

**Example**

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
    modelInputs[0].setData(inputBuffer);
    mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor: mindSporeLite.MSTensor[]) => {
      let output = new Float32Array(mindSporeLiteTensor[0].getData());
      for (let i = 0; i < output.length; i++) {
        console.info(output[i].toString());
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## resize

ArkTS-Dyn:
```TypeScript
resize(inputs: MSTensor[], dims: Array<Array<number>>): boolean
```

ArkTS-Sta:
```TypeScript
resize(inputs: MSTensor[], dims: Array<Array<int>>): boolean
```

resize model input

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-resize(inputs: MSTensor[], dims: Array<Array<int>>): boolean--><!--Device-Model-resize(inputs: MSTensor[], dims: Array<Array<int>>): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | indicates the MSTensor array of the inputs. |
| dims | ArkTS-Dyn: Array&lt;Array&lt;number&gt;&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Array&lt;Array&lt;int&gt;&gt; | Yes | indicates the target new shape array |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean result if the resize operation is successful |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  let new_dim = new Array([1, 32, 32, 1]);
  mindSporeLiteModel.resize(modelInputs, new_dim);
})
```

## runStep

```TypeScript
runStep(inputs: MSTensor[]): boolean
```

Train model by step

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-runStep(inputs: MSTensor[]): boolean--><!--Device-Model-runStep(inputs: MSTensor[]): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | indicates the MSTensor array of the inputs. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean result if the runStep operation is successful |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  const modelInputs = mindSporeLiteModel.getInputs();
  let ret = mindSporeLiteModel.runStep(modelInputs);
  if (ret == false) {
    console.error('MS_LITE_LOG: runStep failed.')
  }
})
```

## setupVirtualBatch

ArkTS-Dyn:
```TypeScript
setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean
```

ArkTS-Sta:
```TypeScript
setupVirtualBatch(virtualBatchMultiplier: int, lr: double, momentum: double): boolean
```

Setup training with virtual batches

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-setupVirtualBatch(virtualBatchMultiplier: int, lr: double, momentum: double): boolean--><!--Device-Model-setupVirtualBatch(virtualBatchMultiplier: int, lr: double, momentum: double): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| virtualBatchMultiplier | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | virtual batch multiplier, use any number < 1 to disable |
| lr | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | learning rate to use for virtual batch, -1 for internal configuration |
| momentum | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | batch norm momentum to use for virtual batch, -1 for internal configuration |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean result if the operation is successful |

**Example**

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        let ret = mindSporeLiteModel.setupVirtualBatch(2, -1, -1);
        if (ret == false) {
          console.error('MS_LITE setupVirtualBatch failed.')
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## updateWeights

```TypeScript
updateWeights(weights: MSTensor[]): boolean
```

Update weights of the model

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-updateWeights(weights: MSTensor[]): boolean--><!--Device-Model-updateWeights(weights: MSTensor[]): boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| weights | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | indicates the MSTensor array of the inputs |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the boolean result if updating weights operation is successful |

**Example**

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        const weights = mindSporeLiteModel.getWeights();
        let ret = mindSporeLiteModel.updateWeights(weights);
        if (ret == false) {
          console.error('MS_LITE_LOG: updateWeights failed.')
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## learningRate

```TypeScript
learningRate?: double
```

The learning rate of the training model

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-learningRate?: double--><!--Device-Model-learningRate?: double-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## trainMode

```TypeScript
trainMode?: boolean
```

The running mode of the model

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Model-trainMode?: boolean--><!--Device-Model-trainMode?: boolean-End-->

**System capability:** SystemCapability.AI.MindSporeLite

