# queryAppKeyState

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## queryAppKeyState

```TypeScript
function queryAppKeyState(): KeyStatus
```

Queries the status of the caller app's sensitive data key under the lock screen in synchronous mode.

**Since:** 18

**System capability:** SystemCapability.Security.ScreenLockFileManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-system-service-abnormal) |
