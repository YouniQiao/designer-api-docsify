# copy（系统接口）

## 导入模块

```TypeScript
import { logLibrary } from 'kits/@kit.PerformanceAnalysisKit';
```

## copy

```TypeScript
function copy(logType: string, logName: string, dest: string): Promise<void>
```

拷贝指定日志类型的指定文件到目标应用目录下。使用Promise回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-指定文件不存在) |


## copy

```TypeScript
function copy(logType: string, logName: string, dest: string, callback: AsyncCallback<void>): void
```

拷贝指定日志类型的指定文件到目标应用目录下。使用callback回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_HIVIEW_SYSTEM

**系统能力：** SystemCapability.HiviewDFX.Hiview.LogLibrary

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| logType | string | 是 |
| logName | string | 是 |
| dest | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21300001](../errorcode-loglibrary-sys.md#21300001-指定文件不存在) |
