# ContinuableInfo (System API)

当注册应用任务流转状态监听的回调时，返回应用任务流转状态和流转信息，注册详见：  
[on('continueStateChange')接口](@ohos.distributedMissionManager:distributedMissionManager.on(type: 'continueStateChange', callback: Callback&lt;ContinueCallbackInfo&gt;))。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ContinuableInfo--><!--Device-unnamed-export interface ContinuableInfo-End-->

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

<!--Device-ContinuableInfo-bundleName: string--><!--Device-ContinuableInfo-bundleName: string-End-->

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

<!--Device-ContinuableInfo-continueType?: string--><!--Device-ContinuableInfo-continueType?: string-End-->

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

<!--Device-ContinuableInfo-srcBundleName?: string--><!--Device-ContinuableInfo-srcBundleName?: string-End-->

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

<!--Device-ContinuableInfo-srcDeviceId: string--><!--Device-ContinuableInfo-srcDeviceId: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## targetAppIds

```TypeScript
targetAppIds?: Array<string>
```

表示任务所属目标应用ID列表。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinuableInfo-targetAppIds?: Array<string>--><!--Device-ContinuableInfo-targetAppIds?: Array<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

