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

<!--Device-geoLocationManager-function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>--><!--Device-geoLocationManager-function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| beaconFence | [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3501602](../errorcode-geoLocationManager.md#3501602-failed-to-delete-a-beacon-fence-because-of-incorrect-information) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let manufactureDataBuffer: Uint8Array = new Uint8Array([0X02, 0X15, 0X00, 0X11, 0X22, 0X33, 0X44, 0X55,
    0X66, 0X77, 0X88, 0X99, 0XAA, 0XBB, 0XCC, 0XDD, 0XEE, 0XFF, 0X11, 0X22, 0X33, 0X44, 0X55]);
  let manufactureDataMaskBuffer: Uint8Array = new Uint8Array([0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
    0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF]);

  let manufactureData: geoLocationManager.BeaconManufactureData = {
    manufactureId: 0X004C,
    manufactureData: manufactureDataBuffer.buffer,
    manufactureDataMask: manufactureDataMaskBuffer.buffer
  };

  let beacon: geoLocationManager.BeaconFence = {
    identifier: "11",
    beaconFenceInfoType: geoLocationManager.BeaconFenceInfoType.BEACON_MANUFACTURE_DATA,
    manufactureData: manufactureData
  };
  geoLocationManager.removeBeaconFence(beacon).then(() => {
    console.info("promise, removeBeaconFence success");
  })
    .catch((error: BusinessError) => {
      console.error("promise, removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
    });
} catch (error) {
  console.error("removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
}
```
