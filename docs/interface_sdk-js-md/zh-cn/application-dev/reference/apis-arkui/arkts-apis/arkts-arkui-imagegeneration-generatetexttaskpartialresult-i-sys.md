# GenerateTextTaskPartialResult（系统接口）

Configuration stream result for AI-generated text tasks.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GenerateTextTaskPartialResult--><!--Device-imageGeneration-interface GenerateTextTaskPartialResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## content

```TypeScript
content?: string
```

Final data in AI-generated text task, available in partial result.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateTextTaskPartialResult-content?: string--><!--Device-GenerateTextTaskPartialResult-content?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## partialFail

```TypeScript
partialFail?: BusinessError
```

Information of the partial error corresponding to AI-generated text task, available in partial error result.

**类型：** [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateTextTaskPartialResult-partialFail?: BusinessError--><!--Device-GenerateTextTaskPartialResult-partialFail?: BusinessError-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## reasoningContent

```TypeScript
reasoningContent?: string
```

Think information in AI-generated text task, available in partial result.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateTextTaskPartialResult-reasoningContent?: string--><!--Device-GenerateTextTaskPartialResult-reasoningContent?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: PartialResultType
```

The type information used for AI-generated text task.

**类型：** [PartialResultType](arkts-arkui-imagegeneration-partialresulttype-e-sys.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateTextTaskPartialResult-type: PartialResultType--><!--Device-GenerateTextTaskPartialResult-type: PartialResultType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

