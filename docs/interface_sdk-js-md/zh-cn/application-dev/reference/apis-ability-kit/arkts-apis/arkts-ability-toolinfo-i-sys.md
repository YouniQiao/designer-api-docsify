# ToolInfo（系统接口）

ToolInfo describes the basic information of a cli tool.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-unnamed-export interface ToolInfo--><!--Device-unnamed-export interface ToolInfo-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## description

```TypeScript
readonly description: string
```

The description of the CLI tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly description: string--><!--Device-ToolInfo-readonly description: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## eventSchemas

```TypeScript
readonly eventSchemas?: Record<string, Record<string, Object>>
```

Schemas about custom event.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Record&lt;string, Object&gt;&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly eventSchemas?: Record<string, Record<string, Object>>--><!--Device-ToolInfo-readonly eventSchemas?: Record<string, Record<string, Object>>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## eventTypes

```TypeScript
readonly eventTypes?: Array<string>
```

Supported event types for custom event.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly eventTypes?: Array<string>--><!--Device-ToolInfo-readonly eventTypes?: Array<string>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## executablePath

```TypeScript
readonly executablePath: string
```

The executable path of the CLI tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly executablePath: string--><!--Device-ToolInfo-readonly executablePath: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## hasSubCommand

```TypeScript
readonly hasSubCommand?: boolean
```

Whether this tool has subcommand.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly hasSubCommand?: boolean--><!--Device-ToolInfo-readonly hasSubCommand?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## inputSchema

```TypeScript
readonly inputSchema: Record<string, Object>
```

The input schema of the CLI tool.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly inputSchema: Record<string, Object>--><!--Device-ToolInfo-readonly inputSchema: Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## isLockScreenExecutionAllowed

```TypeScript
readonly isLockScreenExecutionAllowed?: boolean
```

Whether the tool can be executed when the screen is locked.

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly isLockScreenExecutionAllowed?: boolean--><!--Device-ToolInfo-readonly isLockScreenExecutionAllowed?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## name

```TypeScript
readonly name: string
```

The name of the CLI tool.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly name: string--><!--Device-ToolInfo-readonly name: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## outputSchema

```TypeScript
readonly outputSchema: Record<string, Object>
```

The output schema of the CLI tool.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly outputSchema: Record<string, Object>--><!--Device-ToolInfo-readonly outputSchema: Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## requirePermissions

```TypeScript
readonly requirePermissions?: Array<string>
```

The require permissions of the CLI tool.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly requirePermissions?: Array<string>--><!--Device-ToolInfo-readonly requirePermissions?: Array<string>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## subcommands

```TypeScript
readonly subcommands?: Record<string, SubCommandInfo>
```

SubCommandInfo list.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, SubCommandInfo&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly subcommands?: Record<string, SubCommandInfo>--><!--Device-ToolInfo-readonly subcommands?: Record<string, SubCommandInfo>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## version

```TypeScript
readonly version: string
```

The version of the CLI tool (format defined by provider, e.g., "1.0.0").

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInfo-readonly version: string--><!--Device-ToolInfo-readonly version: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

