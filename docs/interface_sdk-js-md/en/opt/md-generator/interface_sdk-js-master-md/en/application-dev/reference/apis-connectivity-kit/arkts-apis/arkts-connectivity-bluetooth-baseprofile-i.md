# BaseProfile

Base interface of profile.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BaseProfile](ohos.bluetoothManager/bluetoothManager.BaseProfile)

<!--Device-bluetooth-interface BaseProfile--><!--Device-bluetooth-interface BaseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getConnectionDevices

```TypeScript
getConnectionDevices(): Array<string>
```

Obtains the connected devices list of profile.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getConnectionDevices](ohos.bluetoothManager/bluetoothManager.BaseProfile#getConnectionDevices)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-BaseProfile-getConnectionDevices(): Array<string>--><!--Device-BaseProfile-getConnectionDevices(): Array<string>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## Examples

```TypeScript
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let retArray : Array<string> = a2dpSrc.getConnectionDevices();
```

## getDeviceState

```TypeScript
getDeviceState(device: string): ProfileConnectionState
```

Obtains the profile state of device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDeviceState](ohos.bluetoothManager/bluetoothManager.BaseProfile#getDeviceState)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-BaseProfile-getDeviceState(device: string): ProfileConnectionState--><!--Device-BaseProfile-getDeviceState(device: string): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md) |

## Examples

```TypeScript
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : bluetooth.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
```
