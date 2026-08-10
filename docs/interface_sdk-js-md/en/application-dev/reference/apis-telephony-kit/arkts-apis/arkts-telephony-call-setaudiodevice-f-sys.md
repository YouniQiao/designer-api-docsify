# setAudioDevice (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setAudioDevice

```TypeScript
function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void
```

Set the audio device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void--><!--Device-call-function setAudioDevice(device: AudioDevice, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) | Yes | Indicates the device of audio. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of setAudioDevice. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

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

Set the audio device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setAudioDevice(device: AudioDevice): Promise<void>--><!--Device-call-function setAudioDevice(device: AudioDevice): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) | Yes | Indicates the device of audio. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setAudioDevice. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

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

