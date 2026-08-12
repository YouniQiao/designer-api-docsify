# remove (System API)

## Modules to Import

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
```

## remove

```TypeScript
function remove(logType: string, logName: string): void
```

Deletes log files of the specified type in synchronous mode.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_HIVIEW_SYSTEM

<!--Device-logLibrary-function remove(logType: string, logName: string): void--><!--Device-logLibrary-function remove(logType: string, logName: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| logType | string | Yes | Log type, for example, **FAULTLOG**, **BETACLUB**, or **REMOTELOG**. |
| logName | string | Yes | Log file name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid argument. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [21300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-performance-analysis-kit/errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) | Source file does not exists |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  logLibrary.remove('FAULTLOG', 'fault_log_test.zip');
} catch (error) {
  console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```

