# InvokeOptions（系统接口）

```TypeScript
interface InvokeOptions
```

Function调用的可选参数。包含Function调用时的应用上下文信息。

**起始版本：** 26.1.0

<!--Device-functionManager-interface InvokeOptions--><!--Device-functionManager-interface InvokeOptions-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## 导入模块

```TypeScript
import { functionManager, FunctionHook, InvokeFunctionParam, FunctionResultWrap } from '@kit.AbilityKit';
```

## taskId

```TypeScript
taskId?: string
```

表示任务ID，用于任务归因。取值须为[startTask](arkts-ability-taskmanager-starttask-f-sys.md)中指定的任务ID，长度范围为 1~256 个字符。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvokeOptions-taskId?: string--><!--Device-InvokeOptions-taskId?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。
