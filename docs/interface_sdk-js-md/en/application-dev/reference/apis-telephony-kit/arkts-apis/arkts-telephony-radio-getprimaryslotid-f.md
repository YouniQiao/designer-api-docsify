# getPrimarySlotId

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getPrimarySlotId

```TypeScript
function getPrimarySlotId(callback: AsyncCallback<int>): void
```

Obtains the index number of the card slot where the primary card is located if multiple SIM cards are inserted. The primary card is the SIM card inserted in the card slot that uses data services by default.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-radio-function getPrimarySlotId(callback: AsyncCallback<int>): void--><!--Device-radio-function getPrimarySlotId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Indicates the callback for getting the index number of the primary card slot. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId((err: BusinessError, data: number) => {
    if (err) {
        console.error(`getPrimarySlotId failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getPrimarySlotId success, callback: data->${JSON.stringify(data)}`);
});
```


## getPrimarySlotId

```TypeScript
function getPrimarySlotId(): Promise<int>
```

Obtains the index number of the card slot where the primary card is located if multiple SIM cards are inserted. The primary card is the SIM card inserted in the card slot that uses data services by default.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-radio-function getPrimarySlotId(): Promise<int>--><!--Device-radio-function getPrimarySlotId(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Returns the index number of the primary card slot. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId().then((data: number) => {
    console.info(`getPrimarySlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getPrimarySlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

