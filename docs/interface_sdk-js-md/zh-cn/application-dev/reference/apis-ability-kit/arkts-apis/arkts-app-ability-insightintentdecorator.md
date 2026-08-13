# @ohos.app.ability.InsightIntentDecorator(意图装饰器定义)

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [InsightIntentEntity](arkts-ability-app-ability-insightintentdecorator-insightintententity-i.md) | 使用该注解装饰一个继承自[IntentEntity](arkts-ability-insightintent-intententity-i.md#IntentEntity)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentEntity](arkts-ability-app-ability-insightintentdecorator-insightintententity-i.md#InsightIntentEntity)。 |
| [InsightIntentEntry](arkts-ability-app-ability-insightintentdecorator-insightintententry-i.md) | 使用该注解装饰一个继承自  [InsightIntentEntryExecutor](arkts-ability-app-ability-insightintententryexecutor-insightintententryexecutor-c.md#InsightIntentEntryExecutor)的类，实现意图操作并配置意图依赖的Ability组件，便于AI入口拉起依赖的Ability组件时，执行对应的意图操作。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentEntry](arkts-ability-app-ability-insightintentdecorator-insightintententry-i.md#InsightIntentEntry)。 |
| [InsightIntentForm](arkts-ability-app-ability-insightintentdecorator-insightintentform-i.md) | 使用该注解装饰[FormExtensionAbility](@ohos.app.form.FormExtensionAbility)并配置FormExtensionAbility绑定的卡片名称，便于AI入口通过意图添加卡片。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentForm](arkts-ability-app-ability-insightintentdecorator-insightintentform-i.md#InsightIntentForm)。 |
| [InsightIntentFunction](arkts-ability-app-ability-insightintentdecorator-insightintentfunction-i.md) | 该注解与@InsightIntentFunctionMethod注解必须组合使用。使用该注解来装饰类，同时使用@InsightIntentFunctionMethod注解来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentFunction](arkts-ability-app-ability-insightintentdecorator-insightintentfunction-i.md#InsightIntentFunction)。 |
| [InsightIntentFunctionMethod](arkts-ability-app-ability-insightintentdecorator-insightintentfunctionmethod-i.md) | 该注解与@InsightIntentFunction注解必须组合使用。使用该注解来装饰类中的静态函数，同时使用@InsightIntentFunction注解来装饰静态函数所属的类，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentFunctionMethod](arkts-ability-app-ability-insightintentdecorator-insightintentfunctionmethod-i.md#InsightIntentFunctionMethod)。 |
| [InsightIntentLink](arkts-ability-app-ability-insightintentdecorator-insightintentlink-i.md) | 用于描述ArkTS-Sta中[@InsightIntentLink](arkts-ability-app-ability-insightintentdecorator-insightintentlink-i.md#InsightIntentLink)支持的参数，用于定义意图的所有信息（包括意图名称、意图版本号）。使用该注解装饰当前应用的uri链接，可以将该uri链接定义为意图，便于AI入口通过定义的意图快速跳转到当前应用。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentLink](arkts-ability-app-ability-insightintentdecorator-insightintentlink-i.md#InsightIntentLink)。 |
| [InsightIntentPage](arkts-ability-app-ability-insightintentdecorator-insightintentpage-i.md) | 使用该注解装饰当前应用的页面，可以将页面定义为意图，便于AI入口通过意图快速跳转到指定页面。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  [@InsightIntentPage](arkts-ability-app-ability-insightintentdecorator-insightintentpage-i.md#InsightIntentPage)。 |
| [LinkIntentParamMapping](arkts-ability-app-ability-insightintentdecorator-linkintentparammapping-i.md) | LinkIntentParamMapping是[@InsightIntentLink](arkts-ability-app-ability-insightintentdecorator-insightintentlink-i.md#InsightIntentLink)装饰器的意图参数和URI信息的映射。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [LinkParamCategory](arkts-ability-app-ability-insightintentdecorator-linkparamcategory-e.md) | [@InsightIntentLink](arkts-ability-app-ability-insightintentdecorator-insightintentlink-i.md#InsightIntentLink)装饰器的意图参数类别，用于定义意图参数的传递形式。 |

