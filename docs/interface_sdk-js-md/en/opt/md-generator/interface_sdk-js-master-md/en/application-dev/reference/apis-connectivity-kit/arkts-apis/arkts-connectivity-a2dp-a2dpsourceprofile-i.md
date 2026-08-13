# A2dpSourceProfile

Manager a2dp source profile.

**Inheritance/Implementation:** A2dpSourceProfile extends [BaseProfile](arkts-connectivity-a2dp-baseprofile-t.md#BaseProfile)

**Since:** 23

**Deprecated since:** -1

<!--Device-a2dp-interface A2dpSourceProfile--><!--Device-a2dp-interface A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
```

## getPlayingState

```TypeScript
getPlayingState(deviceId: string): PlayingState
```

Obtains the playing state of device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-A2dpSourceProfile-getPlayingState(deviceId: string): PlayingState--><!--Device-A2dpSourceProfile-getPlayingState(deviceId: string): PlayingState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PlayingState](arkts-connectivity-a2dp-playingstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |
