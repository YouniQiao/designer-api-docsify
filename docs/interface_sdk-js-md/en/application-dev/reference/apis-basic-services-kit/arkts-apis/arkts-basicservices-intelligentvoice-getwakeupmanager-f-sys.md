# getWakeupManager (System API)

## Modules to Import

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## getWakeupManager

```TypeScript
function getWakeupManager(): WakeupManager
```

Obtains an [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md) instance.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [22700101](../errorcode-intelligentVoice.md#22700101-insufficient-memory) |
| [22700107](../errorcode-intelligentVoice.md#22700107-system-error) |
