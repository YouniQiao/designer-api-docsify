# @ohos.app.ability.InsightIntentDecorator

## Modules to Import

```TypeScript
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, InsightIntentForm, InsightIntentEntity } from '@kit.AbilityKit';
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, LinkIntentParamMapping, InsightIntentEntity, InsightIntentForm } from '@kit.AbilityKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [EntryIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-entryintentdecoratorinfo-i.md) | Inherits from [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) and is used to describe the parameters supported by the @InsightIntentEntry decorator. |
| [FormIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-formintentdecoratorinfo-i.md) | Inherits from [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) and is used to describe the parameters supported by the @InsightIntentForm decorator. |
| [FunctionIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-functionintentdecoratorinfo-i.md) | Parameter type of the @InsightIntentFunctionMethod decorator. All properties inherit from [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md). |
| [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) | Common properties for intent decorators, used to define basic information about an intent (including the intent name and version number). It applies to all decorators provided by this module. |
| [IntentEntityDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intententitydecoratorinfo-i.md) | Describes the parameters supported by the @InsightIntentEntity decorator. |
| [LinkIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-linkintentdecoratorinfo-i.md) | LinkIntentDecoratorInfo inherits from [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) and describes the parameters supported by the @InsightIntentLink decorator, such as the URI information required for application redirection. |
| [LinkIntentParamMapping](arkts-ability-appabilityinsightintentdecorator-linkintentparammapping-i.md) | LinkIntentParamMapping defines the mapping between intent parameters and URI information for the @InsightIntentLink decorator. |
| [PageIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-pageintentdecoratorinfo-i.md) | PageIntentDecoratorInfo inherits from [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) and describes the parameters supported by the @InsightIntentPage decorator, such as the name of [NavDestination](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10) of the target page. |

### Enums

| Name | Description |
| --- | --- |
| [LinkParamCategory](arkts-ability-appabilityinsightintentdecorator-linkparamcategory-e.md) | Enumerates the intent parameter categories available for the @InsightIntentLink decorator. The enum is used to define how intent parameters should be passed. |

