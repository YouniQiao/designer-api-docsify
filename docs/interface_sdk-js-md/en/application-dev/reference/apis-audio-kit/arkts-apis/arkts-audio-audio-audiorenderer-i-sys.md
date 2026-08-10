# AudioRenderer

提供音频渲染的相关接口。

在使用AudioRenderer的接口之前，需先通过[createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createaudiorenderer)获取AudioRenderer实例。

> **说明：**
> 
> - 本Interface首批接口从API version 8开始支持。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getTarget

```TypeScript
getTarget(): RenderTarget
```

Gets the currently render target of this audio renderer.If the render target has not been changed, the default value {@link RenderTarget#PLAYBACK} will be returned.Ensure that the {@link setTarget} promise is resolved successfully before calling this interface,otherwise, the obtained value may be inaccurate.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioRenderer-getTarget(): RenderTarget--><!--Device-AudioRenderer-getTarget(): RenderTarget-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | Render target of this audio renderer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## Examples

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

Sets the render target of this audio renderer.This function can only be called when the audio renderer is not in the running or released state.Otherwise, it will return an error. The caller must have the ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE permission when target is not {@link RenderTarget#PLAYBACK}.This method can only be called when the audio renderer is ​​not​​ in the RUNNING or RELEASED state.Otherwise, an error will be returned.After changing render target to non-PLAYBACK：1. The audio route and interruption strategy of this renderer will not be affected by{@link AudioSessionManager}.2. The device type of this renderer will be {@link DeviceType#SYSTEM_PRIVATE}.3. Calling {@link start} when the audio scene is not {@link AudioScene#AUDIO_SCENE_VOICE_CHAT} will return error code 6800103.4. Calling {@link getAudioTime} or {@link getAudioTimeSync} will return error code 6800103.5. Calling {@link getAudioTimestampInfo} or {@link getAudioTimestampInfoSync} will return error code 6800103.6. Calling {@link setDefaultOutputDevice} will return error code 6800103.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

<!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>--><!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | Yes | Render target. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800103 | Operation not permit at running and release state. |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |
| 6800301 | Audio client call audio service error, System error. |
| 6800104 | Current renderer is not supported to set target. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setTarget(audio.RenderTarget.INJECT_TO_VOICE_COMMUNICATION_CAPTURE).then(() => {
  console.info('Succeeded in setting target.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set target. code: ${err.code}, message: ${err.message}`);
});
```

