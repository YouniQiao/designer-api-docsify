# getSimAccountInfo

## Modules to Import

```TypeScript
import { sim } from 'sim';
```

## getSimAccountInfo

```TypeScript
function getSimAccountInfo(slotId: int, callback: AsyncCallback<IccAccountInfo>): void
```

Get account information of SIM card.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getSimAccountInfo(slotId: int, callback: AsyncCallback<IccAccountInfo>): void--><!--Device-sim-function getSimAccountInfo(slotId: int, callback: AsyncCallback<IccAccountInfo>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt; | Yes | Indicates the callback for getting a {@code IccAccountInfo} object. The ICCID and phone number will be null if the permission ohos.permission.GET_TELEPHONY_STATE is not granted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) | The SIM card failed to read or update data. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSimAccountInfo

```TypeScript
function getSimAccountInfo(slotId: int): Promise<IccAccountInfo>
```

Get account information of SIM card.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getSimAccountInfo(slotId: int): Promise<IccAccountInfo>--><!--Device-sim-function getSimAccountInfo(slotId: int): Promise<IccAccountInfo>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md)&gt; | Returns a { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8301002](../errorcode-telephony.md#8301002-failed-to-read-or-update-sim-card-data) | The SIM card failed to read or update data. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
    console.info(`getSimAccountInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
});
```

