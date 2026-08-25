# onRefueling

## Modules to Import

```TypeScript
import { carAwareness } from 'kits/@kit.MultimodalAwarenessKit';
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

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RefuelingInfo](arkts-multimodalawareness-carawareness-refuelinginfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [34000001](../errorcode-onScreen.md#34000001-service-exception) |
| [34000002](../errorcode-onScreen.md#34000002-unsupported-application-or-page) |
