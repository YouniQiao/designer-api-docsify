# getSimStateSync

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: number): SimState
```

获取指定卡槽的SIM卡状态。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimState](arkts-telephony-sim-simstate-e.md) |
