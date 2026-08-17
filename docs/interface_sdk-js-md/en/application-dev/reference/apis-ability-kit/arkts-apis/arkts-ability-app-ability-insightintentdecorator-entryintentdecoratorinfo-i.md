# EntryIntentDecoratorInfo

Inherits from [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#intentdecoratorinfo) and is used to describe the parameters supported by the @InsightIntentEntry decorator.

**Inheritance/Implementation:** EntryIntentDecoratorInfo extends [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#intentdecoratorinfo)

**Since:** 20

<!--Device-unnamed-declare interface EntryIntentDecoratorInfo--><!--Device-unnamed-declare interface EntryIntentDecoratorInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentLink } from 'InsightIntentLink';
import { InsightIntentPage } from 'InsightIntentPage';
import { InsightIntentFunctionMethod } from 'InsightIntentFunctionMethod';
import { InsightIntentFunction } from 'InsightIntentFunction';
import { InsightIntentEntry } from 'InsightIntentEntry';
import { LinkParamCategory } from 'LinkParamCategory';
import { InsightIntentForm } from 'InsightIntentForm';
import { InsightIntentEntity } from 'InsightIntentEntity';
```

## abilityName

```TypeScript
abilityName: string
```

Name of the ability bound to the intent.

**Type:** string

**Since:** 20

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-EntryIntentDecoratorInfo-executeMode: insightIntent.ExecuteMode[]--><!--Device-EntryIntentDecoratorInfo-executeMode: insightIntent.ExecuteMode[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

