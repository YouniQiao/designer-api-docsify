# onSimStateChange

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onSimStateChange

```TypeScript
function onSimStateChange(callback: Callback<SimStateData>): void
```

Callback when the sim state corresponding to the default sim card is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function onSimStateChange(callback: Callback<SimStateData>): void--><!--Device-observer-function onSimStateChange(callback: Callback<SimStateData>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | Yes | Indicates the callback for getting the SimStateData object. including state Indicates the sim state, and reason Indicates the cause of the change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |


## onSimStateChange

```TypeScript
function onSimStateChange(options: ObserverOptions, callback: Callback<SimStateData>): void
```

Callback when the sim state corresponding to the monitored {@code slotId} is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function onSimStateChange(options: ObserverOptions, callback: Callback<SimStateData>): void--><!--Device-observer-function onSimStateChange(options: ObserverOptions, callback: Callback<SimStateData>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | Yes | Indicates the callback for getting the SimStateData object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

