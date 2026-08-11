# getProfile

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getProfile

```TypeScript
function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile
```

Obtains the instance of profile.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getProfileInstance

<!--Device-bluetooth-function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile--><!--Device-bluetooth-function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| profileId | [ProfileId](arkts-connectivity-constant-profileid-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [A2dpSourceProfile](arkts-connectivity-a2dp-a2dpsourceprofile-i.md) |

## Examples

```TypeScript
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
```
