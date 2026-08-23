# getSimStateSync

## 导入模块

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: int): SimState
```

获取指定卡槽的SIM卡状态。

**起始版本：** 23

<!--Device-sim-function getSimStateSync(slotId: int): SimState--><!--Device-sim-function getSimStateSync(slotId: int): SimState-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | int | 是 | 卡槽ID。<br/>- 0：卡槽1。<br/>- 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SimState | 返回获取指定卡槽的SIM卡状态。 |

**示例**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```

