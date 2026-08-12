# list（系统接口）

## list

```TypeScript
function list(logType: string): LogEntry[]
```

以同步方法查询指定类型的日志文件列表，接收string类型的对象作为参数，返回指定类型日志的文件列表信息。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

<!--Device-logLibrary-function list(logType: string): LogEntry[]--><!--Device-logLibrary-function list(logType: string): LogEntry[]-End-->

**系统能力：** SystemCapability.HiviewDFX.Hiview.LogLibrary

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| logType | string | 是 |

**返回值：**

| 类型 |
| --- |
| [LogEntry](arkts-performanceanalysis-loglibrary-logentry-i-sys.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { logLibrary } from '@kit.PerformanceAnalysisKit';

try {
  let logFiles = logLibrary.list('HILOG');
  // do something here.
} catch (error) {
  console.error(`Failed to call logLibrary API. Code: ${error?.code}, message: ${error?.message}`);
}
```
