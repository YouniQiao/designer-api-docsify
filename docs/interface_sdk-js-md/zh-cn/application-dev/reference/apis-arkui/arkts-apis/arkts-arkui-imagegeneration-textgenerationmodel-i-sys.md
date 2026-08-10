# TextGenerationModel（系统接口）

AI Text Model Abstract Interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface TextGenerationModel--><!--Device-imageGeneration-interface TextGenerationModel-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## cancelTextGeneration

```TypeScript
cancelTextGeneration(sessionId: int): void
```

Cancel AI text generation task.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TextGenerationModel-cancelTextGeneration(sessionId: int): void--><!--Device-TextGenerationModel-cancelTextGeneration(sessionId: int): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | int | 是 | The session id for cancel an AI text generation task. &lt;br&gt;Value: range: [0, +∞] |

## onComplain

```TypeScript
onComplain(sessionId: int, request: string, result: GenerateTextTaskResult): void
```

User use complaint menu to complain the result of an AI-generated text task.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TextGenerationModel-onComplain(sessionId: int, request: string, result: GenerateTextTaskResult): void--><!--Device-TextGenerationModel-onComplain(sessionId: int, request: string, result: GenerateTextTaskResult): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | int | 是 | The session id of AI text generation task. &lt;br&gt;Value: range: [0, +∞] |
| request | string | 是 | The origin request for AI-generated text task. |
| result | [GenerateTextTaskResult](arkts-arkui-imagegeneration-generatetexttaskresult-i-sys.md) | 是 | The result for AI-generated text task. |

## requestTextGeneration

```TypeScript
requestTextGeneration(sessionId: int, value: string,
      callback: Callback<GenerateTextTaskPartialResult>): void
```

Request AI text generation task to get the generated text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TextGenerationModel-requestTextGeneration(sessionId: int, value: string,      callback: Callback<GenerateTextTaskPartialResult>): void--><!--Device-TextGenerationModel-requestTextGeneration(sessionId: int, value: string,      callback: Callback<GenerateTextTaskPartialResult>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | int | 是 | The session id for requesting an AI text generation task. &lt;br&gt;Value: range: [0, +∞] |
| value | string | 是 | Parameters for requesting an AI text generation task. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GenerateTextTaskPartialResult&gt; | 是 | the callback used to return the GenerateTextTaskPartialResult. |

