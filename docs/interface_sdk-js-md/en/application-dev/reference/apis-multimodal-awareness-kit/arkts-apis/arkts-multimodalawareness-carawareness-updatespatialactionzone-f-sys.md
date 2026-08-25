# updateSpatialActionZone (System API)

## Modules to Import

```TypeScript
import { carAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## updateSpatialActionZone

```TypeScript
function updateSpatialActionZone(zone: number): void
```

Updates the voice zone when the voice subscribes to the spatial point engine capability.

**Since:** 26.1.0

**Required permissions:** ohos.permission.vehicle.MMA_SPATIALACTION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| zone | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34000001](../errorcode-onScreen.md#34000001-service-exception) |
| [34000002](../errorcode-onScreen.md#34000002-unsupported-application-or-page) |
