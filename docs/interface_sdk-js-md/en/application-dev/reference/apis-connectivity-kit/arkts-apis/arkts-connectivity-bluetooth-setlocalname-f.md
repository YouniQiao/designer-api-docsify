# setLocalName

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

## setLocalName

```TypeScript
function setLocalName(name: string): boolean
```

Sets the Bluetooth friendly name of a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setLocalName](arkts-connectivity-bluetoothmanager-setlocalname-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function setLocalName(name: string): boolean--><!--Device-bluetooth-function setLocalName(name: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates a valid Bluetooth name. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
let ret : boolean = bluetooth.setLocalName('device_name');
```

