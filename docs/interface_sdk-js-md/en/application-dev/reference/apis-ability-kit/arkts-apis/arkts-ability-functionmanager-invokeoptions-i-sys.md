# InvokeOptions (System API)

```TypeScript
interface InvokeOptions
```

Optional parameters for Function invocation. Contains the application context information for the Function invocation.

**Since:** 26.1.0

<!--Device-functionManager-interface InvokeOptions--><!--Device-functionManager-interface InvokeOptions-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## Modules to Import

```TypeScript
import { functionManager, FunctionHook, InvokeFunctionParam, FunctionResultWrap } from '@kit.AbilityKit';
```

## taskId

```TypeScript
taskId?: string
```

Indicates the task ID for task attribution. The value must be the task ID specified in [startTask](arkts-ability-taskmanager-starttask-f-sys.md), which must contain 1 to 256 characters.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InvokeOptions-taskId?: string--><!--Device-InvokeOptions-taskId?: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.
