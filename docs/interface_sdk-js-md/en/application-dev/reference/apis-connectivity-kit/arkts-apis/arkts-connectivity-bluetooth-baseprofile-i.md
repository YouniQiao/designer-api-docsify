# BaseProfile

Base interface of profile.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ProfileConnectionState](arkts-connectivity-bluetooth-profileconnectionstate-e.md) |
