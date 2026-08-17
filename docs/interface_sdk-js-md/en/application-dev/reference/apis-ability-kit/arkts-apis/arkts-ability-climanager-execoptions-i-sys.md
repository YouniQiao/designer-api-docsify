# ExecOptions (System API)

Tool execution options.

**Since:** 26.0.0

<!--Device-cliManager-interface ExecOptions--><!--Device-cliManager-interface ExecOptions-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cliManager } from 'cliManager';
```

## background

```TypeScript
background?: boolean
```

Indicates whether the tool is executed in the background.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecOptions-background?: boolean--><!--Device-ExecOptions-background?: boolean-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## timeout

```TypeScript
timeout?: long
```

Indicates the maximum execution time of the tool, in seconds.

**Type:** long

**Default:** 1800

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecOptions-timeout?: long--><!--Device-ExecOptions-timeout?: long-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## yieldMs

```TypeScript
yieldMs?: long
```

Indicates the foreground waiting timeout in milliseconds.

**Type:** long

**Default:** 0

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExecOptions-yieldMs?: long--><!--Device-ExecOptions-yieldMs?: long-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

