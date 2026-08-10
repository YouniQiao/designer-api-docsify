# BaseContext

BaseContext抽象类用于表示继承的子类Context是Stage模型还是FA模型，是所有Context类型的父类。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export default abstract class BaseContext--><!--Device-unnamed-export default abstract class BaseContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## stageMode

```TypeScript
stageMode: boolean
```

表示是否Stage模型。&lt;br&gt;true：[Stage模型](../../../application-models/ability-terminology.md#stage模型)。&lt;br&gt;false：  
[FA模型](../../../application-models/ability-terminology.md#fa模型)。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BaseContext-stageMode: boolean--><!--Device-BaseContext-stageMode: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

