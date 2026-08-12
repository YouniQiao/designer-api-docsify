# copy (System API)

## Modules to Import

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
```

## copy

```TypeScript
function copy(logType: string, logName: string, dest: string): Promise<void>
```

Copies log files of the specified type to the target application directory. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| logType | string | Yes | Log type, for example, **HILOG**, **FAULTLOG**, **BETACLUB**, or **REMOTELOG**. |
| logName | string | Yes | Log file name. |
| dest | string | Yes | Target directory. Enter the relative path of the directory. If this parameter is specified, log files will be saved to the **hiview/dest** folder in the application cache path, that is, **../cache/hiview/dest**. You can enter a multi-level directory. &lt;br&gt;If you leave this parameter empty, log files will be saved to the root directory, that is, the **hiview** folder in the application cache path. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. Depending on whether the operation is successful, you can use the **then()** or **catch()** method to process the callback. |

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
import { BusinessError } from '@kit.BasicServicesKit';

try {
    logLibrary.copy('HILOG', 'hiapplogcat-1.zip', ''
    ).then(
        (val) => {
            // do something here.
        }
    ).catch(
        (err: BusinessError) => {
            // do something here.
        }
    )
} catch (error) {
    console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```


## copy

```TypeScript
function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

Copies log files of the specified type to the target application directory. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| logType | string | Yes | Log type, for example, **HILOG**, **FAULTLOG**, **BETACLUB**, or **REMOTELOG**. |
| logName | string | Yes | Log file name. |
| dest | string | Yes | Target directory. Enter the relative path of the directory. If this parameter is specified, log files will be saved to the **hiview/dest** folder in the application cache path, that is, **../cache/hiview/dest**. You can enter a multi-level directory. &lt;br&gt;If you leave this parameter empty, log files will be saved to the root directory, that is, the **hiview** folder in the application cache path. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to process the received return value. The value **0** indicates that the operation is successful, and any other value indicates that the operation has failed. |

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
    logLibrary.copy('HILOG', 'hiapplogcat-1.zip', 'dir1', (error, val) => {
        if (val === undefined) {
            // copy failed.
        } else {
            // copy success.
        }
    });
} catch (error) {
    console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```

