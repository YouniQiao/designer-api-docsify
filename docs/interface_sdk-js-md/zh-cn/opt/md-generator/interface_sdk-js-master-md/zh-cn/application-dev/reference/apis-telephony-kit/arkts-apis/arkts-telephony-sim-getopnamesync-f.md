# getOpNameSync

## getOpNameSync

```TypeScript
function getOpNameSync(slotId: number): string
```

Obtains the operator name of the SIM card in a specified slot.

**起始版本：** 10

<!--Device-sim-function getOpNameSync(slotId: int): string--><!--Device-sim-function getOpNameSync(slotId: int): string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpNameSync(0);
console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
```
