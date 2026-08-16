# LinkIntentDecoratorInfo

LinkIntentDecoratorInfo inherits from [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#IntentDecoratorInfo) and describes the parameters supported by the @InsightIntentLink decorator, such as the URI information required for application redirection.

**Inheritance/Implementation:** LinkIntentDecoratorInfo extends [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#IntentDecoratorInfo)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-unnamed-declare interface LinkIntentDecoratorInfo--><!--Device-unnamed-declare interface LinkIntentDecoratorInfo-End-->

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

## paramMappings

```TypeScript
paramMappings?: LinkIntentParamMapping[]
```

Mapping between intent parameters and URI information.

**Type:** [LinkIntentParamMapping](arkts-ability-app-ability-insightintentdecorator-linkintentparammapping-i.md)[]

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentDecoratorInfo-uri: string--><!--Device-LinkIntentDecoratorInfo-uri: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

