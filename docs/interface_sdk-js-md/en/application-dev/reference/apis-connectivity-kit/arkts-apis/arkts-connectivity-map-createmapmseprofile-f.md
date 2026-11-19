# createMapMseProfile

## Modules to Import

```TypeScript
import { map } from '@kit.ConnectivityKit';
```

## createMapMseProfile

```TypeScript
function createMapMseProfile(): MapMseProfile
```

create the instance of MAP MSE profile.

**Since:** 11

<!--Device-map-function createMapMseProfile(): MapMseProfile--><!--Device-map-function createMapMseProfile(): MapMseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MapMseProfile](arkts-connectivity-map-mapmseprofile-i-sys.md) | Returns the instance of map mse profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes:         1. The hardware does not support the capability;         2. The chip does not support the capability;         3. A dependent service feature is not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let mapMseProfile = map.createMapMseProfile();
    console.info('MapMse success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
