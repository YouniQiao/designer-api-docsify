# FunctionInfo (System API)

FunctionInfo describes the basic information of a CLI function.

**Since:** 26.0.0

<!--Device-unnamed-export interface FunctionInfo--><!--Device-unnamed-export interface FunctionInfo-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## description

```TypeScript
readonly description: string
```

Human-readable function description, used for AI Agent decision-making.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly description: string--><!--Device-FunctionInfo-readonly description: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## functionName

```TypeScript
readonly functionName: string
```

The name of the function.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly functionName: string--><!--Device-FunctionInfo-readonly functionName: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## functionNamespace

```TypeScript
readonly functionNamespace: string
```

The namespace of the function.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly functionNamespace: string--><!--Device-FunctionInfo-readonly functionNamespace: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## inputSchema

```TypeScript
readonly inputSchema?: string
```

Input parameter JSON Schema, describes the structure of parameters accepted by the function.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly inputSchema?: string--><!--Device-FunctionInfo-readonly inputSchema?: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## outputSchema

```TypeScript
readonly outputSchema?: string
```

Output result JSON Schema (optional), describes the structure of the function return value.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly outputSchema?: string--><!--Device-FunctionInfo-readonly outputSchema?: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## version

```TypeScript
readonly version: string
```

The version of the function (format defined by provider, e.g., "1.0.0").

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FunctionInfo-readonly version: string--><!--Device-FunctionInfo-readonly version: string-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

