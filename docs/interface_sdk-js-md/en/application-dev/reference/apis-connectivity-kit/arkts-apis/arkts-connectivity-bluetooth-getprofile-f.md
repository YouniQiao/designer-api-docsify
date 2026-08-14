# getProfile

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## getProfile

```TypeScript
function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile
```

Obtains the instance of profile.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getProfileInstance](arkts-connectivity-bluetoothmanager-getprofileinstance-f.md#getProfileInstance)

<!--Device-bluetooth-function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile--><!--Device-bluetooth-function getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profileId | ProfileId | Yes | The profile id.. |

**Return value:**

| Type | Description |
| --- | --- |
| A2dpSourceProfile | Returns instance of profile. |

## Examples

```TypeScript
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
```

