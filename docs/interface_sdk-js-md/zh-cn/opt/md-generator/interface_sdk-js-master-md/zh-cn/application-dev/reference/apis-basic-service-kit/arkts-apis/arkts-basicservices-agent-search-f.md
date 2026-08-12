# search

## search

```TypeScript
function search(callback: AsyncCallback<Array<string>>): void
```

根据默认[Filter](arkts-basicservices-agent-filter-i.md#Filter)过滤条件查找任务id，即查询调用时刻至24小时前的所有任务的任务id。使用callback异步回调。

**起始版本：** 10

<!--Device-agent-function search(callback: AsyncCallback<Array<string>>): void--><!--Device-agent-function search(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## search

```TypeScript
function search(filter: Filter, callback: AsyncCallback<Array<string>>): void
```

根据[Filter](arkts-basicservices-agent-filter-i.md#Filter)过滤条件查找任务id。使用callback异步回调。

**起始版本：** 10

<!--Device-agent-function search(filter: Filter, callback: AsyncCallback<Array<string>>): void--><!--Device-agent-function search(filter: Filter, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-basicservices-agent-filter-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |


## search

```TypeScript
function search(filter?: Filter): Promise<Array<string>>
```

根据[Filter](arkts-basicservices-agent-filter-i.md#Filter)过滤条件查找任务id。使用Promise异步回调。

**起始版本：** 10

<!--Device-agent-function search(filter?: Filter): Promise<Array<string>>--><!--Device-agent-function search(filter?: Filter): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-basicservices-agent-filter-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [13400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |
