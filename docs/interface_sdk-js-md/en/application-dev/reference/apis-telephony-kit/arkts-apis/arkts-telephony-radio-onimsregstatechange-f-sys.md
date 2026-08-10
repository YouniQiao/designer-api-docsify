# onImsRegStateChange (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## onImsRegStateChange

```TypeScript
function onImsRegStateChange(slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void
```

Called when the IMS registration state of specified IMS service type corresponding to a monitored {@code slotId} updates.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function onImsRegStateChange(slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void--><!--Device-radio-function onImsRegStateChange(slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| imsType | [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | Yes | Indicates the ims service type of the {@link ImsServiceType}. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ImsRegInfo&gt; | Yes | Indicates the callback for getting an instance of the {@link ImsRegInfo} class. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

