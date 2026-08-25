# TextGenerationModel (System API)

AI Text Model Abstract Interface.@interface TextGenerationModel

**Since:** 23

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## cancelTextGeneration

```TypeScript
cancelTextGeneration(sessionId: number): void
```

Cancel AI text generation task.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |

## onComplain

```TypeScript
onComplain(sessionId: number, request: string, result: GenerateTextTaskResult): void
```

User use complaint menu to complain the result of an AI-generated text task.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| request | string | Yes |
| result | [GenerateTextTaskResult](arkts-arkui-imagegeneration-generatetexttaskresult-i-sys.md) | Yes |

## requestTextGeneration

```TypeScript
requestTextGeneration(sessionId: number, value: string,
      callback: Callback<GenerateTextTaskPartialResult>): void
```

Request AI text generation task to get the generated text.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| value | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GenerateTextTaskPartialResult](arkts-arkui-imagegeneration-generatetexttaskpartialresult-i-sys.md)&gt; | Yes |
