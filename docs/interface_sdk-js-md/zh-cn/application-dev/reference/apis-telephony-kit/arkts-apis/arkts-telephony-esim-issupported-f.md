# isSupported

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## isSupported

```TypeScript
function isSupported(slotId: number): boolean
```

获取指定卡槽是否支持eSIM功能。

**起始版本：** 18

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3120001](../errorcode-telephony.md#3120001-服务连接失败) |
| [3120002](../errorcode-telephony.md#3120002-系统内部错误) |
