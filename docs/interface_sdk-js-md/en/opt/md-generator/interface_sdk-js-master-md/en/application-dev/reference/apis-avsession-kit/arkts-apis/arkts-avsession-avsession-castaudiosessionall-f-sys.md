# castAudioSessionAll (System API)

## Modules to Import

```TypeScript
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| audioDevices | Array & lt;audio.AudioDeviceDescriptor & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) |
