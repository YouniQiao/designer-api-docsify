# InsightIntentEntry

Define InsightIntentEntry Annotation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentEntry--><!--Device-unnamed-export @interface InsightIntentEntry-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from 'kits/@kit.AbilityKit';
```

## abilityName

```TypeScript
abilityName: string
```

The ability name bound to the intent.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntry-abilityName: string--><!--Device-InsightIntentEntry-abilityName: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## displayDescription

```TypeScript
displayDescription: string = ''
```

The display description of intent.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntry-displayDescription: string = ''--><!--Device-InsightIntentEntry-displayDescription: string = ''-End-->

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

<!--Device-InsightIntentEntry-displayName: string--><!--Device-InsightIntentEntry-displayName: string-End-->

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

<!--Device-InsightIntentEntry-domain: string--><!--Device-InsightIntentEntry-domain: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode[]
```

The execute mode of the intent.For UIAbility, the parameter can be set to insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND or insightIntent.ExecuteMode.UI_ABILITY_BACKGROUND or both of them.

**类型：** insightIntent.ExecuteMode[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntry-executeMode: insightIntent.ExecuteMode[]--><!--Device-InsightIntentEntry-executeMode: insightIntent.ExecuteMode[]-End-->

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

<!--Device-InsightIntentEntry-icon: string = ''--><!--Device-InsightIntentEntry-icon: string = ''-End-->

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

<!--Device-InsightIntentEntry-intentName: string--><!--Device-InsightIntentEntry-intentName: string-End-->

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

<!--Device-InsightIntentEntry-intentVersion: string--><!--Device-InsightIntentEntry-intentVersion: string-End-->

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

<!--Device-InsightIntentEntry-keywords: string[] = []--><!--Device-InsightIntentEntry-keywords: string[] = []-End-->

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

<!--Device-InsightIntentEntry-llmDescription: string = ''--><!--Device-InsightIntentEntry-llmDescription: string = ''-End-->

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

<!--Device-InsightIntentEntry-parameters: string = ''--><!--Device-InsightIntentEntry-parameters: string = ''-End-->

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

<!--Device-InsightIntentEntry-result: string = ''--><!--Device-InsightIntentEntry-result: string = ''-End-->

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

<!--Device-InsightIntentEntry-schema: string = ''--><!--Device-InsightIntentEntry-schema: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

