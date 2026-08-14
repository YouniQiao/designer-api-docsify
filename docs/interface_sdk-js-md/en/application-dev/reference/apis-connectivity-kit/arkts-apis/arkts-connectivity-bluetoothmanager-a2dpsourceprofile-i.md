# A2dpSourceProfile

Manager a2dp source profile.

**Inheritance/Implementation:** A2dpSourceProfile extends [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md#BaseProfile)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [A2dpSourceProfile](arkts-connectivity-a2dp-a2dpsourceprofile-i.md#A2dpSourceProfile)

<!--Device-bluetoothManager-interface A2dpSourceProfile--><!--Device-bluetoothManager-interface A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from 'bluetoothManager';
```

## connect

```TypeScript
connect(device: string): void
```

Connect to device with a2dp. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [connect](arkts-connectivity-a2dp-a2dpsourceprofile-i-sys.md#connect)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.DISCOVER_BLUETOOTH

<!--Device-A2dpSourceProfile-connect(device: string): void--><!--Device-A2dpSourceProfile-connect(device: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device to connect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900004 | Profile not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## disconnect

```TypeScript
disconnect(device: string): void
```

Disconnect to device with a2dp. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [disconnect](arkts-connectivity-a2dp-a2dpsourceprofile-i-sys.md#disconnect)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.DISCOVER_BLUETOOTH

<!--Device-A2dpSourceProfile-disconnect(device: string): void--><!--Device-A2dpSourceProfile-disconnect(device: string): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | string | Yes | The address of the remote device to disconnect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900004 | Profile not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## getPlayingState

```TypeScript
getPlayingState(device: string): PlayingState
```

Obtains the playing state of device. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [getPlayingState](arkts-connectivity-a2dp-a2dpsourceprofile-i.md#getPlayingState)

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

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

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900004 | Profile not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let state: bluetoothManager.PlayingState  = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## off_connectionStateChange

```TypeScript
off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void
```

Unsubscribe the event reported when the profile connection state changes. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** connectionStateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

<!--Device-A2dpSourceProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void--><!--Device-A2dpSourceProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | No | Callback used to listen for event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

## on_connectionStateChange

```TypeScript
on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void
```

Subscribe the event reported when the profile connection state changes. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** connectionStateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

<!--Device-A2dpSourceProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void--><!--Device-A2dpSourceProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | Yes | Callback used to listen for event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

