# ExecOptions（系统接口）

Tool execution options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-cliManager-interface ExecOptions--><!--Device-cliManager-interface ExecOptions-End-->

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

Indicates whether the tool is executed in the background.

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecOptions-background?: boolean--><!--Device-ExecOptions-background?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## timeout

```TypeScript
timeout?: long
```

Indicates the maximum execution time of the tool, in seconds.

**类型：** long

**默认值：** 1800

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecOptions-timeout?: long--><!--Device-ExecOptions-timeout?: long-End-->

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

<!--Device-ExecOptions-yieldMs?: long--><!--Device-ExecOptions-yieldMs?: long-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

