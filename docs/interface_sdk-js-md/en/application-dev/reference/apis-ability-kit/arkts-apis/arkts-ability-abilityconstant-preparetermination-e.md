# PrepareTermination

Enumerates the actions triggered when an application is closed by the user. You can use it in  
[onPrepareTermination]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or  
[onPrepareTerminationAsync]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ of  
[AbilityStage]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum PrepareTermination--><!--Device-AbilityConstant-export enum PrepareTermination-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## TERMINATE_IMMEDIATELY

```TypeScript
TERMINATE_IMMEDIATELY = 0
```

Executes the termination action immediately. This is the default behavior.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PrepareTermination-TERMINATE_IMMEDIATELY = 0--><!--Device-PrepareTermination-TERMINATE_IMMEDIATELY = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CANCEL

```TypeScript
CANCEL = 1
```

Cancels the termination action.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PrepareTermination-CANCEL = 1--><!--Device-PrepareTermination-CANCEL = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

