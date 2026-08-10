# isSupported

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## isSupported

```TypeScript
function isSupported(slotId: int): boolean
```

Whether embedded subscriptions are currently supported.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-eSIM-function isSupported(slotId: int): boolean--><!--Device-eSIM-function isSupported(slotId: int): boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 3120002 | System internal error. |
| 3120001 | Service connection failed. |

## 示例

```TypeScript
import { eSIM } from '@kit.TelephonyKit';

let isSupported: boolean = eSIM.isSupported(1);
console.info(`the esim is Supported:` + isSupported);
```

