# getTask

## getTask

```TypeScript
function getTask(context: BaseContext, id: string, token?: string): Promise<Task>
```

根据任务id查询任务。使用Promise异步回调。

**起始版本：** 11

<!--Device-agent-function getTask(context: BaseContext, id: string, token?: string): Promise<Task>--><!--Device-agent-function getTask(context: BaseContext, id: string, token?: string): Promise<Task>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| id | string | 是 |
| token | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Task&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [21900006](../../apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
