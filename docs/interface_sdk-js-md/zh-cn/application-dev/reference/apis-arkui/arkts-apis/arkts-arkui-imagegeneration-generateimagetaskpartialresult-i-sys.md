# GenerateImageTaskPartialResult（系统接口）

Configuration stream result for AI-generated image tasks.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GenerateImageTaskPartialResult--><!--Device-imageGeneration-interface GenerateImageTaskPartialResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## imageData

```TypeScript
imageData?: string
```

image data of the image corresponding to AI-generated image task, available in partial result.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskPartialResult-imageData?: string--><!--Device-GenerateImageTaskPartialResult-imageData?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## imageIndex

```TypeScript
imageIndex?: int
```

Sequence number of the image corresponding to AI-generated image task, available in partial and partial error result.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskPartialResult-imageIndex?: int--><!--Device-GenerateImageTaskPartialResult-imageIndex?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## partialFail

```TypeScript
partialFail?: BusinessError
```

Information of the partial error corresponding to AI-generated image task, available in partial error result.

**类型：** [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskPartialResult-partialFail?: BusinessError--><!--Device-GenerateImageTaskPartialResult-partialFail?: BusinessError-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## totalCount

```TypeScript
totalCount?: int
```

Total number of the image corresponding to AI-generated image task, available in completed result.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskPartialResult-totalCount?: int--><!--Device-GenerateImageTaskPartialResult-totalCount?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: PartialResultType
```

The type information used for AI-generated image task.

**类型：** [PartialResultType](arkts-arkui-imagegeneration-partialresulttype-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskPartialResult-type: PartialResultType--><!--Device-GenerateImageTaskPartialResult-type: PartialResultType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

