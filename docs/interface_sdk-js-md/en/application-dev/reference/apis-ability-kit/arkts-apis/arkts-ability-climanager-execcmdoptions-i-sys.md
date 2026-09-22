# ExecCmdOptions

```TypeScript
interface ExecCmdOptions
```

Describes the options for executing a raw command string via [execCmd](arkts-ability-climanager-execcmd-f.md).

**Since:** 26.0.1

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## Modules to Import

```TypeScript
import { cliManager, CliHook, ExecToolParam, ExecCmdParam, ExecResultWrap } from '@kit.AbilityKit';
```

## challenge

```TypeScript
challenge?: string
```

Indicates the unique identifier obtained from the access token manager.

**Type:** string

**Default:** ""

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## isShellCommand

```TypeScript
isShellCommand?: boolean
```

Indicates whether the command is executed as a shell command.

**Type:** boolean

**Default:** true

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.
