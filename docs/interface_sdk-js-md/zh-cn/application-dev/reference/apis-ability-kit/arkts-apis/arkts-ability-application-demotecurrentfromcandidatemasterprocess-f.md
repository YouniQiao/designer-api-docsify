# demoteCurrentFromCandidateMasterProcess

## 导入模块

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## demoteCurrentFromCandidateMasterProcess

```TypeScript
export function demoteCurrentFromCandidateMasterProcess(): Promise<void>
```

撤销当前进程的备选主控进程资格。使用Promise异步回调。 该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 20

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
| [16000116](../errorcode-ability.md#16000116-当前进程已经是主控进程) |
| [16000117](../errorcode-ability.md#16000117-当前进程非备选主控进程) |
