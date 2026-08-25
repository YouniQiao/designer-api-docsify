# addBeaconFence

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## addBeaconFence

```TypeScript
function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>
```

Add a beacon fence.

**Since:** 20

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fenceRequest | [BeaconFenceRequest](arkts-location-geolocationmanager-beaconfencerequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3501100](../errorcode-geoLocationManager.md#3501100-failed-to-add-a-beacon-fence-because-the-location-switch-is-turned-off) |
| [3501101](../errorcode-geoLocationManager.md#3501101-failed-to-add-a-beacon-fence-because-bluetooth-is-disabled) |
| [3501601](../errorcode-geoLocationManager.md#3501601-failed-to-add-a-beacon-fence-because-the-maximum-number-is-exceeded) |
| [3501603](../errorcode-geoLocationManager.md#3501603-failed-to-add-a-beacon-fence-because-of-duplication) |
