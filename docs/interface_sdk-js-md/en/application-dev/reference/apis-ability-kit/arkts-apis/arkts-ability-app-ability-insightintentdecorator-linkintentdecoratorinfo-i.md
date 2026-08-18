# LinkIntentDecoratorInfo

LinkIntentDecoratorInfo inherits from [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md) and describes the parameters supported by the @InsightIntentLink decorator, such as the URI information required for application redirection.

**Inheritance/Implementation:** LinkIntentDecoratorInfo extends [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md)

**Since:** 20

<!--Device-unnamed-declare interface LinkIntentDecoratorInfo--><!--Device-unnamed-declare interface LinkIntentDecoratorInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, InsightIntentForm, InsightIntentEntity } from '@kit.AbilityKit';
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, LinkIntentParamMapping, InsightIntentEntity, InsightIntentForm } from '@kit.AbilityKit';
```

## paramMappings

```TypeScript
paramMappings?: LinkIntentParamMapping[]
```

Mapping between intent parameters and URI information.

**Type:** [LinkIntentParamMapping](../../apis-na/arkts-apis/arkts-na-app-ability-insightintentdecorator-linkintentparammapping-i.md)[]

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentDecoratorInfo-paramMappings?: LinkIntentParamMapping[]--><!--Device-LinkIntentDecoratorInfo-paramMappings?: LinkIntentParamMapping[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uri

```TypeScript
uri: string
```

URI information associated with the intent.

**Type:** string

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentDecoratorInfo-uri: string--><!--Device-LinkIntentDecoratorInfo-uri: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

