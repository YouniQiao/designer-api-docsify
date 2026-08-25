# list（系统接口）

## 导入模块

```TypeScript
import { logLibrary } from 'kits/@kit.PerformanceAnalysisKit';
```

## list

```TypeScript
function list(logType: string): LogEntry[]
```

以同步方法查询指定类型的日志文件列表，接收string类型的对象作为参数，返回指定类型日志的文件列表信息。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
