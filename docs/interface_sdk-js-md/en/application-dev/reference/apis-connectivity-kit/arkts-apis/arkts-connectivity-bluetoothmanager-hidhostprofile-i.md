# HidHostProfile

Manager hid host profile.

**Inheritance/Implementation:** HidHostProfile extends [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [HidHostProfile](arkts-connectivity-hid-hidhostprofile-i-sys.md)

<!--Device-bluetoothManager-interface HidHostProfile--><!--Device-bluetoothManager-interface HidHostProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## off_connectionStateChange('connectionStateChange')

```TypeScript
off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void
```

Unsubscribe the event reported when the profile connection state changes. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** connectionStateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

<!--Device-HidHostProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void--><!--Device-HidHostProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | No | Callback used to listen for event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

## on_connectionStateChange('connectionStateChange')

```TypeScript
on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void
```

Subscribe the event reported when the profile connection state changes. On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** connectionStateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH

<!--Device-HidHostProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void--><!--Device-HidHostProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | Yes | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | Yes | Callback used to listen for event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

