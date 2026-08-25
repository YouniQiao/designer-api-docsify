# Model

Provides manages model function. Including get inputs, predict ,resize.

**Since:** 10

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

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

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modelFile | string | Yes |
| quantizationType | [QuantizationType](arkts-mindsporelite-mindsporelite-quantizationtype-e.md) | No |
| exportInferenceOnly | boolean | No |
| outputTensorName | string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| weightFile | string | Yes |
| isInference | boolean | No |
| enableFp16 | boolean | No |
| changeableWeightsName | string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getInputs

```TypeScript
getInputs(): MSTensor[]
```

Get model input tensors.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] |

## getWeights

```TypeScript
getWeights(): MSTensor[]
```

Obtain all weights of the model

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] |

## predict

```TypeScript
predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void
```

Infer model

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-shader-i.md) | [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[]&gt; | Yes |

## predict

```TypeScript
predict(inputs: MSTensor[]): Promise<MSTensor[]>
```

Infer model

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-shader-i.md) | [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[]&gt; |

## resize

```TypeScript
resize(inputs: MSTensor[], dims: Array<Array<number>>): boolean
```

resize model input

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-shader-i.md) | [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] | Yes |
| dims | Array & lt;Array & lt;number & gt; & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## runStep

```TypeScript
runStep(inputs: MSTensor[]): boolean
```

Train model by step

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-shader-i.md) | [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setupVirtualBatch

```TypeScript
setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean
```

Setup training with virtual batches

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| virtualBatchMultiplier | number | Yes |
| lr | number | Yes |
| momentum | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## updateWeights

```TypeScript
updateWeights(weights: MSTensor[]): boolean
```

Update weights of the model

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| weights | [MSTensor](arkts-mindsporelite-mindsporelite-mstensor-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## learningRate

```TypeScript
learningRate?: number
```

The learning rate of the training model

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## trainMode

```TypeScript
trainMode?: boolean
```

The running mode of the model

**Type:** boolean

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite
