# setNetworkCapability (System API)

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## setNetworkCapability

```TypeScript
function setNetworkCapability(slotId: number, type: NetworkCapabilityType, state: NetworkCapabilityState,
    callback: AsyncCallback<void>): void
```

Set the type and state for the specified network capability.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState,    callback: AsyncCallback<void>): void--><!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState,    callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Yes |
| state | [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Yes |
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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let type: radio.NetworkCapabilityType = radio.NetworkCapabilityType.SERVICE_TYPE_NR;
let state: radio.NetworkCapabilityState = radio.NetworkCapabilityState.SERVICE_CAPABILITY_ON;
radio.setNetworkCapability(slotId, type, state, (err: BusinessError) => {
    if (err) {
        console.error(`setNetworkCapability failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`setNetworkCapability success.`);
});
```


## setNetworkCapability

```TypeScript
function setNetworkCapability(slotId: number, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>
```

Set the type and state for the specified network capability.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>--><!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Yes |
| state | [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Yes |

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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let type: radio.NetworkCapabilityType = radio.NetworkCapabilityType.SERVICE_TYPE_NR;
let state: radio.NetworkCapabilityState = radio.NetworkCapabilityState.SERVICE_CAPABILITY_ON;
radio.setNetworkCapability(slotId, type, state).then(() => {
    console.info(`setNetworkCapability success`);
}).catch((err: BusinessError) => {
    console.error(`setNetworkCapability failed, promise: err->${JSON.stringify(err)}`);
});
```
