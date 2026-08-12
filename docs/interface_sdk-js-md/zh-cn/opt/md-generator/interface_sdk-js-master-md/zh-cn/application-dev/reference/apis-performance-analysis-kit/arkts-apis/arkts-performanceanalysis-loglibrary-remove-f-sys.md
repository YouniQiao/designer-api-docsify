# remove（系统接口）

## remove

```TypeScript
function remove(logType: string, logName: string): void
```

以同步方法删除指定日志类型的指定文件。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_HIVIEW_SYSTEM

<!--Device-logLibrary-function remove(logType: string, logName: string): void--><!--Device-logLibrary-function remove(logType: string, logName: string): void-End-->

**系统能力：** SystemCapability.HiviewDFX.Hiview.LogLibrary

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| logType | string | 是 |
| logName | string | 是 |

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
  let logFiles = logLibrary.list('FAULTLOG');
  if (logFiles.length > 0) {
    logLibrary.remove('FAULTLOG', logFiles[0].name);
  }
} catch (error) {
  console.error(`Failed to call logLibrary API. Code: ${error?.code}, message: ${error?.message}`);
}
```
