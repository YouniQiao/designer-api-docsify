# ExecResult（系统接口）

Execute result of a tool execution.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-cliManager-interface ExecResult--><!--Device-cliManager-interface ExecResult-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## errorText

```TypeScript
errorText?: string
```

Indicates the error output of the tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-errorText?: string--><!--Device-ExecResult-errorText?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## executionTime

```TypeScript
executionTime: long
```

Indicates the execution duration in milliseconds.

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-executionTime: long--><!--Device-ExecResult-executionTime: long-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## exitCode

```TypeScript
exitCode?: int
```

Indicates the exit code, 0 means success.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-exitCode?: int--><!--Device-ExecResult-exitCode?: int-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## outputText

```TypeScript
outputText?: string
```

Indicates the standard output of the tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-outputText?: string--><!--Device-ExecResult-outputText?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## signalNumber

```TypeScript
signalNumber?: int
```

Indicates the termination signal (if the tool process was terminated by a signal).

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-signalNumber?: int--><!--Device-ExecResult-signalNumber?: int-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## timeOut

```TypeScript
timeOut: boolean
```

Indicates whether it timed out. true means timeout occurred, false means no timeout.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExecResult-timeOut: boolean--><!--Device-ExecResult-timeOut: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

