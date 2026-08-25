# getAutoStartupStatusForSelf

## Modules to Import

```TypeScript
import { autoStartupManager } from 'kits/@kit.AbilityKit';
```

## getAutoStartupStatusForSelf

```TypeScript
function getAutoStartupStatusForSelf(): Promise<boolean>
```

Checks whether the current application is enabled for automatic startup at boot time. This API uses a promise to return the result. This API can be properly called only on phones, PC/2-in-1 devices, tablets, and wearables. On other devices, it returns the error code 801.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
