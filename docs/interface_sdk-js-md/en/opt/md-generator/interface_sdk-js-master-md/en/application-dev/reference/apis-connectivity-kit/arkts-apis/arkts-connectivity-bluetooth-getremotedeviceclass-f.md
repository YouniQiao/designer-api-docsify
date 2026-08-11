# getRemoteDeviceClass

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getRemoteDeviceClass

```TypeScript
function getRemoteDeviceClass(deviceId: string): DeviceClass
```

Obtains the class of a peer Bluetooth device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getRemoteDeviceClass

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getRemoteDeviceClass(deviceId: string): DeviceClass--><!--Device-bluetooth-function getRemoteDeviceClass(deviceId: string): DeviceClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |

## Examples

```TypeScript
let remoteDeviceClass : bluetooth.DeviceClass = bluetooth.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
```
