# turnBySpeed (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## turnBySpeed

```TypeScript
function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>
```

以固定速度原地旋转

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>--><!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 具身设备ID。 &lt;br&gt;取值限定为整数。 |
| angleSpeed | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 角速度。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 转动时长，单位ms。 &lt;br&gt;取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | 202 - 非系统应用 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |
| 33300003 | Feature not supported. |

