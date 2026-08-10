# connectDevice (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## connectDevice

```TypeScript
function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>
```

基于地址连接设备

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_MECHANIC_HARDWARE

**Model restriction:** This API can be used only in the stage model.

<!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>--><!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| addrInfo | [AddressInfo](arkts-mechanic-mechanicmanager-addressinfo-i-sys.md) | Yes | 地址信息。 |
| params | [ConnectParam](arkts-mechanic-mechanicmanager-connectparam-i-sys.md) | Yes | 操作参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AttachStateChangeInfo&gt; | Promise used to return the attach state change information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 33300001 | Service exception. |

