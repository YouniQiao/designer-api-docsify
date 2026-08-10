# GetInsightIntentFlag (System API)

意图信息（[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)）的标识，用于  
[getAllInsightIntentInfo](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getinsightintentinfobybundlename)、  
[getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getinsightintentinfobybundlename)和  
[getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md#getinsightintentinfobyintentname)接口查询意图信息。

> **说明：**
> 
> - 对于使用配置文件开发的意图，通过上述接口查询的全量信息和简要信息完全一致。
> 
> - 对于使用装饰器开发的意图，通过上述接口查询的全量信息和简要信息存在差别，详见下表。
> 
> 表1 全量意图信息与简要意图信息差别
> 
> | 属性 | 全量意图信息是否包含 | 简要意图信息是否包含 |
> | -------- | -------- | -------- |
> | bundleName | 是 | 是 |
> | moduleName | 是 | 是 |
> | intentName | 是 | 是 |
> | domain | 是 | 否 |
> | intentVersion | 是 | 否 |
> | displayName | 是 | 是 |
> | displayDescription | 是 | 否 |
> | schema | 是 | 否 |
> | icon | 是 | 否 |
> | llmDescription | 是 | 否 |
> | keywords | 是 | 否 |
> | intentType | 是 | 是 |
> | subIntentInfo | 是 | 是 |
> | parameters | 是 | 是 |
> | entities | 否 | 否 |
> | developType&lt;sup&gt;23+&lt;/sup&gt; | 是 | 是 |
> | subIntentInfoForConfiguration&lt;sup&gt;23+&lt;/sup&gt; | 否 | 否 |

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-insightIntentDriver-enum GetInsightIntentFlag--><!--Device-insightIntentDriver-enum GetInsightIntentFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_FULL_INSIGHT_INTENT

```TypeScript
GET_FULL_INSIGHT_INTENT = 0x00000001
```

查询[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)中的除entities以外的全量意图信息，详见下表。查询entities信息需要使用GET_ENTITY_INFO。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_FULL_INSIGHT_INTENT = 0x00000001--><!--Device-GetInsightIntentFlag-GET_FULL_INSIGHT_INTENT = 0x00000001-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_SUMMARY_INSIGHT_INTENT

```TypeScript
GET_SUMMARY_INSIGHT_INTENT = 0x00000002
```

查询[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)中的简要意图信息，详见下表。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_SUMMARY_INSIGHT_INTENT = 0x00000002--><!--Device-GetInsightIntentFlag-GET_SUMMARY_INSIGHT_INTENT = 0x00000002-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_ENTITY_INFO

```TypeScript
GET_ENTITY_INFO = 0x00000004
```

查询[EntityInfo](arkts-ability-insightintentdriver-entityinfo-i-sys.md)的信息，不可单独使用，必选结合GET_FULL_INSIGHT_INTENT或者GET_SUMMARY_INSIGHT_INTENT使用。例如`GET_FULL_INSIGHT_INTENT | GET_ENTITY_INFO`。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004--><!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

