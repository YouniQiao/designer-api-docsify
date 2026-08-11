# LocalWantAgentInfo (System API)

Defines the information required for triggering a local WantAgent object. The information can be used as an input parameter in  
[createLocalWantAgent](../../../reference/apis-ability-kit/js-apis-app-ability-wantAgent-sys.md#wantagentcreatelocalwantagent20)to obtain a local WantAgent object.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface LocalWantAgentInfo--><!--Device-unnamed-export interface LocalWantAgentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## operationType

```TypeScript
operationType?: abilityWantAgent.OperationType
```

Type of the operation to execute.

**Type:** abilityWantAgent.OperationType

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalWantAgentInfo-operationType?: abilityWantAgent.OperationType--><!--Device-LocalWantAgentInfo-operationType?: abilityWantAgent.OperationType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## requestCode

```TypeScript
requestCode: int
```

Custom request code, which is used to identify the operation to execute.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalWantAgentInfo-requestCode: int--><!--Device-LocalWantAgentInfo-requestCode: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## wants

```TypeScript
wants: Array<Want>
```

Array of all Want objects. Currently, only one Want object is supported. If multiple values are passed in, only the first member in the array is used.

**Type:** Array&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalWantAgentInfo-wants: Array<Want>--><!--Device-LocalWantAgentInfo-wants: Array<Want>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

