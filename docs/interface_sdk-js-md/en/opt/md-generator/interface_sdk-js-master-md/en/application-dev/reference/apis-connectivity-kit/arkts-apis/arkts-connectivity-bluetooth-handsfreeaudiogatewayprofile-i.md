# HandsFreeAudioGatewayProfile

Manager handsfree AG profile.

**Inheritance/Implementation:** HandsFreeAudioGatewayProfile extends [BaseProfile](arkts-connectivity-bluetooth-baseprofile-i.md#BaseProfile)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [HandsFreeAudioGatewayProfile](ohos.bluetoothManager/bluetoothManager.HandsFreeAudioGatewayProfile)

<!--Device-bluetooth-interface HandsFreeAudioGatewayProfile extends BaseProfile--><!--Device-bluetooth-interface HandsFreeAudioGatewayProfile extends BaseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## connect

```TypeScript
connect(device: string): boolean
```

Connect to device with hfp.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [connect](ohos.bluetoothManager/bluetoothManager.HandsFreeAudioGatewayProfile#connect)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-HandsFreeAudioGatewayProfile-connect(device: string): boolean--><!--Device-HandsFreeAudioGatewayProfile-connect(device: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.connect('XX:XX:XX:XX:XX:XX');
```

## disconnect

```TypeScript
disconnect(device: string): boolean
```

Disconnect to device with hfp.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [disconnect](ohos.bluetoothManager/bluetoothManager.HandsFreeAudioGatewayProfile#disconnect)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-HandsFreeAudioGatewayProfile-disconnect(device: string): boolean--><!--Device-HandsFreeAudioGatewayProfile-disconnect(device: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile = bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
```

## off('connectionStateChange')

```TypeScript
off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void
```

Unsubscribe the event reported when the profile connection state changes .

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [connectionStateChange](ohos.bluetoothManager/bluetoothManager.HandsFreeAudioGatewayProfile.off#event:connectionStateChange)

<!--Device-HandsFreeAudioGatewayProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void--><!--Device-HandsFreeAudioGatewayProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectionStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | No |

## on('connectionStateChange')

```TypeScript
on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void
```

Subscribe the event reported when the profile connection state changes .

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [connectionStateChange](ohos.bluetoothManager/bluetoothManager.HandsFreeAudioGatewayProfile.on#event:connectionStateChange)

<!--Device-HandsFreeAudioGatewayProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void--><!--Device-HandsFreeAudioGatewayProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectionStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | Yes |
