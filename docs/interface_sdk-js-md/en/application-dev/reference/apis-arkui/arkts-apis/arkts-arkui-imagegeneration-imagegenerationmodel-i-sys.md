# ImageGenerationModel (System API)

AI Image Model Abstract Interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-imageGeneration-interface ImageGenerationModel--><!--Device-imageGeneration-interface ImageGenerationModel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## cancelImageGeneration

```TypeScript
cancelImageGeneration(sessionId: int): void
```

Cancel AI image generation task.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-cancelImageGeneration(sessionId: int): void--><!--Device-ImageGenerationModel-cancelImageGeneration(sessionId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | The session id for cancel an AI image generation task. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Value: range: [0, +∞] |

## getModelSupportStyles

```TypeScript
getModelSupportStyles(): Array<ImageStyle>
```

Get the types of image styles supported by the AI model.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-getModelSupportStyles(): Array<ImageStyle>--><!--Device-ImageGenerationModel-getModelSupportStyles(): Array<ImageStyle>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ImageStyle&gt; | image style information. |

## onComplain

```TypeScript
onComplain(sessionId: int, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void
```

User use complaint menu to complain the result of an AI-generated image task.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-onComplain(sessionId: int, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void--><!--Device-ImageGenerationModel-onComplain(sessionId: int, request: GenerateImageTaskParams, result: GenerateImageTaskResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | The session id of AI image generation task. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Value: range: [0, +∞] |
| request | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The origin request for AI-generated image task. |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The result for AI-generated image task. |

## requestImageGeneration

```TypeScript
requestImageGeneration(sessionId: int, params: GenerateImageTaskParams,
      callback: Callback<GenerateImageTaskPartialResult>): void
```

Request AI image generation task to get the generated image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageGenerationModel-requestImageGeneration(sessionId: int, params: GenerateImageTaskParams,      callback: Callback<GenerateImageTaskPartialResult>): void--><!--Device-ImageGenerationModel-requestImageGeneration(sessionId: int, params: GenerateImageTaskParams,      callback: Callback<GenerateImageTaskPartialResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | The session id for requesting an AI image generation task. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Value: range:[0, +∞] |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters for requesting an AI image generation task. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;GenerateImageTaskPartialResult&gt; | Yes | the callback used to return the GenerateImageTaskPartialResult. |

