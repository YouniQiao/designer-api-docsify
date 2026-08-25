# exitMasterProcessRole

## 导入模块

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## exitMasterProcessRole

```TypeScript
export function exitMasterProcessRole(): Promise<void>
```

放弃当前进程的[主控进程](../../../application-models/ability-terminology.md#masterprocess主控进程)身份。使用Promise异步回调。 该接口仅在2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000118](../errorcode-ability.md#16000118-当前进程非主控进程) |
| [16000119](../errorcode-ability.md#16000119-存在未完成的请求) |
