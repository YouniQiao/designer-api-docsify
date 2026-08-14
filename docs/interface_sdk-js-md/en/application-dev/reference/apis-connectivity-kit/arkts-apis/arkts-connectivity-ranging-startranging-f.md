# startRanging

## Modules to Import

```TypeScript
import { ranging } from 'ranging';
```

## startRanging

```TypeScript
function startRanging(params: RangingParams, callback: Callback<RangingResult>): void
```

Initiates ranging with a specified device. If the link to the target device is already established, ranging starts directly. If not connected, this interface will: 1. Attempt to establish connection and perform pairing/encryption. 2. Query service to verify the device supports ranging. Initiate ranging upon confirmation. Ranging state updates are notified via onRangingStateChange callback.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void--><!--Device-ranging-function startRanging(params: RangingParams, callback: Callback<RangingResult>): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [RangingParams](arkts-connectivity-ranging-rangingparams-i.md) | Yes | Parameters for ranging. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RangingResult](arkts-connectivity-ranging-rangingresult-i.md)&gt; | Yes | Indicates the callback for reporting the ranging result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 34900052 | The specified type of ranging service is not supported. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 34900053 | The ranging service is disabled. |
| 34900054 | The parameter value does not meet specifications. |
| 34900051 | The device has already initiated ranging. |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal system error. For example, Internal object is invalid. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

