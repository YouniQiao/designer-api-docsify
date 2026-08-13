# getSimLabelSync

## getSimLabelSync

```TypeScript
function getSimLabelSync(slotId: number): SimLabel
```

Obtains the SIM card label synchronously.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function getSimLabelSync(slotId: int): SimLabel--><!--Device-sim-function getSimLabelSync(slotId: int): SimLabel-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) |

## 示例

```TypeScript
import { sim } from '@kit.TelephonyKit';


let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
console.info(`The sim state is:` + simLabel);
```
