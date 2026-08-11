# offSimStateChange

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## offSimStateChange

```TypeScript
function offSimStateChange(callback?: Callback<SimStateData>): void
```

Cancel callback when the sim state is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function offSimStateChange(callback?: Callback<SimStateData>): void--><!--Device-observer-function offSimStateChange(callback?: Callback<SimStateData>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | No | Indicates the callback to unsubscribe from the simStateChange event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

