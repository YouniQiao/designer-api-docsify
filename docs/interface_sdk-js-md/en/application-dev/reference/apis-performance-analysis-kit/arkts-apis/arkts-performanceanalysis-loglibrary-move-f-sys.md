# move (System API)

## Modules to Import

```TypeScript
import { logLibrary } from 'kits/@kit.PerformanceAnalysisKit';
```

## move

```TypeScript
function move(logType: string, logName: string, dest: string): Promise<void>
```

移动指定日志类型的指定文件到目标应用目录下。使用Promise回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_HIVIEW_SYSTEM

<!--Device-logLibrary-function move(logType: string, logName: string, dest: string): Promise<void>--><!--Device-logLibrary-function move(logType: string, logName: string, dest: string): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| logType | string | Yes | 日志类型字符串，例如"FAULTLOG", "BETACLUB", "REMOTELOG"等。 |
| logName | string | Yes | 日志文件名称。 |
| dest | string | Yes | 目标目录，需填入相对目录名称。传入dest字串后，日志文件将保存到应用缓存路径下的"hiview/*dest*"文件夹，即"../cache/hiview/*dest*"。可填入多 层目录。 &lt;br&gt;如果传入空字串，将保存到根目录下，即应用缓存路径下的hiview文件夹。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，可以在其then()、catch()方法中分别对移动成功、移动异常的回调进行处理。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid argument. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| 21300001 | Source file does not exists |
| 201 | Permission denied |
| 202 | Permission denied, non-system app called system api |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let logObj = logLibrary.list('FAULTLOG');
  if (logObj.length > 0) {
    logLibrary.move('FAULTLOG', logObj[0].name, ''
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


## move

```TypeScript
function move(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

移动指定日志类型的指定文件到目标应用目录下。使用callback回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_HIVIEW_SYSTEM

<!--Device-logLibrary-function move(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-logLibrary-function move(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.LogLibrary

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| logType | string | Yes | 日志类型字符串，例如“HILOG”, "FAULTLOG", "BETACLUB", "REMOTELOG"等。 |
| logName | string | Yes | 日志文件名称。 |
| dest | string | Yes | 目标目录，需填入相对目录名称。传入dest字串后，日志文件将保存到应用缓存路径下的"hiview/*dest*"文件夹，即"../cache/hiview/*dest*"。可填入多 层目录。 &lt;br&gt;如果传入空字串，将保存到根目录下，即应用缓存路径下的hiview文件夹。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，可以在回调函数中处理接口返回值。0表示移动成功，其它值表示移动失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid argument. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| 21300001 | Source file does not exists |
| 201 | Permission denied |
| 202 | Permission denied, non-system app called system api |

## Examples

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logObj = logLibrary.list('FAULTLOG');
  if (logObj.length > 0) {
    logLibrary.move('FAULTLOG', logObj[0].name, 'dir1/dir2', (error, val) => {
      if (val === undefined) {
        // move failed.
      } else {
        // move success.
      }
    });
  }
} catch (error) {
    console.error(`error code: ${error?.code}, error msg: ${error?.message}`);
}
```

