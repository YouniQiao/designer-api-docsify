# isStartupTaskInitialized

## Modules to Import

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## isStartupTaskInitialized

```TypeScript
function isStartupTaskInitialized(startupTask: string): boolean
```

Checks whether a startup task or .so file preloading task is initialized.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTask | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
