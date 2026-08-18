# getWakeupManager (System API)

## Modules to Import

```TypeScript
```

## getWakeupManager

```TypeScript
function getWakeupManager(): WakeupManager
```

Obtains an [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md#wakeupmanager-system-api) instance.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-intelligentVoice-function getWakeupManager(): WakeupManager--><!--Device-intelligentVoice-function getWakeupManager(): WakeupManager-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [22700107](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../../apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let wakeupManager: intelligentVoice.WakeupManager | null = null;
try {
  wakeupManager = intelligentVoice.getWakeupManager();
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get WakeupManager failed. Code:${error.code}, message:${error.message}`);
}
```
