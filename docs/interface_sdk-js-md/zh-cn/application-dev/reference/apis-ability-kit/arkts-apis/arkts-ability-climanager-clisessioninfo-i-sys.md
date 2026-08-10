# CliSessionInfo（系统接口）

Session information of a tool execution.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-cliManager-interface CliSessionInfo--><!--Device-cliManager-interface CliSessionInfo-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## result

```TypeScript
result?: ExecResult
```

Indicates the execution result, has a value when status is completed or failed.

**类型：** [ExecResult](arkts-ability-climanager-execresult-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CliSessionInfo-result?: ExecResult--><!--Device-CliSessionInfo-result?: ExecResult-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## sessionId

```TypeScript
sessionId: string
```

Indicates id of this session.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CliSessionInfo-sessionId: string--><!--Device-CliSessionInfo-sessionId: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## status

```TypeScript
status: SessionStatus
```

Indicates status of session.

**类型：** [SessionStatus](arkts-ability-climanager-sessionstatus-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CliSessionInfo-status: SessionStatus--><!--Device-CliSessionInfo-status: SessionStatus-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## toolName

```TypeScript
toolName: string
```

Indicates name of tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CliSessionInfo-toolName: string--><!--Device-CliSessionInfo-toolName: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

