# download

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## download

```TypeScript
function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void
```

创建并启动一个下载任务，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [downloadFile](arkts-basicservices-request-downloadfile-f.md)(context: BaseContext, config: DownloadConfig, callback: AsyncCallback&lt;DownloadTask&gt;)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## download

```TypeScript
function download(config: DownloadConfig): Promise<DownloadTask>
```

创建并启动一个下载任务，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [downloadFile](arkts-basicservices-request-downloadfile-f.md)(context: BaseContext, config: DownloadConfig)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
