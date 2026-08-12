# touch

## touch

```TypeScript
function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void
```

根据任务id和token查询任务的详细信息。使用callback异步回调。

**起始版本：** 10

<!--Device-agent-function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void--><!--Device-agent-function touch(id: string, token: string, callback: AsyncCallback<TaskInfo>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [21900006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## touch

```TypeScript
function touch(id: string, token: string): Promise<TaskInfo>
```

根据任务id和token查询任务的详细信息。使用Promise异步回调。

**起始版本：** 10

<!--Device-agent-function touch(id: string, token: string): Promise<TaskInfo>--><!--Device-agent-function touch(id: string, token: string): Promise<TaskInfo>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;TaskInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [21900006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900006-操作不存在的任务错误) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
