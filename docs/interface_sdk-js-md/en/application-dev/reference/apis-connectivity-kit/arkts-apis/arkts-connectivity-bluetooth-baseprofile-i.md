# BaseProfile

Base interface of profile.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import bas from '@kit.ConnectivityKit.bas';
import common from '@kit.ConnectivityKit.common';
import bluetooth from '@kit.ConnectivityKit';
import map from '@kit.ConnectivityKit.map';
import pan from '@kit.ConnectivityKit.pan';
import pbap from '@kit.ConnectivityKit.pbap';
import opp from '@kit.ConnectivityKit.opp';
import socket from '@kit.ConnectivityKit.socket';
import wearDetection from '@kit.ConnectivityKit.wearDetection';
import bluetoothManager from '@kit.ConnectivityKitManager';
```

## getConnectionDevices

```TypeScript
getConnectionDevices(): Array<string>
```

Obtains the connected devices list of profile.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getConnectionDevices](arkts-connectivity-bluetoothmanager-baseprofile-i.md#getconnectiondevices)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array & lt;string & gt; | Returns the address of connected devices list. |

**Examples**

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

**Substitutes:** [getDeviceState](arkts-connectivity-bluetoothmanager-baseprofile-i.md#getdevicestate)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of bluetooth device. |

**Return value:**

| Type | Description |
| --- | --- |
| [ProfileConnectionState](arkts-connectivity-bluetooth-profileconnectionstate-e.md) | Returns { |

**Examples**

```TypeScript
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : bluetooth.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
```
