# @ohos.app.ability.insightIntentDriver

The module provides APIs for executing intent calls. The system executes intent calls based on user interaction and more. > **NOTE：**> > Starting from API version 20, this module supports application navigation using intents defined by the > @InsightIntentLink > decorator.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace insightIntentDriver--><!--Device-unnamed-declare namespace insightIntentDriver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [execute](arkts-ability-insightintentdriver-execute-f-sys.md#execute-(System-API)) |
| [execute](arkts-ability-insightintentdriver-execute-f-sys.md#execute-(System-API)) |
| [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getallinsightintentinfo-f-sys.md#getAllInsightIntentInfo-(System-API)) |
| [getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName-(System-API)) |
| [getInsightIntentInfoByFilter](arkts-ability-insightintentdriver-getinsightintentinfobyfilter-f-sys.md#getInsightIntentInfoByFilter-(System-API)) |
| [getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md#getInsightIntentInfoByIntentName-(System-API)) |
| [queryEntityInfo](arkts-ability-insightintentdriver-queryentityinfo-f-sys.md#queryEntityInfo-(System-API)) |
| [queryEntityInfo](arkts-ability-insightintentdriver-queryentityinfo-f-sys.md#queryEntityInfo-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FunctionIntentInfo](arkts-ability-insightintentdriver-functionintentinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EntityInfo](arkts-ability-insightintentdriver-entityinfo-i-sys.md) |
| [EntryIntentInfo](arkts-ability-insightintentdriver-entryintentinfo-i-sys.md) |
| [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) |
| [FormIntentInfo](arkts-ability-insightintentdriver-formintentinfo-i-sys.md) |
| [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md) |
| [InsightIntentInfoFilter](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) |
| [LinkIntentInfo](arkts-ability-insightintentdriver-linkintentinfo-i-sys.md) |
| [PageIntentInfo](arkts-ability-insightintentdriver-pageintentinfo-i-sys.md) |
| [QueryParam](arkts-ability-insightintentdriver-queryparam-i-sys.md) |
| [ServiceExtensionIntentInfo](arkts-ability-insightintentdriver-serviceextensionintentinfo-i-sys.md) |
| [SubIntentInfoForConfiguration](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) |
| [UIAbilityIntentInfo](arkts-ability-insightintentdriver-uiabilityintentinfo-i-sys.md) |
| [UIExtensionIntentInfo](arkts-ability-insightintentdriver-uiextensionintentinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DevelopType](arkts-ability-insightintentdriver-developtype-e-sys.md) |
| [ExecuteModeForConfiguration](arkts-ability-insightintentdriver-executemodeforconfiguration-e-sys.md) |
| [GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md) | Enumerates the flags of intent information ([InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md#InsightIntentInfo-(System-API))). It is used in [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName-(System-API)), [getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName-(System-API)), and [getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md#getInsightIntentInfoByIntentName-(System-API)). > **NOTE：**> > - For intents developed using a configuration file, the full and brief information queried through the preceding > APIs are the same. > > - For intents developed using a decorator, the full and brief information queried through the preceding APIs are > different, as described below. > > Table 1 Differences between full intent information and brief intent information > > \| Name\| Included in Full Intent Information\| Included in Brief Intent Information\| > \| -------- \| -------- \| -------- \| > \| bundleName \| Yes\| Yes\| > \| moduleName \| Yes\| Yes\| > \| intentName \| Yes\| Yes\| > \| domain \| Yes\| No\| > \| intentVersion \| Yes\| No\| > \| displayName \| Yes\| Yes\| > \| displayDescription \| Yes\| No\| > \| schema \| Yes\| No\| > \| icon \| Yes\| No\| > \| llmDescription \| Yes\| No\| > \| keywords \| Yes\| No\| > \| intentType \| Yes\| Yes\| > \| subIntentInfo \| Yes\| Yes\| > \| parameters \| Yes\| Yes\| > \| entities \| No\| No\| > \| [developType](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md) & lt;sup & gt;23+ & lt;/sup & gt; \ | Yes\| Yes\| > \| [subIntentInfoForConfiguration](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md) & lt;sup & gt;23+ & lt;/sup & gt; \ | No\| No\|
| [InsightIntentType](arkts-ability-insightintentdriver-insightintenttype-e-sys.md) |
<!--DelEnd-->
