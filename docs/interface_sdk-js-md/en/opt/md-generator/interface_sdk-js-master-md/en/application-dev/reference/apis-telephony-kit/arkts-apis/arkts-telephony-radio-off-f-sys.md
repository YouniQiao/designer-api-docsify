# off (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## off('imsRegStateChange')

```TypeScript
function off(type: 'imsRegStateChange', slotId: number, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void
```

Unsubscribe from imsRegStateChange event.

**Since:** 9

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function off(type: 'imsRegStateChange', slotId: int, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void--><!--Device-radio-function off(type: 'imsRegStateChange', slotId: int, imsType: ImsServiceType, callback?: Callback<ImsRegInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imsRegStateChange' | Yes |
| slotId | number | Yes |
| imsType | [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ImsRegInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let slotId: number = 0;
let mode: radio.ImsServiceType = radio.ImsServiceType.TYPE_VIDEO;
radio.off('imsRegStateChange', slotId, mode, (data: radio.ImsRegInfo) => {
    console.info(`off imsRegStateChange success, callback: data->${JSON.stringify(data)}`);
});
```
