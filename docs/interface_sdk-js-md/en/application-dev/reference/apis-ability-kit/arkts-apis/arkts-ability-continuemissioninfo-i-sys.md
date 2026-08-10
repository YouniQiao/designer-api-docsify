# ContinueMissionInfo (System API)

表示发起按照包名迁移时所需参数的枚举，迁移Mission详见：  
[continueMission接口](arkts-ability-distributedmissionmanager-continuemission-f-sys.md#continuemission)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ContinueMissionInfo--><!--Device-unnamed-export interface ContinueMissionInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

表示任务所属目标端应用包名。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-bundleName: string--><!--Device-ContinueMissionInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## continueType

```TypeScript
continueType?: string
```

表示任务所属应用迁移类型。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-continueType?: string--><!--Device-ContinueMissionInfo-continueType?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## dstDeviceId

```TypeScript
dstDeviceId: string
```

表示任务迁移目标设备ID。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-dstDeviceId: string--><!--Device-ContinueMissionInfo-dstDeviceId: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## srcBundleName

```TypeScript
srcBundleName?: string
```

表示任务所属源端应用包名，默认与bundleName相同。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-srcBundleName?: string--><!--Device-ContinueMissionInfo-srcBundleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## srcDeviceId

```TypeScript
srcDeviceId: string
```

表示任务迁移源设备ID。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-srcDeviceId: string--><!--Device-ContinueMissionInfo-srcDeviceId: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## wantParam

```TypeScript
wantParam: Record<string, Object>
```

表示扩展参数。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueMissionInfo-wantParam: Record<string, Object>--><!--Device-ContinueMissionInfo-wantParam: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

