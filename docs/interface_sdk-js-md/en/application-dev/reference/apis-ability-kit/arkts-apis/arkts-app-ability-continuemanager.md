# @ohos.app.ability.continueManager

The continueManager module provides capabilities for managing cross-device application migration. For example, it allows you to obtain the result of quickly launching the target application during the cross-device migration process.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace continueManager--><!--Device-unnamed-declare namespace continueManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off](arkts-ability-continuemanager-off-f.md#off) | Unregisters the callback used to obtain the quick start result when an application is launched quickly. This API uses an asynchronous callback to return the result. |
| [offPrepareContinue](arkts-ability-continuemanager-offpreparecontinue-f.md#offpreparecontinue) | Unregister prepareContinue event. |
| [on](arkts-ability-continuemanager-on-f.md#on) | Registers a callback to obtain the quick start result when an application is launched quickly. This API uses an asynchronous callback to return the result. |
| [onPrepareContinue](arkts-ability-continuemanager-onpreparecontinue-f.md#onpreparecontinue) | Register prepareContinue event, when the ability is configured with 'ContinueQuickStart' in the continueType, then can get the result of LaunchReason.PREPARE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CONTINUATION. |

### Interfaces

| Name | Description |
| --- | --- |
| [ContinueResultInfo](arkts-ability-continuemanager-continueresultinfo-i.md) | Describes the quick start result returned by the callback. |

### Enums

| Name | Description |
| --- | --- |
| [ContinueStateCode](arkts-ability-continuemanager-continuestatecode-e.md) | Enumerates the status codes of the quick start result. |

