# list (System API)

## Modules to Import

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
```

## list

```TypeScript
function list(logType: string): LogEntry[]
```

Obtains the list of log files of the specified type in synchronous mode. This API accepts objects of the string type as input parameters and returns a list log files of the specified type.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function list(logType: string): LogEntry[]--><!--Device-logLibrary-function list(logType: string): LogEntry[]-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LogEntry](arkts-performanceanalysis-loglibrary-logentry-i-sys.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logObj = logLibrary.list('HILOG');
  // do something here.
} catch (error) {
  console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```
