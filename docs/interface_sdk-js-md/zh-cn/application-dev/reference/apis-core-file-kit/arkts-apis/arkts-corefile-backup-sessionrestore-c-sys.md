# SessionRestore（系统接口）

恢复流程对象，用于支撑应用全量恢复流程。

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## appendBundles

```TypeScript
appendBundles(remoteCapabilitiesFd: number, bundlesToBackup: string[], infos?: string[]): Promise<void>
```

添加需要恢复的应用及其扩展信息。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| remoteCapabilitiesFd | number | 是 |
| bundlesToBackup | string[] | 是 |
| infos | string[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |
| 13900042 |

## appendBundles

```TypeScript
appendBundles(remoteCapabilitiesFd: number, bundlesToBackup: string[], callback: AsyncCallback<void>): void
```

添加需要恢复的应用。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| remoteCapabilitiesFd | number | 是 |
| bundlesToBackup | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |
| 13900042 |

## cancel

```TypeScript
cancel(bundleName: string): number
```

取消指定应用的恢复任务。

**起始版本：** 18

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## cleanBundleTempDir

```TypeScript
cleanBundleTempDir(bundleName: string): Promise<boolean>
```

清理指定应用的临时目录。

**起始版本：** 20

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## constructor

```TypeScript
constructor(callbacks: GeneralCallbacks)
```

构造SessionRestore实例。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [callbacks](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-appstatefilter-i-sys.md) | [GeneralCallbacks](arkts-corefile-backup-generalcallbacks-i-sys.md) | 是 |

## getApkFileHandle

```TypeScript
getApkFileHandle(path: string, fileName: string): Promise<FileData>
```

获取APK文件的文件句柄。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.BACKUP

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| fileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900001 |
| 13900020 |

## getCompatibilityInfo

```TypeScript
getCompatibilityInfo(bundleName: string, extInfo: string): Promise<string>
```

获取指定应用的兼容性信息。

**起始版本：** 20

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| extInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getFileHandle

```TypeScript
getFileHandle(fileMeta: FileMeta): Promise<void>
```

向服务端请求共享文件，该接口属于零拷贝能力。 开发者可通过onFileReady回调获取文件。 客户端完成文件处理后，调用publishFile发布文件。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## getFileHandle

```TypeScript
getFileHandle(fileMeta: FileMeta, callback: AsyncCallback<void>): void
```

向服务端请求共享文件，该接口属于零拷贝能力。 开发者可通过onFileReady回调获取文件。 客户端完成文件处理后，调用publishFile发布文件。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## getFileHandles

```TypeScript
getFileHandles(fileMeta: FileMeta): Promise<void>
```

向服务端批量请求共享文件，该接口属于零拷贝能力。 开发者可通过onFileReadyBatch回调获取文件。 客户端完成文件处理后，调用publishFile发布文件。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.BACKUP

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900001 |
| 13900020 |

## getLocalCapabilities

```TypeScript
getLocalCapabilities(): Promise<FileData>
```

获取描述本地能力的JSON文件。

**起始版本：** 18

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## migrateFile

```TypeScript
migrateFile(pathInfo: PathInfo, fileMeta: FileMeta): Promise<void>
```

将文件从源路径迁移到目标路径。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.BACKUP

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pathInfo](../../apis-arkui/arkts-components/arkts-arkui-navdestinationcontext-i.md) | [PathInfo](arkts-corefile-backup-pathinfo-i-sys.md) | 是 |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900001 |
| 13900020 |

## publishFile

```TypeScript
publishFile(fileMeta: FileMeta): Promise<void>
```

向备份服务发布文件句柄，通知服务端文件内容已准备完成。 该接口属于零拷贝能力。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## publishFile

```TypeScript
publishFile(fileMeta: FileMeta, callback: AsyncCallback<void>): void
```

向备份服务发布文件句柄，通知服务端文件内容已准备完成。 该接口属于零拷贝能力。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## release

```TypeScript
release(): Promise<void>
```

结束恢复流程，断开应用与备份恢复服务的连接。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

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
| 13600001 |
| 13900001 |
| 13900005 |
| 13900042 |
