# InsightIntentLink

Define InsightIntentLink Annotation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentLink--><!--Device-unnamed-export @interface InsightIntentLink-End-->

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

<!--Device-InsightIntentLink-displayDescription: string = ''--><!--Device-InsightIntentLink-displayDescription: string = ''-End-->

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

<!--Device-InsightIntentLink-displayName: string--><!--Device-InsightIntentLink-displayName: string-End-->

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

<!--Device-InsightIntentLink-domain: string--><!--Device-InsightIntentLink-domain: string-End-->

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

<!--Device-InsightIntentLink-icon: string = ''--><!--Device-InsightIntentLink-icon: string = ''-End-->

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

<!--Device-InsightIntentLink-intentName: string--><!--Device-InsightIntentLink-intentName: string-End-->

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

<!--Device-InsightIntentLink-intentVersion: string--><!--Device-InsightIntentLink-intentVersion: string-End-->

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

<!--Device-InsightIntentLink-keywords: string[] = []--><!--Device-InsightIntentLink-keywords: string[] = []-End-->

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

<!--Device-InsightIntentLink-llmDescription: string = ''--><!--Device-InsightIntentLink-llmDescription: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## paramMappings

```TypeScript
paramMappings: string = ''
```

The parameters mapping of a link.The value is the name of a variable of type LinkIntentParamMapping[].

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentLink-paramMappings: string = ''--><!--Device-InsightIntentLink-paramMappings: string = ''-End-->

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

<!--Device-InsightIntentLink-parameters: string = ''--><!--Device-InsightIntentLink-parameters: string = ''-End-->

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

<!--Device-InsightIntentLink-result: string = ''--><!--Device-InsightIntentLink-result: string = ''-End-->

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

<!--Device-InsightIntentLink-schema: string = ''--><!--Device-InsightIntentLink-schema: string = ''-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## uri

```TypeScript
uri: string
```

The uri of a link.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentLink-uri: string--><!--Device-InsightIntentLink-uri: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

