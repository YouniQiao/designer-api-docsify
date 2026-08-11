# MSTensor

Provides MSTensor definition

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-mindSporeLite-interface MSTensor--><!--Device-mindSporeLite-interface MSTensor-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## getData

```TypeScript
getData(): ArrayBuffer
```

Get MSTensor data

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-getData(): ArrayBuffer--><!--Device-MSTensor-getData(): ArrayBuffer-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | the data of tensor |

## Examples

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

## setData

```TypeScript
setData(inputArray: ArrayBuffer): void
```

Set MSTensor data

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-setData(inputArray: ArrayBuffer): void--><!--Device-MSTensor-setData(inputArray: ArrayBuffer): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputArray | ArrayBuffer | Yes | indicates the buffer of tensor |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000013 | Failed to set MSTensor data. Possible causes: 1. The input array buffer size is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

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
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

## dataSize

```TypeScript
dataSize: int
```

The data size of the tensor, the unit is byte.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-dataSize: int--><!--Device-MSTensor-dataSize: int-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## dtype

```TypeScript
dtype: DataType
```

The data type of the tensor.

**Type:** [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-dtype: DataType--><!--Device-MSTensor-dtype: DataType-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## elementNum

```TypeScript
elementNum: int
```

The number of elements in the tensor.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-elementNum: int--><!--Device-MSTensor-elementNum: int-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## format

```TypeScript
format: Format
```

The format of the tensor.

**Type:** [Format](arkts-mindsporelite-mindsporelite-format-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-format: Format--><!--Device-MSTensor-format: Format-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## name

```TypeScript
name: string
```

The name of the tensor.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-name: string--><!--Device-MSTensor-name: string-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## shape

```TypeScript
shape: int[]
```

The shape of the tensor.

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MSTensor-shape: int[]--><!--Device-MSTensor-shape: int[]-End-->

**System capability:** SystemCapability.AI.MindSporeLite

