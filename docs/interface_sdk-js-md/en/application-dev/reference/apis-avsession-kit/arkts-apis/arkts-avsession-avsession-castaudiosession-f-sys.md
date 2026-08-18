# castAudioSession (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## castAudioSession

```TypeScript
function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void
```

Cast Audio to the remote devices or cast back local device

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void--><!--Device-avSession-function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes | Specifies the sessionId which to send to remote. |
| audioDevices | Array&lt;audio.AudioDeviceDescriptor&gt; | Yes | Specifies the audio devices to cast. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) | The remote session connection failed. |


## castAudioSession

```TypeScript
function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>
```

Cast Audio to the remote devices or cast back local device

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>--><!--Device-avSession-function castAudioSession(session: SessionToken, audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Yes | Specifies the sessionId which to send to remote. |
| audioDevices | Array&lt;audio.AudioDeviceDescriptor&gt; | Yes | Specifies the audio devices to cast. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) | The remote session connection failed. |

