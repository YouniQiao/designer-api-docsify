# show

## show

```TypeScript
function show(id: string, callback: AsyncCallback<TaskInfo>): void
```

根据任务id查询任务的详细信息。使用callback异步回调。

**起始版本：** 10

<!--Device-agent-function show(id: string, callback: AsyncCallback<TaskInfo>): void--><!--Device-agent-function show(id: string, callback: AsyncCallback<TaskInfo>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## show

```TypeScript
function show(id: string): Promise<TaskInfo>
```

根据任务id查询任务的详细信息。使用Promise异步回调。

**起始版本：** 10

<!--Device-agent-function show(id: string): Promise<TaskInfo>--><!--Device-agent-function show(id: string): Promise<TaskInfo>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;TaskInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
