# getLocalCapabilities（系统接口）

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getLocalCapabilities

```TypeScript
function getLocalCapabilities(): Promise<FileData>
```

获取描述本地能力的JSON文件。

**起始版本：** 10

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
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(callback: AsyncCallback<FileData>): void
```

获取描述本地能力的JSON文件。

**起始版本：** 10

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>
```

获取描述本地能力的JSON文件。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dataList](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponent-s.md) | Array&lt;[IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |
