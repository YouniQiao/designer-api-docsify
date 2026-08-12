# copy（系统接口）

## copy

```TypeScript
function copy(logType: string, logName: string, dest: string): Promise<void>
```

拷贝指定日志类型的指定文件到目标应用目录下。使用Promise回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string): Promise<void>-End-->

**系统能力：** SystemCapability.HiviewDFX.Hiview.LogLibrary

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| logType | string | 是 |
| logName | string | 是 |
| dest | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [21300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-loglibrary-sys.md#21300001-指定文件不存在) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let logFiles = logLibrary.list('HILOG');
  if (logFiles.length > 0) {
    logLibrary.copy('HILOG', logFiles[0].name, ''
    ).then(
      (copyResult) => {
        // do something here.
      }
    ).catch(
      (err: BusinessError) => {
        // do something here.
      }
    )
  }
} catch (error) {
    console.error(`Failed to call logLibrary API. Code: ${error?.code}, message: ${error?.message}`);
}
```


## copy

```TypeScript
function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

拷贝指定日志类型的指定文件到目标应用目录下。使用callback回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-logLibrary-function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.HiviewDFX.Hiview.LogLibrary

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| logType | string | 是 |
| logName | string | 是 |
| dest | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [21300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-loglibrary-sys.md#21300001-指定文件不存在) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logFiles = logLibrary.list('HILOG');
  if (logFiles.length > 0) {
    logLibrary.copy('HILOG', logFiles[0].name, 'dir1', (error, copyResult) => {
      if (error) {
        console.error(`Failed to copy log file. Code: ${error.code}, message: ${error.message}`);
      } else {
        // copy success.
      }
    });
  }
} catch (error) {
    console.error(`Failed to call logLibrary API. Code: ${error?.code}, message: ${error?.message}`);
}
```
