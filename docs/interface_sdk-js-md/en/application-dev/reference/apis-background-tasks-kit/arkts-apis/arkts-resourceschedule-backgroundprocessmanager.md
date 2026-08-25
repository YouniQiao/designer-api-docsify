# @ohos.resourceschedule.backgroundProcessManager(Background Child Process Management)

The **backgroundProcessManager** module provides APIs for background child process management. You can use these APIs to suppress and unsuppress child processes to prevent child processes from occupying too many system resources and causing system stuttering. The APIs take effect only for the child processes created through [OH_Ability_StartNativeChildProcess](../../../reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess).

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

## Modules to Import

```TypeScript
import { backgroundProcessManager } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerSaveMode(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-getpowersavemode-f.md) |
| [isPowerSaveMode(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-ispowersavemode-f.md) |
| [resetProcessPriority(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-resetprocesspriority-f.md) |
| [setPowerSaveMode(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-setpowersavemode-f.md) |
| [setProcessPriority(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-setprocesspriority-f.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PowerSaveMode(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) |
| [ProcessPriority(Background Child Process Management)](arkts-backgroundtasks-backgroundprocessmanager-processpriority-e.md) |
