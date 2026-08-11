# @ohos.resourceschedule.backgroundProcessManager(Background Child Process Management)

The **backgroundProcessManager** module provides APIs for background child process management. You can use these APIs to suppress and unsuppress child processes to prevent child processes from occupying too many system resources and causing system stuttering. The APIs take effect only for the child processes created through   
[OH_Ability_StartNativeChildProcess](../../../reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess).

**Since:** 17

<!--Device-unnamed-declare namespace backgroundProcessManager--><!--Device-unnamed-declare namespace backgroundProcessManager-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

## Modules to Import

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-getpowersavemode-f.md#getpowersavemode) |
| [isPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-ispowersavemode-f.md#ispowersavemode) |
| [resetProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-resetprocesspriority-f.md#resetprocesspriority) |
| [setPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-setpowersavemode-f.md#setpowersavemode) |
| [setProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-setprocesspriority-f.md#setprocesspriority) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) |
| [ProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-processpriority-e.md) |
