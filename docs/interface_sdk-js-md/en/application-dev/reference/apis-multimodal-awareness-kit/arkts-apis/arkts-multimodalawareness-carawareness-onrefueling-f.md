# onRefueling

## Modules to Import

```TypeScript
import { carAwareness } from '@kit.MultimodalAwarenessKit';
```

## onRefueling

```TypeScript
function onRefueling(callback: Callback<RefuelingInfo>): void
```

Enables refueling awareness and subscribes to refueling awareness results. If this function is not supported, no callback will be triggered. You can obtain the supported capabilities by calling the getAllCapacityList method.

**Since:** 26.1.0

**Required permissions:** ohos.permission.vehicle.MMA_ENERGYREFILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-carAwareness-function onRefueling(callback: Callback<RefuelingInfo>): void--><!--Device-carAwareness-function onRefueling(callback: Callback<RefuelingInfo>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RefuelingInfo](arkts-multimodalawareness-carawareness-refuelinginfo-i.md)&gt; | Yes | Callback for obtaining the capability data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [34000002](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-unsupported-application-or-page) | Specific capability not supported. |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) | Service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

