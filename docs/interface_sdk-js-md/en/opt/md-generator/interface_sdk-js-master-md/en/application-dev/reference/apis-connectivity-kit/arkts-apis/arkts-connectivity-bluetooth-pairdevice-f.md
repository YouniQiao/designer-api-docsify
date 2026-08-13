# pairDevice

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## pairDevice

```TypeScript
function pairDevice(deviceId: string): boolean
```

Starts pairing with a remote Bluetooth device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [pairDevice](arkts-connectivity-bluetoothmanager-pairdevice-f.md#pairDevice)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function pairDevice(deviceId: string): boolean--><!--Device-bluetooth-function pairDevice(deviceId: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// The address can be scanned.
let result : boolean = bluetooth.pairDevice("XX:XX:XX:XX:XX:XX");
```
