# getSimOperatorNumeric

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimOperatorNumeric

```TypeScript
function getSimOperatorNumeric(slotId: int, callback: AsyncCallback<string>): void
```

Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**Since:** 23

<!--Device-sim-function getSimOperatorNumeric(slotId: int, callback: AsyncCallback<string>): void--><!--Device-sim-function getSimOperatorNumeric(slotId: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the PLMN number; returns an empty string if no SIM card is inserted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSimOperatorNumeric

```TypeScript
function getSimOperatorNumeric(slotId: int): Promise<string>
```

Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**Since:** 23

<!--Device-sim-function getSimOperatorNumeric(slotId: int): Promise<string>--><!--Device-sim-function getSimOperatorNumeric(slotId: int): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the PLMN number; returns an empty string if no SIM card is inserted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0).then((data: string) => {
    console.info(`getSimOperatorNumeric success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimOperatorNumeric failed, promise: err->${JSON.stringify(err)}`);
});
```

