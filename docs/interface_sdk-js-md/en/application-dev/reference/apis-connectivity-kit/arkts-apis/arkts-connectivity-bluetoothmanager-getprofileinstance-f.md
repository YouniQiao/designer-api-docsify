# getProfileInstance

## Modules to Import

```TypeScript
import { bluetoothManager } from 'bluetoothManager';
```

## getProfileInstance

```TypeScript
function getProfileInstance(
    profileId: ProfileId
  ): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile
```

Obtains the instance of profile.

**Since:** 9

**Deprecated since:** 10

<!--Device-bluetoothManager-function getProfileInstance(    profileId: ProfileId  ): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile--><!--Device-bluetoothManager-function getProfileInstance(    profileId: ProfileId  ): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profileId | ProfileId | Yes | The profile id.. |

**Return value:**

| Type | Description |
| --- | --- |
| A2dpSourceProfile | Returns the instance of profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

