# onRangingStateChange

## Modules to Import

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## onRangingStateChange

```TypeScript
function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void
```

Registers a callback to receive ranging state change notifications.

Notifies state changes for both active ranging and passive ranging operations.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void--><!--Device-ranging-function onRangingStateChange(callback: Callback<RangingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RangingStateChangeInfo&gt; | Yes | Callback used to listen for the ranging state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 34900099 | Internal system error. For example, Internal object is invalid. |
| 201 | Permission denied. |

