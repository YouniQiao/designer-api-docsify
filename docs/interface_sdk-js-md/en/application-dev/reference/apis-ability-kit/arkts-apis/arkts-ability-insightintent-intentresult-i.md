# IntentResult

意图执行的返回结果，支持[泛型类型](../../../quick-start/introduction-to-arkts.md#泛型类和接口)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

<!--Device-insightIntent-interface IntentResult<T>--><!--Device-insightIntent-interface IntentResult<T>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { insightIntent } from 'kits/@kit.AbilityKit';
```

## code

```TypeScript
code: int
```

意图执行返回的错误码，由开发者定义。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

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

意图执行返回的结果，通常会包含需要返回给系统入口的数据。

**Type:** T

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-IntentResult-result?: T--><!--Device-IntentResult-result?: T-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

