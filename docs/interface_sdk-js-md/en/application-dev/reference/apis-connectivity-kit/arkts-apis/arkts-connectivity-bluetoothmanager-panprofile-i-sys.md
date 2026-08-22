# PanProfile

Manager pan profile.

**Inheritance/Implementation:** PanProfile extends [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [PanProfile](arkts-connectivity-pan-panprofile-i.md)

<!--Device-bluetoothManager-interface PanProfile--><!--Device-bluetoothManager-interface PanProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## disconnect

```TypeScript
disconnect(device: string): void
```

Disconnect to device with pan. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [disconnect](arkts-connectivity-pan-panprofile-i-sys.md#disconnect)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-PanProfile-disconnect(device: string): void--><!--Device-PanProfile-disconnect(device: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device to disconnect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.disconnect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let hidHostProfile: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
    hidHostProfile.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
    panProfile.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## isTetheringOn

```TypeScript
isTetheringOn(): boolean
```

Obtains the tethering enable or disable. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [isTetheringOn](arkts-connectivity-pan-panprofile-i-sys.md#istetheringon)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

<!--Device-PanProfile-isTetheringOn(): boolean--><!--Device-PanProfile-isTetheringOn(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns the value { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
    panProfile.isTetheringOn();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## setTethering

```TypeScript
setTethering(enable: boolean): void
```

Enable bluetooth tethering. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH and MANAGE_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [setTethering](arkts-connectivity-pan-panprofile-i-sys.md#settethering)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH
- API version 9: ohos.permission.DISCOVER_BLUETOOTH

<!--Device-PanProfile-setTethering(enable: boolean): void--><!--Device-PanProfile-setTethering(enable: boolean): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Specifies whether to enable tethering. The value {@code true} indicates that tethering is enabled, and the value {@code false} indicates that tethering is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
    panProfile.setTethering(true);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

