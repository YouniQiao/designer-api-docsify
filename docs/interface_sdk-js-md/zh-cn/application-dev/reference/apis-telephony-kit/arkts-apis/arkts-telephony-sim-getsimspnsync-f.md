# getSimSpnSync

## 导入模块

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimSpnSync

```TypeScript
function getSimSpnSync(slotId: int): string
```

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let spn: string = sim.getSimSpnSync(0);
console.info(`the sim card spn is:` + spn);
```
