# hasSimCardSync

## hasSimCardSync

```TypeScript
function hasSimCardSync(slotId: number): boolean
```

Checks whether a SIM card is inserted in a specified slot.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function hasSimCardSync(slotId: int): boolean--><!--Device-sim-function hasSimCardSync(slotId: int): boolean-End-->

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

let hasSimCard: boolean = sim.hasSimCardSync(0);
console.info(`has sim card: ` + hasSimCard);
```
