# createClient

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## createClient

```TypeScript
function createClient(address: string): Client
```

创建SSAP客户端实例。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ssap-function createClient(address: string): Client--><!--Device-ssap-function createClient(address: string): Client-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string | Yes | 服务端的设备地址。例如，“11:22:33:AA:BB:FF” &lt;br&gt;长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Client](arkts-connectivity-ssap-client-i.md) | Returns a SSAP client instance { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100041 | Invalid address. |

