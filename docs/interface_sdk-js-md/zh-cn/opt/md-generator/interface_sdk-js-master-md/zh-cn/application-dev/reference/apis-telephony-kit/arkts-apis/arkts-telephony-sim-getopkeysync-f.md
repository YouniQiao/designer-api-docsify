# getOpKeySync

## 导入模块

```TypeScript
```

## getOpKeySync

```TypeScript
function getOpKeySync(slotId: number): string
```

Obtains the operator key of the SIM card in a specified slot.

**起始版本：** 23

<!--Device-sim-function getOpKeySync(slotId: int): string--><!--Device-sim-function getOpKeySync(slotId: int): string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpKeySync(0);
console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
```
