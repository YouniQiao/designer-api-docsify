# InsightIntentEntity

使用该注解装饰一个继承自[IntentEntity](arkts-ability-insightintent-intententity-i.md#IntentEntity)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见  
[@InsightIntentEntity](#InsightIntentEntity)。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export @interface InsightIntentEntity--><!--Device-unnamed-export @interface InsightIntentEntity-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## entityCategory

```TypeScript
entityCategory: string
```

表示意图实体类别。可以基于意图实体类别对意图实体进行归类

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

表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。取值参见  
[各垂域意图Schema](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713)。与ArkTS-Dyn不同，ArkTS-Sta场景下的parameters字段为字符串类型，需赋值`Record&lt;string, RecordData&gt;`类型变量的名称。

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

表示意图实体支持查询的属性列表。列表中的属性名必须在parameters中定义。

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []--><!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

