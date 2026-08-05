# IntentResult

Defines the return result of intent execution. The \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ is supported.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

<!--Device-insightIntent-interface IntentResult<T>--><!--Device-insightIntent-interface IntentResult<T>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## code

```TypeScript
code: int
```

Error code returned by the intent execution, defined by the developer.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-IntentResult-code: int--><!--Device-IntentResult-code: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## result

```TypeScript
result?: T
```

Result data returned by the intent execution, typically containing information to be passed back to the system entry point.

**Type:** T

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-IntentResult-result?: T--><!--Device-IntentResult-result?: T-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

