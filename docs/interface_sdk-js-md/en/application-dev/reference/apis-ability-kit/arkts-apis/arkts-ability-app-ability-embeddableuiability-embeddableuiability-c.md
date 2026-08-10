# EmbeddableUIAbility

EmbeddableUIAbility组件是为原子化服务提供可嵌入式的UIAbility组件，继承自[UIAbility](arkts-app-ability-uiability.md)。开发者通过实现EmbeddableUIAbility，为其他应用提供跳出式启动和嵌入式启动原子化服务方式。各类Ability的继承关系详见[继承关系说明](../../../reference/apis-ability-kit/js-apis-app-ability-ability.md#ability的继承关系说明)。

**Inheritance/Implementation:** EmbeddableUIAbility extends [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export default class EmbeddableUIAbility extends UIAbility--><!--Device-unnamed-export default class EmbeddableUIAbility extends UIAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { EmbeddableUIAbility } from 'kits/@kit.AbilityKit';
```

## context

```TypeScript
context: EmbeddableUIAbilityContext
```

EmbeddableUIAbility组件的上下文。

**Type:** [EmbeddableUIAbilityContext](arkts-ability-embeddableuiabilitycontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EmbeddableUIAbility-context: EmbeddableUIAbilityContext--><!--Device-EmbeddableUIAbility-context: EmbeddableUIAbilityContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

