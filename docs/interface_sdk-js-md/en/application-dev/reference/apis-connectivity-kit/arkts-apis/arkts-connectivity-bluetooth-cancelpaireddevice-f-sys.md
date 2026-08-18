# cancelPairedDevice (System API)

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
import { access } from '@kit.ConnectivityKit';
import { baseProfile } from '@kit.ConnectivityKit';
import { ble } from '@kit.ConnectivityKit';
import { connection } from '@kit.ConnectivityKit';
import { constant } from '@kit.ConnectivityKit';
import { hfp } from '@kit.ConnectivityKit';
import { hid } from '@kit.ConnectivityKit';
import { bas } from '@kit.ConnectivityKit';
import { common } from '@kit.ConnectivityKit';
import { bluetooth } from '@kit.ConnectivityKit';
import { map } from '@kit.ConnectivityKit';
import { pan } from '@kit.ConnectivityKit';
import { pbap } from '@kit.ConnectivityKit';
import { opp } from '@kit.ConnectivityKit';
import { socket } from '@kit.ConnectivityKit';
import { wearDetection } from '@kit.ConnectivityKit';
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## cancelPairedDevice

```TypeScript
function cancelPairedDevice(deviceId: string): boolean
```

Remove a paired remote device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [cancelPairedDevice](arkts-connectivity-bluetoothmanager-cancelpaireddevice-f-sys.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function cancelPairedDevice(deviceId: string): boolean--><!--Device-bluetooth-function cancelPairedDevice(deviceId: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | The address of the remote device to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
let result : boolean = bluetooth.cancelPairedDevice("XX:XX:XX:XX:XX:XX");
```

