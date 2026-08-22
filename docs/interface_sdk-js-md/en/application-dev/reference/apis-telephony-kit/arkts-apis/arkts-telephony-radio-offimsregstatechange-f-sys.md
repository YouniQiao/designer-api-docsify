# offImsRegStateChange (System API)

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## offImsRegStateChange

```TypeScript
function offImsRegStateChange(slotId: int, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void
```

Unsubscribe from imsRegStateChange event.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function offImsRegStateChange(slotId: int, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void--><!--Device-radio-function offImsRegStateChange(slotId: int, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| imsType | [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | Yes | Indicates the ims service type of the [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ImsRegInfo](arkts-telephony-radio-imsreginfo-i-sys.md)&gt; | No | Indicates the callback for getting an instance of the [ImsRegInfo](arkts-telephony-radio-imsreginfo-i-sys.md) class. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |

