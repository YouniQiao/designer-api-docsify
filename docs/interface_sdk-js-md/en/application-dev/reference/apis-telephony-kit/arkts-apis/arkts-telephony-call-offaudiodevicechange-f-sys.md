# offAudioDeviceChange (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## offAudioDeviceChange

```TypeScript
function offAudioDeviceChange(callback?: Callback<AudioDeviceCallbackInfo>): void
```

Unsubscribe from the audioDeviceChange event.

**Since:** 26.1.0

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function offAudioDeviceChange(callback?: Callback<AudioDeviceCallbackInfo>): void--><!--Device-call-function offAudioDeviceChange(callback?: Callback<AudioDeviceCallbackInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceCallbackInfo](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md)&gt; | No | Indicates the callback for getting the result of Current AudioDevice. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

