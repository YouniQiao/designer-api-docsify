# HapModuleInfo (System API)

FA模型的使用信息属性集合。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usageStatistics-interface HapModuleInfo--><!--Device-usageStatistics-interface HapModuleInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## abilityDescriptionId

```TypeScript
abilityDescriptionId?: long
```

FA的MainAbility descriptionId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-abilityDescriptionId?: long--><!--Device-HapModuleInfo-abilityDescriptionId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## abilityIconId

```TypeScript
abilityIconId?: long
```

FA的MainAbility iconId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-abilityIconId?: long--><!--Device-HapModuleInfo-abilityIconId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## abilityLableId

```TypeScript
abilityLableId?: long
```

FA的MainAbility labelId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-abilityLableId?: long--><!--Device-HapModuleInfo-abilityLableId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName?: string
```

FA的MainAbility名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-abilityName?: string--><!--Device-HapModuleInfo-abilityName?: string-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## appLabelId

```TypeScript
appLabelId?: long
```

FA的应用labelId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-appLabelId?: long--><!--Device-HapModuleInfo-appLabelId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-bundleName: string--><!--Device-HapModuleInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## descriptionId

```TypeScript
descriptionId?: long
```

FA所属的应用descriptionId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-descriptionId?: long--><!--Device-HapModuleInfo-descriptionId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId?: string
```

设备Id。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-deviceId?: string--><!--Device-HapModuleInfo-deviceId?: string-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## formRecords

```TypeScript
formRecords: Array<HapFormInfo>
```

FA中卡片的使用记录。

**Type:** Array&lt;HapFormInfo&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-formRecords: Array<HapFormInfo>--><!--Device-HapModuleInfo-formRecords: Array<HapFormInfo>-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## labelId

```TypeScript
labelId?: long
```

FA所属module的labelId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-labelId?: long--><!--Device-HapModuleInfo-labelId?: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## lastModuleUsedTime

```TypeScript
lastModuleUsedTime: long
```

FA的上一次使用时间，单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-lastModuleUsedTime: long--><!--Device-HapModuleInfo-lastModuleUsedTime: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## launchedCount

```TypeScript
launchedCount: int
```

FA的启动次数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-launchedCount: int--><!--Device-HapModuleInfo-launchedCount: int-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

FA所属module名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HapModuleInfo-moduleName: string--><!--Device-HapModuleInfo-moduleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.App

**System API:** This is a system API.

