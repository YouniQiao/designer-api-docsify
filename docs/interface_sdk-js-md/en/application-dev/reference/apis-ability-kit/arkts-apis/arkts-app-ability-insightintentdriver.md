# @ohos.app.ability.insightIntentDriver

The module provides APIs for executing intent calls. The system executes intent calls based on user interaction and more. > **NOTE：**> > Starting from API version 20, this module supports application navigation using intents defined by the > @InsightIntentLink > decorator.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace insightIntentDriver--><!--Device-unnamed-declare namespace insightIntentDriver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'insightIntentDriver';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [execute](arkts-ability-insightintentdriver-execute-f-sys.md#execute) | Executes a call to an intent. This API uses an asynchronous callback to return the result. When the caller is in the background, the ohos.permission.START_ABILITIES_FROM_BACKGROUND permission is required. When [ExecuteMode](arkts-ability-insightintent-executemode-e.md#ExecuteMode) of the intent call is set to **UI_ABILITY_BACKGROUND**, the ohos.permission.ABILITY_BACKGROUND_COMMUNICATION permission is required. On API 26.0.0 and above, intent can be executed across devices. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required. |
| [execute](arkts-ability-insightintentdriver-execute-f-sys.md#execute-(System-API)) | Executes a call to an intent. This API uses a promise to return the result. When the caller is in the background, the ohos.permission.START_ABILITIES_FROM_BACKGROUND permission is required. When [ExecuteMode](arkts-ability-insightintent-executemode-e.md#ExecuteMode) of the intent call is set to **UI_ABILITY_BACKGROUND**, the ohos.permission.ABILITY_BACKGROUND_COMMUNICATION permission is required. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required. On API 26.0.0 and above, intent can be executed across devices. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required. |
| [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getallinsightintentinfo-f-sys.md#getAllInsightIntentInfo) | Obtains the information about all intents on the current device. This API uses a promise to return the result. |
| [getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName) | Obtains the intent information on the current device based on the given bundle name. This API uses a promise to return the result. |
| [getInsightIntentInfoByFilter](arkts-ability-insightintentdriver-getinsightintentinfobyfilter-f-sys.md#getInsightIntentInfoByFilter) | Obtains the intent information on the current device based on the given intent filter. This API uses a promise to return the result.<br>If the user ID of the calling application is different from the user ID of the intent, the calling application must request the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission. |
| [getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md#getInsightIntentInfoByIntentName) | Obtains the intent information on the current device based on the bundle name, module name, and intent name. This API uses a promise to return the result. |
| [queryEntityInfo](arkts-ability-insightintentdriver-queryentityinfo-f-sys.md#queryEntityInfo) | Query insight intent entity information. |
| [queryEntityInfo](arkts-ability-insightintentdriver-queryentityinfo-f-sys.md#queryEntityInfo-(System-API)) | Query insight intent entity information. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [FunctionIntentInfo](arkts-ability-insightintentdriver-functionintentinfo-i.md) | Defines the parameter type of the @InsightIntentFunctionMethod decorator. All parameters inherit from [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md#IntentDecoratorInfo). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [EntityInfo](arkts-ability-insightintentdriver-entityinfo-i-sys.md) | EntityInfo inherits from [IntentEntityDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intententitydecoratorinfo-i.md#IntentEntityDecoratorInfo) and is used to describe the information about the intent entity defined by the @InsightIntentEntity decorator. |
| [EntryIntentInfo](arkts-ability-insightintentdriver-entryintentinfo-i-sys.md) | Describes the parameters supported by the @InsightIntentForm decorator, such as the widget name. It also describes the widget information bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
| [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) | Defines the parameter used to execute an intent call. |
| [FormIntentInfo](arkts-ability-insightintentdriver-formintentinfo-i-sys.md) | Describes the parameters supported by the @InsightIntentForm decorator, such as the widget name. It also describes the widget information bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
| [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md) | Defines the intent information, which is the specific parameter configuration of the intent in the device. |
| [InsightIntentInfoFilter](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) | Defines an intent filter, which specifies the criteria for selecting target intents. It is used to filter intents on the device that meet these criteria. |
| [LinkIntentInfo](arkts-ability-insightintentdriver-linkintentinfo-i-sys.md) | Describes the parameters supported by the @InsightIntentLink decorator, such as the URI required for application redirection. |
| [PageIntentInfo](arkts-ability-insightintentdriver-pageintentinfo-i-sys.md) | Describes the parameters supported by the @InsightIntentPage decorator, such as the [NavDestination](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10) name of the target page. |
| [QueryParam](arkts-ability-insightintentdriver-queryparam-i-sys.md) | Param when query insight intent entity. |
| [ServiceExtensionIntentInfo](arkts-ability-insightintentdriver-serviceextensionintentinfo-i-sys.md) | Describes the information of the ServiceExtensionAbility bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
| [SubIntentInfoForConfiguration](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | Describes the unique information of the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
| [UIAbilityIntentInfo](arkts-ability-insightintentdriver-uiabilityintentinfo-i-sys.md) | Describes the information of the UIAbility bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
| [UIExtensionIntentInfo](arkts-ability-insightintentdriver-uiextensionintentinfo-i-sys.md) | Describes the information of the UIExtensionAbility bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DevelopType](arkts-ability-insightintentdriver-developtype-e-sys.md) | Enumerates the modes that define how an intent is developed. |
| [ExecuteModeForConfiguration](arkts-ability-insightintentdriver-executemodeforconfiguration-e-sys.md) | Enumerates the execution modes supported by an [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md). For example, if **executeMode** in the [insight_intent.json configuration file] (../../../application-models/insight-intent-config-development.md#description-of-the-insight_intentjson-file) is set to **foreground**, the intent bound to the UIAbility can run in the foreground. |
| [GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md) | Enumerates the flags of intent information ([InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md#InsightIntentInfo-(System-API))). It is used in [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName-(System-API)), [getInsightIntentInfoByBundleName](arkts-ability-insightintentdriver-getinsightintentinfobybundlename-f-sys.md#getInsightIntentInfoByBundleName-(System-API)), and [getInsightIntentInfoByIntentName](arkts-ability-insightintentdriver-getinsightintentinfobyintentname-f-sys.md#getInsightIntentInfoByIntentName-(System-API)). > **NOTE：**> > - For intents developed using a configuration file, the full and brief information queried through the preceding > APIs are the same. > > - For intents developed using a decorator, the full and brief information queried through the preceding APIs are > different, as described below. > > Table 1 Differences between full intent information and brief intent information > > \| Name\| Included in Full Intent Information\| Included in Brief Intent Information\| > \| -------- \| -------- \| -------- \| > \| bundleName \| Yes\| Yes\| > \| moduleName \| Yes\| Yes\| > \| intentName \| Yes\| Yes\| > \| domain \| Yes\| No\| > \| intentVersion \| Yes\| No\| > \| displayName \| Yes\| Yes\| > \| displayDescription \| Yes\| No\| > \| schema \| Yes\| No\| > \| icon \| Yes\| No\| > \| llmDescription \| Yes\| No\| > \| keywords \| Yes\| No\| > \| intentType \| Yes\| Yes\| > \| subIntentInfo \| Yes\| Yes\| > \| parameters \| Yes\| Yes\| > \| entities \| No\| No\| > \| developType&lt;sup&gt;23+&lt;/sup&gt; \| Yes\| Yes\| > \| subIntentInfoForConfiguration&lt;sup&gt;23+&lt;/sup&gt; \| No\| No\| |
| [InsightIntentType](arkts-ability-insightintentdriver-insightintenttype-e-sys.md) | Enumerates the intent types defined by the intent decorator. You can obtain the intent type from [LinkIntentInfo](arkts-ability-insightintentdriver-linkintentinfo-i-sys.md#LinkIntentInfo-(System-API)) returned by calling APIs such as [getAllInsightIntentInfo](arkts-ability-insightintentdriver-getallinsightintentinfo-f-sys.md#getAllInsightIntentInfo-(System-API)). |
<!--DelEnd-->

