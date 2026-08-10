# setConnectionMode (System API)

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## setConnectionMode

```TypeScript
function setConnectionMode(mode: ConnectionMode, duration: int): Promise<void>
```

设置设备的NearLink连接模式。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function setConnectionMode(mode: ConnectionMode, duration: int): Promise<void>--><!--Device-manager-function setConnectionMode(mode: ConnectionMode, duration: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [ConnectionMode](arkts-connectivity-manager-connectionmode-e-sys.md) | Yes | 需要设置的NearLink连接模式 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示设置连接模式的持续时间（以秒为单位）。值为0表示无限制 &lt;br&gt;单位为： 秒，取值应为≥0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 36100040 | Integer out of range. |

