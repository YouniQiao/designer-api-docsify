# getSimSpnSync

## getSimSpnSync

```TypeScript
function getSimSpnSync(slotId: number): string
```

Obtains the service provider name (SPN) of the SIM card in a specified slot.

&lt;p&gt;The value is recorded in the EFSPN file of the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**起始版本：** 10

<!--Device-sim-function getSimSpnSync(slotId: int): string--><!--Device-sim-function getSimSpnSync(slotId: int): string-End-->

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

let spn: string = sim.getSimSpnSync(0);
console.info(`the sim card spn is:` + spn);
```
