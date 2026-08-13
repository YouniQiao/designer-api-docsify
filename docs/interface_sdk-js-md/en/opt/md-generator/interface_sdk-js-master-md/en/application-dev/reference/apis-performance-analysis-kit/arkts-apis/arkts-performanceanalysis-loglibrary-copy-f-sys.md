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

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |
| logName | string | Yes |
| dest | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let logObj = logLibrary.list('HILOG');
  if (logObj.length > 0) {
    logLibrary.copy('HILOG', logObj[0].name, ''
    ).then(
      (val) => {
        // do something here.
      }
    ).catch(
      (err: BusinessError) => {
        // do something here.
      }
    )
  }
} catch (error) {
    console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```


## copy

```TypeScript
function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

Copies log files of the specified type to the target application directory. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| logType | string | Yes |
| logName | string | Yes |
| dest | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-specified-file-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logObj = logLibrary.list('HILOG');
  if (logObj.length > 0) {
    logLibrary.copy('HILOG', logObj[0].name, 'dir1', (error, val) => {
      if (val === undefined) {
        // copy failed.
      } else {
        // copy success.
      }
    });
  }
} catch (error) {
    console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```
