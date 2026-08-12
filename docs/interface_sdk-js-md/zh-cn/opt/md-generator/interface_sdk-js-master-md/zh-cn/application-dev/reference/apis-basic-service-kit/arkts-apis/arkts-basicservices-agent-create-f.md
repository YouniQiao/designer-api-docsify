# create

## create

```TypeScript
function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void
```

创建需要上传或下载的任务，并将其排入队列。支持HTTP/HTTPS协议，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-agent-function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void--><!--Device-agent-function create(context: BaseContext, config: Config, callback: AsyncCallback<Task>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [Config](arkts-basicservices-agent-config-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Task&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [21900004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900004-应用任务队列已满) |
| [21900005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400001-文件操作异常) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## create

```TypeScript
function create(context: BaseContext, config: Config): Promise<Task>
```

创建需要上传或下载的任务，并将其排入队列。支持HTTP/HTTPS协议，使用Promise异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-agent-function create(context: BaseContext, config: Config): Promise<Task>--><!--Device-agent-function create(context: BaseContext, config: Config): Promise<Task>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [Config](arkts-basicservices-agent-config-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Task & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [21900004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900004-应用任务队列已满) |
| [21900005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400001-文件操作异常) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
