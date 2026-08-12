# ImageGenerationModel (System API)

AI Image Model Abstract Interface.

**Since:** 23

<!--Device-imageGeneration-interface ImageGenerationModel--><!--Device-imageGeneration-interface ImageGenerationModel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { imageGeneration } from '@kit.ArkUI';
```

## cancelImageGeneration

```TypeScript
cancelImageGeneration(sessionId: number): void
```

Cancel AI image generation task.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-cancelImageGeneration(sessionId: int): void--><!--Device-ImageGenerationModel-cancelImageGeneration(sessionId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |

## getModelSupportStyles

```TypeScript
getModelSupportStyles(): Array<ImageStyle>
```

Get the types of image styles supported by the AI model.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-getModelSupportStyles(): Array<ImageStyle>--><!--Device-ImageGenerationModel-getModelSupportStyles(): Array<ImageStyle>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[ImageStyle](arkts-arkui-imagegeneration-imagestyle-i-sys.md)&gt; |

## onComplain

```TypeScript
onComplain(sessionId: number, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void
```

User use complaint menu to complain the result of an AI-generated image task.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-onComplain(sessionId: int, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void--><!--Device-ImageGenerationModel-onComplain(sessionId: int, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| request | [GenerateImageTaskParams](arkts-arkui-imagegeneration-generateimagetaskparams-i-sys.md) | Yes |
| result | [GenerateImageTaskResult](arkts-arkui-imagegeneration-generateimagetaskresult-i-sys.md) | Yes |

## requestImageGeneration

```TypeScript
requestImageGeneration(sessionId: number, params: GenerateImageTaskParams,
      callback: Callback<GenerateImageTaskPartialResult>): void
```

Request AI image generation task to get the generated image.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-requestImageGeneration(sessionId: int, params: GenerateImageTaskParams,      callback: Callback<GenerateImageTaskPartialResult>): void--><!--Device-ImageGenerationModel-requestImageGeneration(sessionId: int, params: GenerateImageTaskParams,      callback: Callback<GenerateImageTaskPartialResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| params | [GenerateImageTaskParams](arkts-arkui-imagegeneration-generateimagetaskparams-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GenerateImageTaskPartialResult](arkts-arkui-imagegeneration-generateimagetaskpartialresult-i-sys.md)&gt; | Yes |
