# getSimLabelSync

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimLabelSync

```TypeScript
function getSimLabelSync(slotId: number): SimLabel
```

通过传入SIM卡槽的ID，获取对应的SIM卡标签。

**起始版本：** 20

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) |
