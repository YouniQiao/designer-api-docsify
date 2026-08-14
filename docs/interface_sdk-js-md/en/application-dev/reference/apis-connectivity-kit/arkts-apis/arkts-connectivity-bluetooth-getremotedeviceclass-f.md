# getRemoteDeviceClass

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## getRemoteDeviceClass

```TypeScript
function getRemoteDeviceClass(deviceId: string): DeviceClass
```

Obtains the class of a peer Bluetooth device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getRemoteDeviceClass](arkts-connectivity-bluetoothmanager-getremotedeviceclass-f.md#getRemoteDeviceClass)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getRemoteDeviceClass(deviceId: string): DeviceClass--><!--Device-bluetooth-function getRemoteDeviceClass(deviceId: string): DeviceClass-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | The address of the remote device. |

**Return value:**

| Type | Description |
| --- | --- |
| DeviceClass | The class of the remote device, { |

## Examples

```TypeScript
let remoteDeviceClass : bluetooth.DeviceClass = bluetooth.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
```

