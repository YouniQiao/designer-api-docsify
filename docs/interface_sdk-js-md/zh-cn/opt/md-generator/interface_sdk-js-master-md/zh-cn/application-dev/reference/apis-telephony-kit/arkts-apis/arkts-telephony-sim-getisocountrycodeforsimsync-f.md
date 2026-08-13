# getISOCountryCodeForSimSync

## getISOCountryCodeForSimSync

```TypeScript
function getISOCountryCodeForSimSync(slotId: number): string
```

Obtains the ISO country code of the SIM card in a specified slot.

**起始版本：** 23

**废弃版本：** -1

<!--Device-sim-function getISOCountryCodeForSimSync(slotId: int): string--><!--Device-sim-function getISOCountryCodeForSimSync(slotId: int): string-End-->

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

let countryCode: string = sim.getISOCountryCodeForSimSync(0);
console.info(`the country ISO is:` + countryCode);
```
