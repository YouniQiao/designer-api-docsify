# getWakeupManager (System API)

## Modules to Import

```TypeScript
import { intelligentVoice } from '@kit.BasicServicesKit';
```

## getWakeupManager

```TypeScript
function getWakeupManager(): WakeupManager
```

Obtains an [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md#WakeupManager) instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-intelligentVoice-function getWakeupManager(): WakeupManager--><!--Device-intelligentVoice-function getWakeupManager(): WakeupManager-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [22700107](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-intelligentVoice.md#22700107-system-error) | System error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [22700101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-intelligentVoice.md#22700101-insufficient-memory) | No memory. |

## Examples

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

