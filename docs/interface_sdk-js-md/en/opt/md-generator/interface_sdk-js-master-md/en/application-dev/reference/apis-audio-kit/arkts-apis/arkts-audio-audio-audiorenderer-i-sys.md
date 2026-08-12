# AudioRenderer

This interface provides APIs for audio rendering.

Before calling any API in AudioRenderer, you must use  
[createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md#createAudioRenderer)to create an AudioRenderer instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 8.

**Since:** 8

<!--Device-audio-interface AudioRenderer--><!--Device-audio-interface AudioRenderer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## getTarget

```TypeScript
getTarget(): RenderTarget
```

Gets the currently render target of this audio renderer.If the render target has not been changed, the default value [PLAYBACK](arkts-audio-audio-rendertarget-e-sys.md#PLAYBACK) will be returned.If the [setTarget](#setTarget) has been called before calling this interface, ensure its promise object has been resolved successfully, otherwise, the obtained value may be inaccurate.

**Since:** 22

<!--Device-AudioRenderer-getTarget(): RenderTarget--><!--Device-AudioRenderer-getTarget(): RenderTarget-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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

Sets the render target of this audio renderer.This function can only be called when the audio renderer is not in the running or released state.Otherwise, it will return an error. The caller must have the ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE permission when target is not [PLAYBACK](arkts-audio-audio-rendertarget-e-sys.md#PLAYBACK).After changing render target to non-PLAYBACK：

1. The audio route and interruption strategy of this renderer will not be affected by [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md#AudioSessionManager).2. The device type of this renderer will be [SYSTEM_PRIVATE](arkts-audio-audio-devicetype-e.md#SYSTEM_PRIVATE).3. Calling [start](start) when the audio scene is not [AUDIO_SCENE_VOICE_CHAT](arkts-audio-audio-audioscene-e.md#AUDIO_SCENE_VOICE_CHAT) will return error code 6800301.4. Calling [getAudioTime](getAudioTime) or [getAudioTimeSync](getAudioTimeSync) will return error code 6800301.5. Calling [getAudioTimestampInfo](getAudioTimestampInfo) or [getAudioTimestampInfoSync](getAudioTimestampInfoSync) will return error code 6800301.6. Calling [setDefaultOutputDevice](setDefaultOutputDevice) will return error code 6800301.

**Since:** 22

**Required permissions:** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

<!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>--><!--Device-AudioRenderer-setTarget(target: RenderTarget): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800301-system-error) |
| [6800104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800104-unsupported-parameter-value) |

## Examples

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

Sets the render target of this audio renderer.This function can only be called when the audio renderer is not in the running or released state.Otherwise, it will return an error. The caller must have the ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE permission when target is not [PLAYBACK](arkts-audio-audio-rendertarget-e-sys.md#PLAYBACK).After changing render target to non-PLAYBACK:

1. The audio route and interruption strategy of this renderer will not be affected by[AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md#AudioSessionManager).2. The device type of this renderer will be [SYSTEM_PRIVATE](arkts-audio-audio-devicetype-e.md#SYSTEM_PRIVATE).3. Calling [start](start) when the audio scene is not [AUDIO_SCENE_VOICE_CHAT](arkts-audio-audio-audioscene-e.md#AUDIO_SCENE_VOICE_CHAT) will  return error code 6800301.4. Calling [getAudioTime](getAudioTime) or [getAudioTimeSync](getAudioTimeSync) will return error code 6800301.5. Calling [getAudioTimestampInfo](getAudioTimestampInfo) or [getAudioTimestampInfoSync](getAudioTimestampInfoSync) will return error code 6800301.6. Calling [setDefaultOutputDevice](setDefaultOutputDevice) will return error code 6800301.

This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRenderer-setTarget(target: RenderTarget, targetParams?: AudioRendererTargetParams): Promise<void>--><!--Device-AudioRenderer-setTarget(target: RenderTarget, targetParams?: AudioRendererTargetParams): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | Yes |
| targetParams | [AudioRendererTargetParams](arkts-audio-audio-audiorenderertargetparams-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800301](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800301-system-error) |
| [6800104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800104-unsupported-parameter-value) |
