# GeneralCallbacks（系统接口）

备份和恢复过程中的通用回调。 备份服务通过这些回调向客户端通知备份或恢复阶段。@interface GeneralCallbacks

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## onBackupSizeReport

```TypeScript
onBackupSizeReport?: OnBackupSizeReport
```

备份服务返回结果或进度信息时触发的回调。 返回框架扫描到的应用待备份数据量信息。

**起始版本：** 18

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onFileReadyBatch

```TypeScript
onFileReadyBatch?: OnFileReadyBatch
```

备份服务向客户端发送文件时触发的回调。 File参数表示发送给客户端的文件。 返回的文件归备份服务所有，客户端关闭文件句柄后由备份服务清理。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |

## onProcess

```TypeScript
onProcess(bundleName: string, process: string): void
```

备份服务返回结果或进度信息时触发的回调。 返回应用的处理结果或进度信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| process | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13500006 |
| 13500008 |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |

## onResultReport

```TypeScript
onResultReport(bundleName: string, result: string): void
```

备份服务返回结果信息时触发的回调。 第一个字符串参数表示触发回调的应用名称。 第二个字符串参数表示应用的处理结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| result | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |

## onAllBundlesEnd

```TypeScript
onAllBundlesEnd: AsyncCallback<undefined>
```

所有应用的备份或恢复完成或异常中止时触发的回调。

**类型：** [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;undefined&gt;

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onBackupServiceDied

```TypeScript
onBackupServiceDied: Callback<undefined>
```

备份服务异常死亡时触发的回调。

**类型：** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;undefined&gt;

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onBundleBegin

```TypeScript
onBundleBegin: AsyncCallback<string, void | string>
```

应用备份或恢复开始时触发的回调。 第一个字符串参数表示应用名称。 发生BusinessError时，第二个字符串参数 返回对应的应用名称。

**类型：** [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onBundleEnd

```TypeScript
onBundleEnd: AsyncCallback<string, void | string>
```

应用备份或恢复成功结束或异常中止时触发的回调。 第一个字符串参数表示应用名称。 发生BusinessError时，第二个字符串参数 返回对应的应用名称。

**类型：** [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onFileReady

```TypeScript
onFileReady: AsyncCallback<File>
```

备份服务向客户端发送文件时触发的回调。 File参数表示发送给客户端的文件。 返回的文件归备份服务所有，客户端关闭文件句柄后由备份服务清理。

**类型：** [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;File&gt;

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## onMigrateResult

```TypeScript
onMigrateResult?: AsyncCallback<string, void | string>
```

文件迁移流程结束时触发的回调。 第一个字符串参数表示应用名称。 发生BusinessError时，第二个字符串参数 返回对应的应用名称。

**类型：** [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。
