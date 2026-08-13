# getRemoteDeviceName

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getRemoteDeviceName

```TypeScript
function getRemoteDeviceName(deviceId: string): string
```

Obtains the name of a peer Bluetooth device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRemoteDeviceName](arkts-connectivity-bluetoothmanager-getremotedevicename-f.md#getRemoteDeviceName)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getRemoteDeviceName(deviceId: string): string--><!--Device-bluetooth-function getRemoteDeviceName(deviceId: string): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let remoteDeviceName : string = bluetooth.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
```
