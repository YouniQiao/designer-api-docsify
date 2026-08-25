# SyncFolderAccessor（系统接口）

同步根管理类，负责为系统文件管理应用提供获取三方网盘注册的同步根信息的能力。

**起始版本：** 21

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudDiskManager } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

SyncFolderAccessor的构造函数，用于获取SyncFolderAccessor类的实例。

**起始版本：** 21

**需要权限：** ohos.permission.ACCESS_CLOUD_DISK_INFO

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getAllSyncFolders

```TypeScript
getAllSyncFolders(): Promise<Array<SyncFolder>>
```

获取所有注册的同步根信息。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.ACCESS_CLOUD_DISK_INFO

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[SyncFolder](arkts-corefile-clouddiskmanager-syncfolder-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34400003](../errorcode-clouddiskmanager-sys.md#34400003-ipc通信失败) |
| [34400014](../errorcode-clouddiskmanager-sys.md#34400014-系统内部错误) |
| [34400015](../errorcode-clouddiskmanager-sys.md#34400015-当前设备不允许使用云盘功能) |
