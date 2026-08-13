# A2dpSourceProfile

Manager a2dp source profile.

**Inheritance/Implementation:** A2dpSourceProfile extends [BaseProfile](arkts-connectivity-bluetooth-baseprofile-i.md#BaseProfile)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [A2dpSourceProfile](arkts-connectivity-bluetoothmanager-a2dpsourceprofile-i.md#A2dpSourceProfile)

<!--Device-bluetooth-interface A2dpSourceProfile--><!--Device-bluetooth-interface A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## connect

```TypeScript
connect(device: string): boolean
```

Connect to device with a2dp.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [connect](arkts-connectivity-bluetoothmanager-a2dpsourceprofile-i.md#connect)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-A2dpSourceProfile-connect(device: string): boolean--><!--Device-A2dpSourceProfile-connect(device: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device to connect. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## disconnect

```TypeScript
disconnect(device: string): boolean
```

Disconnect to device with a2dp.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [disconnect](arkts-connectivity-bluetoothmanager-a2dpsourceprofile-i.md#disconnect)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-A2dpSourceProfile-disconnect(device: string): boolean--><!--Device-A2dpSourceProfile-disconnect(device: string): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device to disconnect. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## getPlayingState

```TypeScript
getPlayingState(device: string): PlayingState
```

Obtains the playing state of device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getPlayingState](arkts-connectivity-bluetoothmanager-a2dpsourceprofile-i.md#getPlayingState)

<!--Device-A2dpSourceProfile-getPlayingState(device: string): PlayingState--><!--Device-A2dpSourceProfile-getPlayingState(device: string): PlayingState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device. |

**Return value:**

| Type | Description |
| --- | --- |
| PlayingState | Returns { |

## off_connectionStateChange

```TypeScript
off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void
```

Unsubscribe the event reported when the profile connection state changes .

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** connectionStateChange

<!--Device-A2dpSourceProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void--><!--Device-A2dpSourceProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | No | Callback used to listen for event. |

## on_connectionStateChange

```TypeScript
on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void
```

Subscribe the event reported when the profile connection state changes .

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** connectionStateChange

<!--Device-A2dpSourceProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void--><!--Device-A2dpSourceProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | Yes | Callback used to listen for event. |

