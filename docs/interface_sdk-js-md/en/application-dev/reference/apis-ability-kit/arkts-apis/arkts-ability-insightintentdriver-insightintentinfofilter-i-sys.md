# InsightIntentInfoFilter (System API)

意图筛选器，描述目标意图的筛选条件，用于筛选设备上符合条件的意图。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntentDriver-interface InsightIntentInfoFilter--><!--Device-insightIntentDriver-interface InsightIntentInfoFilter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## bundleName

```TypeScript
bundleName?: string
```

目标意图所属的应用包名称。

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

意图信息（[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)）的标识，用于表示查询全量意图信息或者简要意图信息，取值可参考  
[GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

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

目标意图名称。

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

目标意图所属的模块名称。

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

目标意图所属的用户ID。

**说明：**

如果调用方应用的用户ID与目标意图所属的用户ID不同，则需要申请权限`ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS`。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentInfoFilter-userId?: int--><!--Device-InsightIntentInfoFilter-userId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

