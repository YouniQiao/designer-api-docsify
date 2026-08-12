# createGlobalAudioLoopback (System API)

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## createGlobalAudioLoopback

```TypeScript
function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>
```

Creates a global audio loopback instance, which provides low-latency in-ear monitor function.Hardware audio loopback can only be created in supported platform, application can use[isAudioLoopbackSupported](arkts-audio-audio-audiostreammanager-i.md#isAudioLoopbackSupported) to check first.There should be only one main instance that own the global loopback in the system, the others are controllers. A controller can manage the global loopback by sending commands to the main instance, and listen status change from it.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>--><!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | Yes |
| isController | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioLoopback](arkts-audio-audio-audioloopback-i.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800101-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6800104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-audio-kit/errorcode-audio.md#6800104-unsupported-parameter-value) |
