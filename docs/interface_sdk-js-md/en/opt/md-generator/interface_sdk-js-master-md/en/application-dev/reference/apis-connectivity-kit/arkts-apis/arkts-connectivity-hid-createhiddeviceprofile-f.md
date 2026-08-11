# createHidDeviceProfile

## Modules to Import

```TypeScript
import { hid } from 'kits/@kit.ConnectivityKit';
```

## createHidDeviceProfile

```TypeScript
function createHidDeviceProfile(): HidDeviceProfile
```

Creates the instance of HID device profile.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-hid-function createHidDeviceProfile(): HidDeviceProfile--><!--Device-hid-function createHidDeviceProfile(): HidDeviceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HidDeviceProfile](arkts-connectivity-hid-hiddeviceprofile-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
try {
    let hidDeviceProfile = hid.createHidDeviceProfile();
    console.info('hidDevice success');
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
