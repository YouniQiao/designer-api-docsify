# setSimLabelIndex (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## setSimLabelIndex

```TypeScript
function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>
```

设置SIM卡标签索引。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>--><!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| simId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示来自SIM账户信息的卡的SIM ID。 &lt;br&gt;取值范围:[1,500] |
| simLabelIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示卡的SIM标签索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setSimLabelIndex. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Nonsystem applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.setSimLabelIndex(1,  0).then(() => {
    console.info(`setSimLabelIndex success.`);
}).catch((err: BusinessError) => {
    console.error(`setSimLabelIndex failed, promise: err->${JSON.stringify(err)}`);
});
```

