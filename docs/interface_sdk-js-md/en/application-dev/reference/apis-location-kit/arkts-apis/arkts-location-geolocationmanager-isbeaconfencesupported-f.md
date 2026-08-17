# isBeaconFenceSupported

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## isBeaconFenceSupported

```TypeScript
function isBeaconFenceSupported(): boolean
```

Check whether the BeaconFence service is supported.

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-geoLocationManager-function isBeaconFenceSupported(): boolean--><!--Device-geoLocationManager-function isBeaconFenceSupported(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isBeaconFenceSupported = geoLocationManager.isBeaconFenceSupported();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

