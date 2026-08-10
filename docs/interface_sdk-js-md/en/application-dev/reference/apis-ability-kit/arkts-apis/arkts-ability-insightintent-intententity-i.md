# IntentEntity

意图实体结构体定义，用于定义意图执行过程中涉及的关键信息对象，包括意图参数和意图执行结果等。

开发者通过继承该类来定义意图实体，继承类需使用  
[@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)装饰。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

<!--Device-insightIntent-interface IntentEntity--><!--Device-insightIntent-interface IntentEntity-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { insightIntent } from 'kits/@kit.AbilityKit';
```

## entityId

```TypeScript
entityId: string
```

意图实体的ID。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-IntentEntity-entityId: string--><!--Device-IntentEntity-entityId: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

