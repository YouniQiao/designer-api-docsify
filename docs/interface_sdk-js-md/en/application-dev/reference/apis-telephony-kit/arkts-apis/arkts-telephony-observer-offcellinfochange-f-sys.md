# offCellInfoChange (System API)

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## offCellInfoChange

```TypeScript
function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void
```

Cancel callback when the cell information is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | No | Indicates the callback to unsubscribe from the cellInfoChange event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

