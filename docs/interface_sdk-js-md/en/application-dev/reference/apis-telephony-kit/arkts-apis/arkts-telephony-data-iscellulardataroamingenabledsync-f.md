# isCellularDataRoamingEnabledSync

## Modules to Import

```TypeScript
import { data } from 'data';
```

## isCellularDataRoamingEnabledSync

```TypeScript
function isCellularDataRoamingEnabledSync(slotId: int): boolean
```

Check whether roaming is enabled for cellular data services.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function isCellularDataRoamingEnabledSync(slotId: int): boolean--><!--Device-data-function isCellularDataRoamingEnabledSync(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the ID of a card slot. The value {@code 0} indicates card 1, and the value {@code 1} indicates card 2. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Internal error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataRoamingEnabledSync(0);
    console.info(`isCellularDataRoamingEnabledSync success : ${isEnabled}`);
} catch (err) {
    console.error(`isCellularDataRoamingEnabledSync fail. code: ${err.code}, message: ${err.message}`);  
}
```

