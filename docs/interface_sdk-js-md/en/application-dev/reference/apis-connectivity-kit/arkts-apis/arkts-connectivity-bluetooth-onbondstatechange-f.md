# on_bondStateChange

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

## on_bondStateChange('bondStateChange')

```TypeScript
function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void
```

Subscribe the event reported when a remote Bluetooth device is bonded.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** bondStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void--><!--Device-bluetooth-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bondStateChange' | Yes | Type of the bond state event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BondStateParam&gt; | Yes | Callback used to listen for the bond state event, [BondStateParam](arkts-connectivity-bluetooth-bondstateparam-i.md). |

**Examples**

```TypeScript
function onReceiveEvent(data : bluetooth.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
```

