# addBeaconFence

## Modules to Import

```TypeScript
```

## addBeaconFence

```TypeScript
function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>
```

Add a beacon fence.

**Since:** 26.1.0

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-geoLocationManager-function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<int>--><!--Device-geoLocationManager-function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<int>-End-->

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3501601](../errorcode-geoLocationManager.md#3501601-failed-to-add-a-beacon-fence-because-the-maximum-number-is-exceeded) |
| [3501603](../errorcode-geoLocationManager.md#3501603-failed-to-add-a-beacon-fence-because-of-duplication) |
| [3501101](../errorcode-geoLocationManager.md#3501101-failed-to-add-a-beacon-fence-because-bluetooth-is-disabled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3501100](../errorcode-geoLocationManager.md#3501100-failed-to-add-a-beacon-fence-because-the-location-switch-is-turned-off) |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // The iBeacon protocol is used as an example. The format is as follows:
  // 01 byte    type = 0x02
  // 01 byte    len = 0x15 = 21
  // 16 byte    UUID
  // 02 byte    major
  // 02 byte    minor
  // 01 byte    tx power
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

  let fenceRequest: geoLocationManager.BeaconFenceRequest = {
    beacon: beacon,
    transitionCallback: (transition: geoLocationManager.GeofenceTransition) => {
      if (transition) {
        console.info("GeofenceTransition: err" + JSON.stringify(transition));
      }
    },
    fenceExtensionAbilityName: "MyFenceExtensionAbility",
  };
  geoLocationManager.addBeaconFence(fenceRequest).then((id) => {
    console.info("addBeaconFence success, fence id:" + id);
  }).catch((err: BusinessError) => {
    console.error('promise, addBeaconFence: error=' + JSON.stringify(err));
  });
} catch (error) {
  console.error("addBeaconFence: errCode" + error.code + ", errMessage" + error.message);
}
```
