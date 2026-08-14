# onCellInfoChange (System API)

## Modules to Import

```TypeScript
import { observer } from 'observer';
```

## onCellInfoChange

```TypeScript
function onCellInfoChange(callback: Callback<Array<CellInformation>>): void
```

Callback when the cell information corresponding to the default sim card is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-observer-function onCellInfoChange(callback: Callback<Array<CellInformation>>): void--><!--Device-observer-function onCellInfoChange(callback: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | Yes | Indicates the callback for getting an array of instances of the classes derived from [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md#CellInformation-(System-API)). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |


## onCellInfoChange

```TypeScript
function onCellInfoChange(options: ObserverOptions, callback: Callback<Array<CellInformation>>): void
```

Callback when the cell information corresponding to a monitored {@code slotId} is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-observer-function onCellInfoChange(options: ObserverOptions, callback: Callback<Array<CellInformation>>): void--><!--Device-observer-function onCellInfoChange(options: ObserverOptions, callback: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | Yes | Indicates the callback for getting an array of instances of the classes derived from [CellInformation](arkts-telephony-observer-cellinformation-t-sys.md#CellInformation-(System-API)). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

