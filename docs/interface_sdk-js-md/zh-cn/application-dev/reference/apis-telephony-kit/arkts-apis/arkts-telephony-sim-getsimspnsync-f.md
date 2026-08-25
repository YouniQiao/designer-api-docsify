# getSimSpnSync

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimSpnSync

```TypeScript
function getSimSpnSync(slotId: number): string
```

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |
