# GetInsightIntentFlag (System API)

Enumerates the flags of intent information ([InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)). It is used in [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md), [getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md), and [getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md). &gt; **NOTE：**&gt; &gt; - For intents developed using a configuration file, the full and brief information queried through the preceding &gt; APIs are the same. &gt; &gt; - For intents developed using a decorator, the full and brief information queried through the preceding APIs are &gt; different, as described below. &gt; &gt; Table 1 Differences between full intent information and brief intent information &gt; &gt; | Name| Included in Full Intent Information| Included in Brief Intent Information| &gt; | -------- | -------- | -------- | &gt; | bundleName | Yes| Yes| &gt; | moduleName | Yes| Yes| &gt; | intentName | Yes| Yes| &gt; | domain | Yes| No| &gt; | intentVersion | Yes| No| &gt; | displayName | Yes| Yes| &gt; | displayDescription | Yes| No| &gt; | schema | Yes| No| &gt; | icon | Yes| No| &gt; | llmDescription | Yes| No| &gt; | keywords | Yes| No| &gt; | intentType | Yes| Yes| &gt; | subIntentInfo | Yes| Yes| &gt; | parameters | Yes| Yes| &gt; | entities | No| No| &gt; | developType&lt;sup&gt;23+&lt;/sup&gt; | Yes| Yes| &gt; | subIntentInfoForConfiguration&lt;sup&gt;23+&lt;/sup&gt; | No| No|

**Since:** 23

<!--Device-insightIntentDriver-enum GetInsightIntentFlag--><!--Device-insightIntentDriver-enum GetInsightIntentFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_FULL_INSIGHT_INTENT

```TypeScript
GET_FULL_INSIGHT_INTENT = 0x00000001
```

Used to query all intent information (except entities) in [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md). To query entities information, use **GET_ENTITY_INFO**.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_FULL_INSIGHT_INTENT = 0x00000001--><!--Device-GetInsightIntentFlag-GET_FULL_INSIGHT_INTENT = 0x00000001-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_SUMMARY_INSIGHT_INTENT

```TypeScript
GET_SUMMARY_INSIGHT_INTENT = 0x00000002
```

Used to query brief intent information in [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_SUMMARY_INSIGHT_INTENT = 0x00000002--><!--Device-GetInsightIntentFlag-GET_SUMMARY_INSIGHT_INTENT = 0x00000002-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_ENTITY_INFO

```TypeScript
GET_ENTITY_INFO = 0x00000004
```

Used to query [EntityInfo](arkts-ability-insightintentdriver-entityinfo-i-sys.md). It must be used together with **GET_FULL_INSIGHT_INTENT** or **GET_SUMMARY_INSIGHT_INTENT**. Example usage: `GET_FULL_INSIGHT_INTENT | GET_ENTITY_INFO`.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004--><!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

