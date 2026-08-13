# getProfileConnState

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getProfileConnState

```TypeScript
function getProfileConnState(profileId: ProfileId): ProfileConnectionState
```

Obtains the connection state of profile.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getProfileConnectionState](arkts-connectivity-bluetoothmanager-getprofileconnectionstate-f.md#getProfileConnectionState)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getProfileConnState(profileId: ProfileId): ProfileConnectionState--><!--Device-bluetooth-function getProfileConnState(profileId: ProfileId): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| profileId | [ProfileId](arkts-connectivity-bluetoothmanager-profileid-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ProfileConnectionState](arkts-connectivity-baseprofile-profileconnectionstate-t.md) |

## Examples

```TypeScript
let result : bluetooth.ProfileConnectionState = bluetooth.getProfileConnState(bluetooth.ProfileId.PROFILE_A2DP_SOURCE);
```
