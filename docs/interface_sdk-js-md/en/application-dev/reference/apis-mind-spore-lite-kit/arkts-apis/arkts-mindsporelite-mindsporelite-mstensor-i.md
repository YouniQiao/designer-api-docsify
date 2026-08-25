# MSTensor

Provides MSTensor definition

**Since:** 10

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

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

## setData

```TypeScript
setData(inputArray: ArrayBuffer): void
```

Set MSTensor data

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputArray | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000013 |

## dataSize

```TypeScript
dataSize: number
```

The data size of the tensor, the unit is byte.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## dtype

```TypeScript
dtype: DataType
```

The data type of the tensor.

**Type:** DataType

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## elementNum

```TypeScript
elementNum: number
```

The number of elements in the tensor.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## format

```TypeScript
format: Format
```

The format of the tensor.

**Type:** [Format](arkts-mindsporelite-mindsporelite-format-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## name

```TypeScript
name: string
```

The name of the tensor.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## shape

```TypeScript
shape: number[]
```

The shape of the tensor.

**Type:** number[]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite
