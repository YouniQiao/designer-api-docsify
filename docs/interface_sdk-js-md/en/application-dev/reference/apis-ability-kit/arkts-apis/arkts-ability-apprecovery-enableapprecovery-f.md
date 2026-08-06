# enableAppRecovery

## enableAppRecovery

```TypeScript
function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void
```

Enables application recovery. After this API is called, the first ability that is displayed when the application is started from the initiator can be restored.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void--><!--Device-appRecovery-function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| restart | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Whether the application is restarted upon a fault. By default, the application is restarted. |
| saveOccasion | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Scenario for saving the application state. By default, the state is saved when a fault occurs. |
| saveMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Application state saving mode. By default, the application state is written to the local file cache. |

