# InsightIntentPage

使用该注解装饰当前应用的页面，可以将页面定义为意图，便于AI入口通过意图快速跳转到指定页面。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  
[@InsightIntentPage](#InsightIntentPage)。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentPage--><!--Device-unnamed-export @interface InsightIntentPage-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## displayDescription

```TypeScript
displayDescription: string = ''
```

表示显示给用户的意图描述。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-displayDescription: string = ''--><!--Device-InsightIntentPage-displayDescription: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## displayName

```TypeScript
displayName: string
```

表示显示给用户的意图名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-displayName: string--><!--Device-InsightIntentPage-displayName: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## domain

```TypeScript
domain: string
```

表示意图垂域，用于将意图按垂直领域分类（例如：视频、音乐、游戏），取值范围参见  
[各垂域的智慧分发特性列表](https://developer.huawei.com/consumer/cn/doc/service/intents-ai-distribution-characteristic-0000001901922213#section2656133582215)中的垂域字段。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-domain: string--><!--Device-InsightIntentPage-domain: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## icon

```TypeScript
icon: string = ''
```

表示意图图标，用于在AI入口显示。ArkTS-Sta为字符串类型，所以与ArkTS-Dyn写法存在部分差异：  
- 当表示图标读取网络资源时，赋值无差异，例如'https://www.example.com/music/'。  
- 当表示图标读取本地资源时，ArkTS-Dyn写法为`\$r("app.media.app_icon")`、ArkTS-Sta写法为`'\$r("app.media.app_icon")'`。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-icon: string = ''--><!--Device-InsightIntentPage-icon: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## intentName

```TypeScript
intentName: string
```

表示意图名称，是意图的唯一标识。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-intentName: string--><!--Device-InsightIntentPage-intentName: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## intentVersion

```TypeScript
intentVersion: string
```

表示意图版本号。当意图能力演进时，可通过版本号进行区分和管理。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-intentVersion: string--><!--Device-InsightIntentPage-intentVersion: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## keywords

```TypeScript
keywords: string[] = []
```

表示意图的搜索关键字。

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-keywords: string[] = []--><!--Device-InsightIntentPage-keywords: string[] = []-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## llmDescription

```TypeScript
llmDescription: string = ''
```

表示意图的功能，用于大型语言模型理解该意图。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-llmDescription: string = ''--><!--Device-InsightIntentPage-llmDescription: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## navDestinationName

```TypeScript
navDestinationName: string = ''
```

表示与意图绑定[navDestination](./@internal/component/ets/navigation.navDestination)组件的名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-navDestinationName: string = ''--><!--Device-InsightIntentPage-navDestinationName: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## navigationId

```TypeScript
navigationId: string = ''
```

表示与意图绑定的[Navigation](./@internal/component/ets/navigation)组件的id属性。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-navigationId: string = ''--><!--Device-InsightIntentPage-navigationId: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## pagePath

```TypeScript
pagePath: string
```

表示与意图绑定的页面路径，该页面需要是一个实际存在的文件。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-pagePath: string--><!--Device-InsightIntentPage-pagePath: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters: string = ''
```

表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。取值参见  
[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。与ArkTS-Dyn不同，ArkTS-Sta场景下的parameters字段为字符串类型，需赋值`Record&lt;string, RecordData&gt;`类型变量的名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-parameters: string = ''--><!--Device-InsightIntentPage-parameters: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## result

```TypeScript
result: string = ''
```

表示意图调用返回结果的数据格式声明，用于定义意图调用返回结果的数据格式。与ArkTS-Dyn不同，ArkTS-Sta场景下的result字段为字符串类型，需赋值`Record&lt;string, RecordData&gt;`类型变量的名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-result: string = ''--><!--Device-InsightIntentPage-result: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## schema

```TypeScript
schema: string = ''
```

表示接入的标准意图的名称。开发者[接入标准意图](../../../application-models/insight-intent-definition.md#接入标准意图)时，需要配置该字段，  
[创建自定义意图](../../../application-models/insight-intent-definition.md#创建自定义意图)时，无需配置该字段。标准意图列表参见  
[附录：标准意图接入规范](../../../application-models/insight-intent-access-specifications.md)。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-schema: string = ''--><!--Device-InsightIntentPage-schema: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## uiAbility

```TypeScript
uiAbility: string = ''
```

表示与意图绑定的UIAbility名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-uiAbility: string = ''--><!--Device-InsightIntentPage-uiAbility: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

