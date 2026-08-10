# AppGroupCallbackInfo (System API)

应用分组变化回调返回的属性集合

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usageStatistics-interface AppGroupCallbackInfo--><!--Device-usageStatistics-interface AppGroupCallbackInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## appNewGroup

```TypeScript
appNewGroup: int
```

变化后的应用分组。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AppGroupCallbackInfo-appNewGroup: int--><!--Device-AppGroupCallbackInfo-appNewGroup: int-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

## appOldGroup

```TypeScript
appOldGroup: int
```

变化前的应用分组。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AppGroupCallbackInfo-appOldGroup: int--><!--Device-AppGroupCallbackInfo-appOldGroup: int-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AppGroupCallbackInfo-bundleName: string--><!--Device-AppGroupCallbackInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

## changeReason

```TypeScript
changeReason: long
```

分组变化原因。

- 256:使用记录初创建时，默认匹配的原因。  
- 512:计算优先级分组时异常。  
- 768:使用时长变化。   
- 1024:有其他应用为当前应用强制设置优先级分组。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AppGroupCallbackInfo-changeReason: long--><!--Device-AppGroupCallbackInfo-changeReason: long-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

## userId

```TypeScript
userId: int
```

用户id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AppGroupCallbackInfo-userId: int--><!--Device-AppGroupCallbackInfo-userId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**System API:** This is a system API.

