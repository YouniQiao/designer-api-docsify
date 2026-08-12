# RemoteDevice

Remote device operation methods.

**Since:** 26.0.0

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

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getAcbState(): AcbState--><!--Device-RemoteDevice-getAcbState(): AcbState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AcbState](arkts-connectivity-remotedevice-acbstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## getConnectionState

```TypeScript
getConnectionState(): ConnectionState
```

Gets the profile connection state.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getConnectionState(): ConnectionState--><!--Device-RemoteDevice-getConnectionState(): ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## getDeviceClass

```TypeScript
getDeviceClass(): DeviceClass
```

Gets the type of the NearLink device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceClass(): DeviceClass--><!--Device-RemoteDevice-getDeviceClass(): DeviceClass-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceClass](arkts-connectivity-connection-deviceclass-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## getDeviceInformation

```TypeScript
getDeviceInformation(): DeviceInformation
```

Obtains the remote device information.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation--><!--Device-RemoteDevice-getDeviceInformation(): DeviceInformation-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## getDeviceName

```TypeScript
getDeviceName(): string
```

Gets the name of the NearLink device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getDeviceName(): string--><!--Device-RemoteDevice-getDeviceName(): string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## getPairingState

```TypeScript
getPairingState(): PairingState
```

Gets the pairing state.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-getPairingState(): PairingState--><!--Device-RemoteDevice-getPairingState(): PairingState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PairingState](arkts-connectivity-nearlinkconstant-pairingstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## startPairing

```TypeScript
startPairing(): Promise<void>
```

Initiate pairing to remote NearLink device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoteDevice-startPairing(): Promise<void>--><!--Device-RemoteDevice-startPairing(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
