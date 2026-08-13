# @ohos.app.ability.AbilityConstant

AbilityConstant provides enums related to abilities, including the window mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace AbilityConstant--><!--Device-unnamed-declare namespace AbilityConstant-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AbilityConstant } from '@kit.AbilityKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [LastExitDetailInfo](arkts-ability-abilityconstant-lastexitdetailinfo-i.md) | Describes the key runtime information of the process where the ability last exited. |
| [LaunchParam](arkts-ability-abilityconstant-launchparam-i.md) | Describes the launch parameters, which mainly include the ability launch reasons and reasons for the last exit. The parameter values are automatically passed in by the system when the ability is launched. You do not need to change the values. |

### Enums

| Name | Description |
| --- | --- |
| [CollaborateResult](arkts-ability-abilityconstant-collaborateresult-e.md) | Enumerates the collaboration request results. You can use it in multi-device collaboration scenarios to specify whether the target application accepts the collaboration request from the caller application. You can use it in [onCollaborate()](arkts-ability-app-ability-uiability-uiability-c.md#onCollaborate) of the UIAbility. |
| [ContinueState](arkts-ability-abilityconstant-continuestate-e.md) | Enumerates the mission continuation states of the application. It is used in the [setMissionContinueState](arkts-ability-uiabilitycontext-c.md#setMissionContinueState) API of [UIAbilityContext](arkts-ability-uiabilitycontext-c.md#UIAbilityContext). |
| [LastExitReason](arkts-ability-abilityconstant-lastexitreason-e.md) | Enumerates the reasons for the last exit of the ability. You can use it together with the value of **launchParam.lastExitReason** in [onCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onCreate) of the UIAbility to complete different operations. |
| [LaunchReason](arkts-ability-abilityconstant-launchreason-e.md) | Enumerates the ability launch reasons. You can use it together with the value of **launchParam.launchReason** in [onCreate(want, launchParam)](arkts-ability-app-ability-uiability-uiability-c.md#onCreate) of the UIAbility to complete different operations. |
| [MemoryLevel](arkts-ability-abilityconstant-memorylevel-e.md) | Enumerates the memory levels of the entire device. You can use it in [onMemoryLevel()](arkts-ability-app-ability-ability-ability-c.md#onMemoryLevel) of the UIAbility to complete different operations. > **NOTE：**> > - The trigger conditions may differ across various devices. For example, on a standard device with 12 GB of > memory: > - When the available memory of the entire device drops to 1700 MB to 1800 MB, the **onMemoryLevel** callback > with a value of **0** is triggered, indicating that the available memory is moderate. > - When the available memory of the entire device drops to 1600 MB to 1700 MB, the **onMemoryLevel** callback > with a value of **1** is triggered, indicating that the available memory is low. > - When the available memory of the entire device drops below 1600 MB, the **onMemoryLevel** callback with a > value of **2** is triggered, indicating that the available memory is critically low. |
| [OnContinueResult](arkts-ability-abilityconstant-oncontinueresult-e.md) | Enumerates the ability continuation results. You can use it in [onContinue()](arkts-ability-app-ability-uiability-uiability-c.md#onContinue) of the UIAbility to complete different operations. |
| [OnSaveResult](arkts-ability-abilityconstant-onsaveresult-e.md) | Enumerates the result types for the operation of saving application data. You can use it in [onSaveState()](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) of the UIAbility to complete [UIAbility backup and restore](../../../application-models/ability-recover-guideline.md). |
| [PrepareTermination](arkts-ability-abilityconstant-preparetermination-e.md) | Enumerates the actions triggered when an application is closed by the user. You can use it in [onPrepareTermination](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onPrepareTermination) or [onPrepareTerminationAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onPrepareTerminationAsync) of [AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md#AbilityStage). |
| [StateType](arkts-ability-abilityconstant-statetype-e.md) | Enumerates the scenarios for saving application data. You can use it in [onSaveState()](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) of the UIAbility to complete [UIAbility backup and restore](../../../application-models/ability-recover-guideline.md). |
| [WindowMode](arkts-ability-abilityconstant-windowmode-e.md) | Enumerates the window modes in which a UIAbility can be displayed at startup. It can be used in [startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) . |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [WindowMode](arkts-ability-abilityconstant-windowmode-e-sys.md) | Enumerates the window modes in which a UIAbility can be displayed at startup. It can be used in [startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) . |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [REASON_MESSAGE_DESKTOP_SHORTCUT](arkts-ability-abilityconstant-con.md#REASON_MESSAGE_DESKTOP_SHORTCUT) | The UIAbility is launched via a home screen shortcut. If this string is obtained from the **launchReasonMessage** property in [LaunchParam](arkts-ability-abilityconstant-launchparam-i.md#LaunchParam), the UIAbility is initiated by touching a shortcut on the home screen. |

