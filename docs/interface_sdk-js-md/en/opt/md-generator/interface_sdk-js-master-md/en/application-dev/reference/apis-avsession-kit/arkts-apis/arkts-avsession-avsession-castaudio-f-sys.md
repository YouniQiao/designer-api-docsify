# castAudio (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## castAudio

```TypeScript
function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void
```

Cast Audio to the remote devices or cast back local device

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void--><!--Device-avSession-function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) \| 'all' | Yes |
| audioDevices | Array & lt;audio.AudioDeviceDescriptor & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioRoutingManager = audioManager.getRoutingManager();
let audioDevices: audio.AudioDeviceDescriptors | undefined = undefined;
audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data) => {
  audioDevices = data;
  console.info('Promise returned to indicate that the device list is obtained.');
  if (audioDevices !== undefined) {
    avSession.castAudio('all', audioDevices as audio.AudioDeviceDescriptors, () => {
        console.info('Succeeded in casting audio.');
    });
  }
});
```


## castAudio

```TypeScript
function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>
```

Cast Audio to the remote devices or cast back local device

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>--><!--Device-avSession-function castAudio(session: SessionToken | 'all', audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) \| 'all' | Yes |
| audioDevices | Array & lt;audio.AudioDeviceDescriptor & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [6600104](../errorcode-avsession.md#6600104-remote-session-connection-failure) |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioRoutingManager = audioManager.getRoutingManager();
let audioDevices: audio.AudioDeviceDescriptors | undefined = undefined;
audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data) => {
  audioDevices = data;
  console.info('Promise returned to indicate that the device list is obtained.');
});

if (audioDevices !== undefined) {
  avSession.castAudio('all', audioDevices as audio.AudioDeviceDescriptors).then(() => {
    console.info('Succeeded in creating controller.');
  });
}
```
