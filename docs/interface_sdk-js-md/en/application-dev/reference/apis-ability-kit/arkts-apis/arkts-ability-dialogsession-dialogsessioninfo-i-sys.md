# DialogSessionInfo (System API)

提供会话信息，包括请求方信息、目标组件信息列表、其他参数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-dialogSession-export interface DialogSessionInfo--><!--Device-dialogSession-export interface DialogSessionInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dialogSession } from 'kits/@kit.AbilityKit';
```

## callerAbilityInfo

```TypeScript
callerAbilityInfo: DialogAbilityInfo
```

表示请求方组件信息。

**Type:** [DialogAbilityInfo](arkts-ability-dialogsession-dialogabilityinfo-i-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-callerAbilityInfo: DialogAbilityInfo--><!--Device-DialogSessionInfo-callerAbilityInfo: DialogAbilityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parameters

```TypeScript
parameters?: Record<string, Object>
```

表示其他参数。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-parameters?: Record<string, Object>--><!--Device-DialogSessionInfo-parameters?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## targetAbilityInfos

```TypeScript
targetAbilityInfos: Array<DialogAbilityInfo>
```

表示目标组件信息列表。

**Type:** Array&lt;DialogAbilityInfo&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-targetAbilityInfos: Array<DialogAbilityInfo>--><!--Device-DialogSessionInfo-targetAbilityInfos: Array<DialogAbilityInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

