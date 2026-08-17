# getNetworkSelectionMode

## Modules to Import

```TypeScript
import { radio } from 'radio';
```

## getNetworkSelectionMode

```TypeScript
function getNetworkSelectionMode(slotId: int, callback: AsyncCallback<NetworkSelectionMode>): void
```

Obtains the network search mode of the SIM card in a specified slot.

**Since:** 23

<!--Device-radio-function getNetworkSelectionMode(slotId: int, callback: AsyncCallback<NetworkSelectionMode>): void--><!--Device-radio-function getNetworkSelectionMode(slotId: int, callback: AsyncCallback<NetworkSelectionMode>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetworkSelectionMode](arkts-telephony-radio-networkselectionmode-e.md)&gt; | Yes | Indicates the callback for getting the network search mode of the SIM card. Available values are as follows: &lt;ul&gt; &lt;li&gt;[NETWORK_SELECTION_UNKNOWN](arkts-telephony-radio-networkselectionmode-e.md#networkselectionunknown) &lt;li&gt;[NETWORK_SELECTION_AUTOMATIC](arkts-telephony-radio-networkselectionmode-e.md#networkselectionautomatic) &lt;li&gt;[NETWORK_SELECTION_MANUAL](arkts-telephony-radio-networkselectionmode-e.md#networkselectionmanual) &lt;ul&gt; |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId, (err: BusinessError, data: radio.NetworkSelectionMode) => {
    if (err) {
        console.error(`getNetworkSelectionMode failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getNetworkSelectionMode success, callback: data->${JSON.stringify(data)}`);
});
```


## getNetworkSelectionMode

```TypeScript
function getNetworkSelectionMode(slotId: int): Promise<NetworkSelectionMode>
```

Obtains the network search mode of the SIM card in a specified slot.

**Since:** 23

<!--Device-radio-function getNetworkSelectionMode(slotId: int): Promise<NetworkSelectionMode>--><!--Device-radio-function getNetworkSelectionMode(slotId: int): Promise<NetworkSelectionMode>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[NetworkSelectionMode](arkts-telephony-radio-networkselectionmode-e.md)&gt; | Returns the network search mode of the SIM card. Available values are as follows: &lt;ul&gt; &lt;li&gt;{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId).then((data: radio.NetworkSelectionMode) => {
    console.info(`getNetworkSelectionMode success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkSelectionMode failed, promise: err->${JSON.stringify(err)}`);
});
```

