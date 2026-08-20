# offCellularDataFlowChange

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## offCellularDataFlowChange

```TypeScript
function offCellularDataFlowChange(callback?: Callback<DataFlowType>): void
```

Cancel callback when the uplink and downlink data flow state of cellular data services is updated.

**Since:** 23

<!--Device-observer-function offCellularDataFlowChange(callback?: Callback<DataFlowType>): void--><!--Device-observer-function offCellularDataFlowChange(callback?: Callback<DataFlowType>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;DataFlowType&gt; | No | Indicates the callback to unsubscribe from the cellularDataFlowChange event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |

