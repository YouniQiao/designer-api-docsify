# AudioRenderer

This interface provides APIs for audio rendering.

Before calling any API in AudioRenderer, you must use  
[createAudioRenderer]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_to create an AudioRenderer instance.
    **NOTE**  
    
    - The initial APIs of this interface are supported since API version 8.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## getTarget

```TypeScript
getTarget(): RenderTarget
```

Gets the currently render target of this audio renderer.If the render target has not been changed, the default value \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ will be returned.If the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ has been called before calling this interface, ensure its promise object has been resolved successfully, otherwise, the obtained value may be inaccurate.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioRenderer-getTarget(): RenderTarget--><!--Device-AudioRenderer-getTarget(): RenderTarget-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Render target of this audio renderer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

**Example**

```TypeScript
async function getTarget(){
  // (Optional) Set the injection mode.
  await audioRenderer.setTarget(audio.RenderTarget.INJECT_TO_VOICE_COMMUNICATION_CAPTURE);
  console.info('Succeeded in setting target.');

  // If the SetTarget API has been called before this API is called, ensure that the SetTarget API has been successfully called. Otherwise, the obtained value may be inaccurate.
  let renderTarget = audioRenderer.getTarget();
  console.info(`Succeeded in getting target, RenderTarget: ${renderTarget}.`);
}
```

## setTarget

```TypeScript
setTarget(target: RenderTarget): Promise<void>
```

Sets the render target of this audio renderer.This function can only be called when the audio renderer is not in the running or released state.Otherwise, it will return an error. The caller must have the ohos.permission.INJECT\_PLAYBACK\_TO\_AUDIO\_CAPTURE permission when target is not \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.After changing render target to non-PLAYBACK：

1. The audio route and interruption strategy of this renderer will not be affected by \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.2. The device type of this renderer will be \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.3. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ when the audio scene is not \_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ will return error code 6800301.4. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ will return error code 6800301.5. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ will return error code 6800301.6. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ will return error code 6800301.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

<!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>--><!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Render target. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at running and release state. |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) | Current renderer is not supported to set target. |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio client call audio service error, System error. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setTarget(audio.RenderTarget.INJECT_TO_VOICE_COMMUNICATION_CAPTURE).then(() => {
  console.info('Succeeded in setting target.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set target. code: ${err.code}, message: ${err.message}`);
});
```

## setTarget

```TypeScript
setTarget(target: RenderTarget, targetParams?: AudioRendererTargetParams): Promise<void>
```

Sets the render target of this audio renderer.This function can only be called when the audio renderer is not in the running or released state.Otherwise, it will return an error. The caller must have the ohos.permission.INJECT\_PLAYBACK\_TO\_AUDIO\_CAPTURE permission when target is not \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.After changing render target to non-PLAYBACK:

1. The audio route and interruption strategy of this renderer will not be affected by\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.2. The device type of this renderer will be \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.3. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ when the audio scene is not \_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ will return error code 6800301.4. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ will return error code 6800301.5. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ will return error code 6800301.6. Calling \_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ will return error code 6800301.

This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRenderer-setTarget(target: RenderTarget, targetParams?: AudioRendererTargetParams): Promise<void>--><!--Device-AudioRenderer-setTarget(target: RenderTarget, targetParams?: AudioRendererTargetParams): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Render target. |
| targetParams | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameter used to specify the target capturer stream into which the renderer stream is injected. If this parameter is not specified when target is not \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, the renderer stream is automatically injected into all voice communication capture streams by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at running and release state. |
| [6800104](../errorcode-audio.md#6800104-unsupported-parameter-value) | Current renderer is not supported to set target. |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio server process died. |

