# ExecCmdOptions（系统接口）

Options for executing a command.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-cliManager-interface ExecCmdOptions--><!--Device-cliManager-interface ExecCmdOptions-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## background

```TypeScript
background?: boolean
```

Indicates whether the command is executed in the background.

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-background?: boolean--><!--Device-ExecCmdOptions-background?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## callback

```TypeScript
callback?: ToolEventCallback
```

Indicates the event callback for receiving tool events. If provided, auto-subscribe is performed.

**类型：** [ToolEventCallback](arkts-ability-tooleventcallback-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-callback?: ToolEventCallback--><!--Device-ExecCmdOptions-callback?: ToolEventCallback-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## env

```TypeScript
env?: Record<string, string>
```

Indicates the environment variables for the command.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-env?: Record<string, string>--><!--Device-ExecCmdOptions-env?: Record<string, string>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## policy

```TypeScript
policy?: string
```

Indicates the security policy.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-policy?: string--><!--Device-ExecCmdOptions-policy?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## timeout

```TypeScript
timeout?: long
```

Indicates the maximum execution time of the command, in seconds.

**类型：** long

**默认值：** 1800

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-timeout?: long--><!--Device-ExecCmdOptions-timeout?: long-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## workDir

```TypeScript
workDir?: string
```

Indicates the working directory for the command.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-workDir?: string--><!--Device-ExecCmdOptions-workDir?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## yieldMs

```TypeScript
yieldMs?: long
```

Indicates the foreground waiting timeout in milliseconds.

**类型：** long

**默认值：** 0

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecCmdOptions-yieldMs?: long--><!--Device-ExecCmdOptions-yieldMs?: long-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

