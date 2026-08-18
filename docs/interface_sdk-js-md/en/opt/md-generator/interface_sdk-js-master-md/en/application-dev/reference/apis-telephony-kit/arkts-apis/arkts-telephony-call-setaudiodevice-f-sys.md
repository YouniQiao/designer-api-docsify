# setAudioDevice (System API)

## Modules to Import

```TypeScript
```

## setAudioDevice

```TypeScript
function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void
```

Sets the audio device for a call. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void--><!--Device-call-function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let audioDevice: call.AudioDevice = {
    deviceType: call.AudioDeviceType.DEVICE_EARPIECE
}
call.setAudioDevice(audioDevice, (err: BusinessError) => {
    if (err) {
        console.error(`setAudioDevice fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setAudioDevice success.`);
    }
});
```


## setAudioDevice

```TypeScript
function setAudioDevice(device: AudioDevice): Promise<void>
```

Sets the audio device for a call. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setAudioDevice(device: AudioDevice): Promise<void>--><!--Device-call-function setAudioDevice(device: AudioDevice): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let audioDevice: call.AudioDevice = {
    deviceType: call.AudioDeviceType.DEVICE_EARPIECE
}
call.setAudioDevice(audioDevice).then(() => {
    console.info(`setAudioDevice success.`);
}).catch((err: BusinessError) => {
    console.error(`setAudioDevice fail, promise: err->${JSON.stringify(err)}`);
});
```
