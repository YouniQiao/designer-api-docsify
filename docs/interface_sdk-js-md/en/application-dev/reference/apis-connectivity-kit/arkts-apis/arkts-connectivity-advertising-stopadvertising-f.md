# stopAdvertising

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.ConnectivityKit';
```

## stopAdvertising

```TypeScript
function stopAdvertising(advertisingId: int): Promise<void>
```

停止广播ID对应的广播。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>--><!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advertisingId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示广播ID &lt;br&gt;取值应为≥0的整数，取值为当前广播的广播ID。 |

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
| 36100040 | Invalid advertising ID. |

