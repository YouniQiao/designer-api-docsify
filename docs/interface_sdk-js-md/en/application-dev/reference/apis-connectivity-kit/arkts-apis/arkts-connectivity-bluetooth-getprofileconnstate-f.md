# getProfileConnState

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

## getProfileConnState

```TypeScript
function getProfileConnState(profileId: ProfileId): ProfileConnectionState
```

Obtains the connection state of profile.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getProfileConnectionState](arkts-connectivity-bluetoothmanager-getprofileconnectionstate-f.md)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getProfileConnState(profileId: ProfileId): ProfileConnectionState--><!--Device-bluetooth-function getProfileConnState(profileId: ProfileId): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profileId | ProfileId | Yes | The profile id. |

**Return value:**

| Type | Description |
| --- | --- |
| ProfileConnectionState | Returns the connection state. |

**Examples**

```TypeScript
let result : bluetooth.ProfileConnectionState = bluetooth.getProfileConnState(bluetooth.ProfileId.PROFILE_A2DP_SOURCE);
```

