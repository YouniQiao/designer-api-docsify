# RemoteDevice

Remote device operation methods.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-remoteDevice-interface RemoteDevice--><!--Device-remoteDevice-interface RemoteDevice-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## getAcbState

```TypeScript
getAcbState(): AcbState
```

Gets the ACB connection state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getAcbState(): AcbState--><!--Device-RemoteDevice-getAcbState(): AcbState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| AcbState | Returns the ACB connection state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## getConnectionState

```TypeScript
getConnectionState(): ConnectionState
```

Gets the profile connection state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getConnectionState(): ConnectionState--><!--Device-RemoteDevice-getConnectionState(): ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| ConnectionState | Returns the connection state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## getDeviceClass

```TypeScript
getDeviceClass(): DeviceClass
```

Gets the type of the NearLink device.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceClass(): DeviceClass--><!--Device-RemoteDevice-getDeviceClass(): DeviceClass-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| DeviceClass | Indicates the type of the NearLink device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## getDeviceInformation

```TypeScript
getDeviceInformation(): DeviceInformation
```

Obtains the remote device information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation--><!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) | Returns the remote device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## getDeviceName

```TypeScript
getDeviceName(): string
```

Gets the name of the NearLink device.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceName(): string--><!--Device-RemoteDevice-getDeviceName(): string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the device name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## getPairingState

```TypeScript
getPairingState(): PairingState
```

Gets the pairing state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getPairingState(): PairingState--><!--Device-RemoteDevice-getPairingState(): PairingState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| PairingState | Returns the pairing state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## startPairing

```TypeScript
startPairing(): Promise<void>
```

Initiate pairing to remote NearLink device.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-startPairing(): Promise<void>--><!--Device-RemoteDevice-startPairing(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

