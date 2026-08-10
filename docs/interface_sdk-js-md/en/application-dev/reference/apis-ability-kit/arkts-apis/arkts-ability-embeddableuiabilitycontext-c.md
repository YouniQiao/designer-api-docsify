# EmbeddableUIAbilityContext

EmbeddableUIAbilityContext是  
[EmbeddableUIAbility](arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md)组件的上下文，继承自  
[UIAbilityContext](arkts-ability-uiabilitycontext-c.md)。

每个EmbeddableUIAbility组件实例化时，系统都会自动创建对应的EmbeddableUIAbilityContext。

> **说明：**
> 
> - 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

**Inheritance/Implementation:** EmbeddableUIAbilityContext extends [UIAbilityContext](arkts-ability-uiabilitycontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export default class EmbeddableUIAbilityContext extends UIAbilityContext--><!--Device-unnamed-export default class EmbeddableUIAbilityContext extends UIAbilityContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

