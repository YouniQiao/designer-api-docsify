# createA2dpSrcProfile

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
```

## createA2dpSrcProfile

```TypeScript
function createA2dpSrcProfile(): A2dpSourceProfile
```

create the instance of a2dp profile.

**Since:** 10

<!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile--><!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [A2dpSourceProfile](arkts-connectivity-a2dp-a2dpsourceprofile-i.md) | Returns the instance of profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let a2dpProfile = a2dp.createA2dpSrcProfile();
    console.info('a2dp success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
