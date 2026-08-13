# getSimOperatorNumericSync

## getSimOperatorNumericSync

```TypeScript
function getSimOperatorNumericSync(slotId: number): string
```

Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function getSimOperatorNumericSync(slotId: int): string--><!--Device-sim-function getSimOperatorNumericSync(slotId: int): string-End-->

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

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(`the sim operator numeric is:` + numeric);
```
