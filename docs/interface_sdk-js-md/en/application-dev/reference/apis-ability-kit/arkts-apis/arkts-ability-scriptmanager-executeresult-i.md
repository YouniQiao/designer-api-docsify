# ExecuteResult

Result of arkTS script execution.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-scriptManager-interface ExecuteResult--><!--Device-scriptManager-interface ExecuteResult-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## code

```TypeScript
code: number
```

Indicates result code.The value range is all integers.

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExecuteResult-code: number--><!--Device-ExecuteResult-code: number-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## flags

```TypeScript
flags?: number
```

Indicates the URIs read and write permissions which consistent with \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_,flags must be one of \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_,\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_,\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_|\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_.The value range is all integers.

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExecuteResult-flags?: number--><!--Device-ExecuteResult-flags?: number-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## result

```TypeScript
result?: Record<string, Object>
```

Indicates execute result.

**Type:** Record&lt;string, Object&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExecuteResult-result?: Record<string, Object>--><!--Device-ExecuteResult-result?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

## uris

```TypeScript
uris?: Array<string>
```

Indicates the URIs will be authorized to the caller.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExecuteResult-uris?: Array<string>--><!--Device-ExecuteResult-uris?: Array<string>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

