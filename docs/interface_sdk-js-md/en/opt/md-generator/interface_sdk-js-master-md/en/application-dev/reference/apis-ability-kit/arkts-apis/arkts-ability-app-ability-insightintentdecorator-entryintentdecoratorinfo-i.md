# EntryIntentDecoratorInfo

Inherits from [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#IntentDecoratorInfo) and is used to describe the parameters supported by the @InsightIntentEntry decorator.

**Inheritance/Implementation:** EntryIntentDecoratorInfo extends [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#IntentDecoratorInfo)

**Since:** 20

**Deprecated since:** -1

<!--Device-unnamed-declare interface EntryIntentDecoratorInfo--><!--Device-unnamed-declare interface EntryIntentDecoratorInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from '@kit.AbilityKit';
```

## abilityName

```TypeScript
abilityName: string
```

Name of the ability bound to the intent.

**Type:** string

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-EntryIntentDecoratorInfo-abilityName: string--><!--Device-EntryIntentDecoratorInfo-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode[]
```

Execution mode of the intent call, that is, execution mode supported when the bound ability is started.

**Type:** insightIntent.ExecuteMode[]

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-EntryIntentDecoratorInfo-executeMode: insightIntent.ExecuteMode[]--><!--Device-EntryIntentDecoratorInfo-executeMode: insightIntent.ExecuteMode[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
