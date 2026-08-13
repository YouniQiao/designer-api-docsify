# query（系统接口）

## query

```TypeScript
function query(id: string, callback: AsyncCallback<TaskInfo>): void
```

Queries specified task details. Creates a group based on GroupConfig

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.DOWNLOAD_SESSION_MANAGER or ohos.permission.UPLOAD_SESSION_MANAGER

<!--Device-agent-function query(id: string, callback: AsyncCallback<TaskInfo>): void--><!--Device-agent-function query(id: string, callback: AsyncCallback<TaskInfo>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## query

```TypeScript
function query(id: string): Promise<TaskInfo>
```

Queries specified task details.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.DOWNLOAD_SESSION_MANAGER or ohos.permission.UPLOAD_SESSION_MANAGER

<!--Device-agent-function query(id: string): Promise<TaskInfo>--><!--Device-agent-function query(id: string): Promise<TaskInfo>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;TaskInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
