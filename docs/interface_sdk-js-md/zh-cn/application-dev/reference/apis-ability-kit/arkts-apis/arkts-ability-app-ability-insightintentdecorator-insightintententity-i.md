# InsightIntentEntity

Define InsightIntentEntity Annotation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentEntity--><!--Device-unnamed-export @interface InsightIntentEntity-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from 'kits/@kit.AbilityKit';
```

## entityCategory

```TypeScript
entityCategory: string
```

The entity category.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntity-entityCategory: string--><!--Device-InsightIntentEntity-entityCategory: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters: string = ""
```

The parameters of intent entity.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntity-parameters: string = ""--><!--Device-InsightIntentEntity-parameters: string = ""-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## supportedQueryProperties

```TypeScript
supportedQueryProperties: string[] = []
```

Supported query properties.

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []--><!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

