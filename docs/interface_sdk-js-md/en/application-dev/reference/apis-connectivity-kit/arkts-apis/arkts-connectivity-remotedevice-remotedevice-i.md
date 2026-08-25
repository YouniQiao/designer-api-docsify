# RemoteDevice

Provides the method for operating on a remote device. Before using this method, you need to call [remoteDevice.createRemoteDevice](arkts-connectivity-remotedevice-createremotedevice-f.md) to create a [RemoteDevice](#remotedevice) instance. You need to create only one instance for a device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from '@kit.ConnectivityKit';
```

## getAcbState

```TypeScript
getAcbState(): AcbState
```

Obtains the logical link connection status with a remote device. This method is applicable when you need to check whether a logical link is ready, for example, checking the logical link status before data transfer or message communication. Unlike [getConnectionState](#getconnectionstate) which obtains the connection status at the device level, this API obtains the connection status at the logical link (ACB) level.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AcbState](arkts-connectivity-remotedevice-acbstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## getConnectionState

```TypeScript
getConnectionState(): ConnectionState
```

Obtains the connection status between the local and remote devices. Unlike [getAcbState](#getacbstate) which obtains the connection status at the logical link (ACB) level, this API obtains the connection status at the device level.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## getDeviceClass

```TypeScript
getDeviceClass(): DeviceClass
```

Obtains the type of a remote device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## getDeviceInformation

```TypeScript
getDeviceInformation(): DeviceInformation
```

Obtains the information of a remote device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## getDeviceName

```TypeScript
getDeviceName(): string
```

Obtains the name of a remote device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## getPairingState

```TypeScript
getPairingState(): PairingState
```

Obtains the pairing status with a remote device.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PairingState](arkts-connectivity-nearlinkconstant-pairingstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |

## startPairing

```TypeScript
startPairing(): Promise<void>
```

Initiates pairing with a remote device. This API uses a promise to return the result. After the pairing is initiated, different types of dialog boxes will be displayed based on the input and output capability IDs of the local and remote devices, for example, whether the devices have the display and keyboard input capabilities. The user will need to confirm the pairing.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100003 |
| 36100099 |
