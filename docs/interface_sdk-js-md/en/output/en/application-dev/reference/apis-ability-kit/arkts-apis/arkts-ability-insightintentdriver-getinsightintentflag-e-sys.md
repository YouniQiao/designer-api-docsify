# GetInsightIntentFlag (System API)

Enumerates the flags of intent information ([InsightIntentInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_). It is used in [getAllInsightIntentInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [getInsightIntentInfoByBundleName]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, and [getInsightIntentInfoByIntentName]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. > **NOTE** > > - For intents developed using a configuration file, the full and brief information queried through the preceding > APIs are the same. > > - For intents developed using a decorator, the full and brief information queried through the preceding APIs are > different, as described below. > > Table 1 Differences between full intent information and brief intent information > > | Name| Included in Full Intent Information| Included in Brief Intent Information| > | -------- | -------- | -------- | > | bundleName | Yes| Yes| > | moduleName | Yes| Yes| > | intentName | Yes| Yes| > | domain | Yes| No| > | intentVersion | Yes| No| > | displayName | Yes| Yes| > | displayDescription | Yes| No| > | schema | Yes| No| > | icon | Yes| No| > | llmDescription | Yes| No| > | keywords | Yes| No| > | intentType | Yes| Yes| > | subIntentInfo | Yes| Yes| > | parameters | Yes| Yes| > | entities | No| No| > | developType\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_23+\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ | Yes| Yes| > | subIntentInfoForConfiguration\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_23+\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ | No| No|

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-insightIntentDriver-enum GetInsightIntentFlag--><!--Device-insightIntentDriver-enum GetInsightIntentFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## GET_FULL_INSIGHT_INTENT

```TypeScript
GET_FULL_INSIGHT_INTENT = 0x00000001
```

Used to query all intent information (except entities) in [InsightIntentInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. To query entities information, use **GET\_ENTITY\_INFO**.

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

Used to query brief intent information in [InsightIntentInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

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

Used to query [EntityInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. It must be used together with **GET\_FULL\_INSIGHT\_INTENT** or **GET\_SUMMARY\_INSIGHT\_INTENT**. Example usage: \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004--><!--Device-GetInsightIntentFlag-GET_ENTITY_INFO = 0x00000004-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

