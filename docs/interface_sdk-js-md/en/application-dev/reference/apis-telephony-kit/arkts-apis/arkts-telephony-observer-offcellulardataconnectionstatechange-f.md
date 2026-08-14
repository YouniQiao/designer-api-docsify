# offCellularDataConnectionStateChange

## Modules to Import

```TypeScript
import { observer } from 'observer';
```

## offCellularDataConnectionStateChange

```TypeScript
function offCellularDataConnectionStateChange(callback?: Callback<DataConnectionStateInfo>): void
```

Cancel callback when the cellular data link connection state is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-observer-function offCellularDataConnectionStateChange(callback?: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function offCellularDataConnectionStateChange(callback?: Callback<DataConnectionStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | No | Indicates the callback to unsubscribe from the cellularDataConnectionStateChange event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

