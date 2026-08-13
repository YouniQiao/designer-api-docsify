# HandsFreeAudioGatewayProfile

Manager hfp source profile.

**Inheritance/Implementation:** HandsFreeAudioGatewayProfile extends [BaseProfile](arkts-connectivity-hfp-baseprofile-t.md#BaseProfile)

**Since:** 23

**Deprecated since:** -1

<!--Device-hfp-interface HandsFreeAudioGatewayProfile--><!--Device-hfp-interface HandsFreeAudioGatewayProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { hfp } from '@kit.ConnectivityKit';
```

## connect

```TypeScript
connect(deviceId: string): void
```

Initiate an HFP connection to a remote device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-HandsFreeAudioGatewayProfile-connect(deviceId: string): void--><!--Device-HandsFreeAudioGatewayProfile-connect(deviceId: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

## disconnect

```TypeScript
disconnect(deviceId: string): void
```

Disconnect the HFP connection with the remote device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-HandsFreeAudioGatewayProfile-disconnect(deviceId: string): void--><!--Device-HandsFreeAudioGatewayProfile-disconnect(deviceId: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |
