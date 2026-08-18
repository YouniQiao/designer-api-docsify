# IntentResult

Defines the return result of intent execution. The [generic type](../../../quick-start/introduction-to-arkts.md#generic-class-and-interface) is supported.

**Since:** 26.0.0

<!--Device-insightIntent-interface IntentResult--><!--Device-insightIntent-interface IntentResult-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { insightIntent } from '@kit.AbilityKit';
import { insightIntent } from '@kit.AbilityKit';
import { insightIntentDriver } from '@kit.AbilityKit';
import { insightIntentDriver } from '@kit.AbilityKit';
import { insightIntentProvider } from '@kit.AbilityKit';
import { insightIntentProvider } from '@kit.AbilityKit';
```

## code

```TypeScript
code: int
```

Error code returned by the intent execution, defined by the developer.

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IntentResult-code: int--><!--Device-IntentResult-code: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## result

```TypeScript
result?: T
```

Result data returned by the intent execution, typically containing information to be passed back to the system entry point.

**Type:** T

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IntentResult-result?: T--><!--Device-IntentResult-result?: T-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

