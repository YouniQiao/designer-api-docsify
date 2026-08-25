# removeBeaconFence

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeBeaconFence

```TypeScript
function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>
```

Remove a beacon fence.

**Since:** 20

**Required permissions:** 
- API version 20 - 24: ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [beaconFence](arkts-location-geolocationmanager-geofencetransition-i.md) | [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3501602](../errorcode-geoLocationManager.md#3501602-failed-to-delete-a-beacon-fence-because-of-incorrect-information) |
