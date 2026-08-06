# InsightIntentInfoFilter (System API)

Defines an intent filter, which specifies the criteria for selecting target intents. It is used to filter intents on the device that meet these criteria.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntentDriver-interface InsightIntentInfoFilter--><!--Device-insightIntentDriver-interface InsightIntentInfoFilter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the application to which the intent belongs.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-bundleName?: string--><!--Device-InsightIntentInfoFilter-bundleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## intentFlags

```TypeScript
intentFlags: int
```

Flag of the intent information ([InsightIntentInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_). It is used to query full or brief intent information. For details, see  
[GetInsightIntentFlag]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-intentFlags: int--><!--Device-InsightIntentInfoFilter-intentFlags: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## intentName

```TypeScript
intentName?: string
```

Intent name.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-intentName?: string--><!--Device-InsightIntentInfoFilter-intentName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName?: string
```

Module name of the application to which the intent belongs.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-moduleName?: string--><!--Device-InsightIntentInfoFilter-moduleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

ID of the user to which the intent belongs.

**NOTE**

If the user ID of the calling application is different from the user ID of the intent, the calling application must request the ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS permission.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-userId?: int--><!--Device-InsightIntentInfoFilter-userId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

