# removeStartupTaskResult

## Modules to Import

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## removeStartupTaskResult

```TypeScript
function removeStartupTaskResult(startupTask: string): void
```

Removes the initialization result of a startup task or .so file preloading task.  
- If a startup task name is passed, the initialization result of that startup task is removed.  
- If a .so file is passed, the .so file is set to the unloaded state, but the loaded .so file in the cache is not  
removed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTask | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
