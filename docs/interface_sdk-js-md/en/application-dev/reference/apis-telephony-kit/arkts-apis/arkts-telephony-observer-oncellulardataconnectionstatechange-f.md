# onCellularDataConnectionStateChange

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onCellularDataConnectionStateChange

```TypeScript
function onCellularDataConnectionStateChange(callback: Callback<DataConnectionStateInfo>): void
```

Callback when the cellular data link connection state corresponding to the default sim card is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function onCellularDataConnectionStateChange(callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function onCellularDataConnectionStateChange(callback: Callback<DataConnectionStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | Yes | Indicates the callback for getting the cellular data link connection state, and networkType Indicates the radio access technology for cellular data services. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |


## onCellularDataConnectionStateChange

```TypeScript
function onCellularDataConnectionStateChange(options: ObserverOptions,
              callback: Callback<DataConnectionStateInfo>): void
```

Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function onCellularDataConnectionStateChange(options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function onCellularDataConnectionStateChange(options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | Yes | Indicates the callback for getting the cellular data link connection state, and networkType Indicates the radio access technology for cellular data services. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

