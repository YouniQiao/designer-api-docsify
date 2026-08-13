# getSimStateSync

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: number): SimState
```

Obtains the state of the SIM card in a specified slot.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function getSimStateSync(slotId: int): SimState--><!--Device-sim-function getSimStateSync(slotId: int): SimState-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimState](arkts-telephony-sim-simstate-e.md) |

## 示例

```TypeScript
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```
