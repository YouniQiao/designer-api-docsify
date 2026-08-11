# A2dpSourceProfile

Manager a2dp source profile.

**Inheritance/Implementation:** A2dpSourceProfile extends [BaseProfile](arkts-connectivity-a2dp-baseprofile-t.md)

**Since:** 10

<!--Device-a2dp-interface A2dpSourceProfile extends BaseProfile--><!--Device-a2dp-interface A2dpSourceProfile extends BaseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { a2dp } from 'kits/@kit.ConnectivityKit';
```

## getPlayingState

```TypeScript
getPlayingState(deviceId: string): PlayingState
```

Obtains the playing state of device.

**Since:** 10

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |
