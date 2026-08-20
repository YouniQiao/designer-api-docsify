# castAudioSessionAll (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## castAudioSessionAll

```TypeScript
function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>
```

Cast all the media audio to the remote devices or cast back local device

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>--><!--Device-avSession-function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| audioDevices | Array&lt;audio.AudioDeviceDescriptor&gt; | Yes | Specifies the audio devices to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) | The remote session connection failed. |

