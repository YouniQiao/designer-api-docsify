# @ohos.app.ability.InsightIntentDecorator

## 导入模块

```TypeScript
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, InsightIntentForm, InsightIntentEntity } from '@kit.AbilityKit';
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, LinkIntentParamMapping, InsightIntentEntity, InsightIntentForm } from '@kit.AbilityKit';
```

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [EntryIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-entryintentdecoratorinfo-i.md) | EntryIntentDecoratorInfo继承自[IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md)，用于描述 @InsightIntentEntry 装饰器支持的参数。 |
| [FormIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-formintentdecoratorinfo-i.md) | FormIntentDecoratorInfo继承自[IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md)，用于描述 @InsightIntentForm 装饰器支持的参数。 |
| [FunctionIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-functionintentdecoratorinfo-i.md) | @InsightIntentFunctionMethod 装饰器的参数类型，当前全部属性均继承自[IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md)。 |
| [IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md) | 意图装饰器的通用属性，用于定义意图的基本信息（包括意图名称、意图版本号）。适用于本模块的所有装饰器。 |
| [IntentEntityDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intententitydecoratorinfo-i.md) | 用于描述 @InsightIntentEntity 装饰器支持的参数。 |
| [LinkIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-linkintentdecoratorinfo-i.md) | LinkIntentDecoratorInfo继承自[IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md)，用于描述 @InsightIntentLink 装饰器支持的参数，例如应用间跳转需要的uri信息。 |
| [LinkIntentParamMapping](arkts-ability-appabilityinsightintentdecorator-linkintentparammapping-i.md) | LinkIntentParamMapping是 @InsightIntentLink 装饰器的意图参数和uri信息的映射。 |
| [PageIntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-pageintentdecoratorinfo-i.md) | PageIntentDecoratorInfo继承自[IntentDecoratorInfo](arkts-ability-appabilityinsightintentdecorator-intentdecoratorinfo-i.md)，用于描述 @InsightIntentPage 装饰器支持的参数，例如目标页面的 [NavDestination](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10)名称。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [LinkParamCategory](arkts-ability-appabilityinsightintentdecorator-linkparamcategory-e.md) | @InsightIntentLink 装饰器的意图参数类别，用于定义意图参数的传递形式。 |

