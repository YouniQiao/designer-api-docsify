# isSimActiveSync

## isSimActiveSync

```TypeScript
function isSimActiveSync(slotId: number): boolean
```

Checks whether the SIM card in a specified slot is activated.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function isSimActiveSync(slotId: int): boolean--><!--Device-sim-function isSimActiveSync(slotId: int): boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(`the sim is active:` + isSimActive);
```
