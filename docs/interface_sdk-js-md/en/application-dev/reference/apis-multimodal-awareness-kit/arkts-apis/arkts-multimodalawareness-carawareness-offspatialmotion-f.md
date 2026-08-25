# offSpatialMotion

## Modules to Import

```TypeScript
import { carAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## offSpatialMotion

```TypeScript
function offSpatialMotion(callback?: Callback<SpatialMotionInfo>): void
```

Disables spatial motion awareness and subscribes to spatial motion awareness results.

**Since:** 26.1.0

**Required permissions:** ohos.permission.vehicle.MMA_SPATIALACTION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SpatialMotionInfo](arkts-multimodalawareness-carawareness-spatialmotioninfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [34000001](../errorcode-onScreen.md#34000001-service-exception) |
