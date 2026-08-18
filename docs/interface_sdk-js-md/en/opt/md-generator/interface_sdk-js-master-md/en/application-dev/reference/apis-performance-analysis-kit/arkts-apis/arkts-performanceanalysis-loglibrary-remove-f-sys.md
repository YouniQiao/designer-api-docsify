# remove (System API)

## Modules to Import

```TypeScript
```

## remove

```TypeScript
function remove(logType: string, logName: string): void
```

Deletes log files of the specified type in synchronous mode.

**Since:** 23

**Required permissions:** ohos.permission.WRITE_HIVIEW_SYSTEM

<!--Device-logLibrary-function remove(logType: string, logName: string): void--><!--Device-logLibrary-function remove(logType: string, logName: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |
| logName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logObj = logLibrary.list('FAULTLOG');
  if (logObj.length > 0) {
    logLibrary.remove('FAULTLOG', logObj[0].name);
  }
} catch (error) {
  console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```
