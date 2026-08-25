# IncrementalBackupSession（系统接口）

增量备份流程对象，用于支撑应用增量备份流程。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## appendBundles

```TypeScript
appendBundles(bundlesToBackup: Array<IncrementalBackupData>): Promise<void>
```

添加需要增量备份的应用。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundlesToBackup | Array&lt;[IncrementalBackupData](arkts-corefile-backup-incrementalbackupdata-i.md)&gt; | 是 |

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
| 13900011 |
| 13900025 |
| 13900042 |

## appendBundles

```TypeScript
appendBundles(bundlesToAppend: Array<IncrementalBackupData>, infos: string[]): Promise<void>
```

添加需要增量备份的应用。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundlesToAppend | Array&lt;[IncrementalBackupData](arkts-corefile-backup-incrementalbackupdata-i.md)&gt; | 是 |
| infos | string[] | 是 |

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
| 13900011 |
| 13900025 |
| 13900042 |

## cancel

```TypeScript
cancel(bundleName: string): number
```

取消指定应用的增量备份任务。

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

构造IncrementalBackupSession实例。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [callbacks](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-appstatefilter-i-sys.md) | [GeneralCallbacks](arkts-corefile-backup-generalcallbacks-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getBackupDataSize

```TypeScript
getBackupDataSize(isPreciseScan: boolean, dataList: Array<IncrementalBackupTime>): Promise<void>
```

获取应用待备份数据量。

**起始版本：** 18

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isPreciseScan | boolean | 是 |
| [dataList](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponent-s.md) | Array&lt;[IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md)&gt; | 是 |

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
| 13900020 |
| 13900042 |

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

## release

```TypeScript
release(): Promise<void>
```

结束增量备份流程，断开应用与备份恢复服务的连接。

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
