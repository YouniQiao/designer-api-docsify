# InsightIntentPage

Define InsightIntentPage Annotation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentPage--><!--Device-unnamed-export @interface InsightIntentPage-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from 'kits/@kit.AbilityKit';
```

## displayDescription

```TypeScript
displayDescription: string = ''
```

The display description of intent.

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

The display name of intent.

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

The intent domain.

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

The icon of intent, the string type indicates an online resource or a local resource.For example, "\$r('app.media.startIcon')".The value of Resource type must be a literal.

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

The intent name.

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

The intent version.

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

The search keywords of intent.

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

The large language model description of intent.

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

The navigation destination name bound to the intent.

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

The navigation Id bound to the intent.

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

The page path bound to the intent.

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

The parameters of intent.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

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

The type definition of the result returned by intent call.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

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

The schema of intent, indicates a standard intent.

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

The uiAbility name bound to the intent.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentPage-uiAbility: string = ''--><!--Device-InsightIntentPage-uiAbility: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

