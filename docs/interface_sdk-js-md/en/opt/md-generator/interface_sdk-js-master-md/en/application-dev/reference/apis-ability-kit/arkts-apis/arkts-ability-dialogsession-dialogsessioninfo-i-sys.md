# DialogSessionInfo (System API)

Provides session information, including the requester information, target ability information list, and other parameters.

**Since:** 23

**Deprecated since:** -1

<!--Device-dialogSession-export interface DialogSessionInfo--><!--Device-dialogSession-export interface DialogSessionInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## callerAbilityInfo

```TypeScript
callerAbilityInfo: DialogAbilityInfo
```

Ability information of the requester.

**Type:** [DialogAbilityInfo](arkts-ability-dialogsession-dialogabilityinfo-i-sys.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-callerAbilityInfo: DialogAbilityInfo--><!--Device-DialogSessionInfo-callerAbilityInfo: DialogAbilityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parameters

```TypeScript
parameters?: Record<string, RecordData>
```

Other parameters.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-parameters?: Record<string, RecordData>--><!--Device-DialogSessionInfo-parameters?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## targetAbilityInfos

```TypeScript
targetAbilityInfos: Array<DialogAbilityInfo>
```

List of target ability information.

**Type:** Array&lt;[DialogAbilityInfo](arkts-ability-dialogsession-dialogabilityinfo-i-sys.md)&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogSessionInfo-targetAbilityInfos: Array<DialogAbilityInfo>--><!--Device-DialogSessionInfo-targetAbilityInfos: Array<DialogAbilityInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.
