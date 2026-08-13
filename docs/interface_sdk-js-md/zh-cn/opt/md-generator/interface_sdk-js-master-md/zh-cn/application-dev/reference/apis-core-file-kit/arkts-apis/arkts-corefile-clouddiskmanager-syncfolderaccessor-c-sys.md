# SyncFolderAccessor（系统接口）

同步根管理类，负责为系统文件管理应用提供获取三方网盘注册的同步根信息的能力。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cloudDiskManager-class SyncFolderAccessor--><!--Device-cloudDiskManager-class SyncFolderAccessor-End-->

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

## constructor

```TypeScript
constructor()
```

SyncFolderAccessor的构造函数，用于获取SyncFolderAccessor类的实例。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_CLOUD_DISK_INFO

<!--Device-SyncFolderAccessor-constructor()--><!--Device-SyncFolderAccessor-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { cloudDiskManager } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('constructor')
      .onClick(async() => {
          try {
            let syncFolderAccessor: cloudDiskManager.SyncFolderAccessor = new cloudDiskManager.SyncFolderAccessor();
          } catch (err) {
              let error: BusinessError = err as BusinessError;
              console.error(`SyncFolderAccessor constructor failed. Code: ${error.code}, message: ${error.message}`);
          }
      });
    }
  }
}
```

## getAllSyncFolders

```TypeScript
getAllSyncFolders(): Promise<Array<SyncFolder>>
```

获取所有注册的同步根信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_CLOUD_DISK_INFO

<!--Device-SyncFolderAccessor-getAllSyncFolders(): Promise<Array<SyncFolder>>--><!--Device-SyncFolderAccessor-getAllSyncFolders(): Promise<Array<SyncFolder>>-End-->

**系统能力：** SystemCapability.FileManagement.CloudDiskManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[SyncFolder](arkts-corefile-clouddiskmanager-syncfolder-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34400014](../errorcode-clouddiskmanager-sys.md#34400014-系统内部错误) |
| [34400015](../errorcode-clouddiskmanager-sys.md#34400015-当前设备不允许使用云盘功能) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [34400003](../errorcode-clouddiskmanager-sys.md#34400003-ipc通信失败) |

## 示例

```TypeScript
import { cloudDiskManager } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
const TAG: string = '[cloudDiskManager]';

try {
    console.info(`${TAG}getAllSyncFolders start`);
    let syncFolderAccessor: cloudDiskManager.SyncFolderAccessor = new cloudDiskManager.SyncFolderAccessor();
    syncFolderAccessor.getAllSyncFolders().then((syncFolders) => {
        console.info(`${TAG}getAllSyncFolders success, length: ${syncFolders.length}`);
        for (let i = 0; i < syncFolders.length; ++i) {
            console.info(`${TAG}syncFolders[${i}].path: ${syncFolders[i].path}`);
            console.info(`${TAG}syncFolders[${i}].bundleName: ${syncFolders[i].bundleName}`);
            console.info(`${TAG}syncFolders[${i}].state: ${syncFolders[i].state}`);
            if (syncFolders[i].displayNameResId) {
                console.info(`${TAG}syncFolders[${i}].displayNameResId: ${syncFolders[i].displayNameResId}`);
            }
            if (syncFolders[i].customAlias) {
                console.info(`${TAG}syncFolders[${i}].customAlias: ${syncFolders[i].customAlias}`);
            }
        }
    }).catch((err: BusinessError<object>) => {
        console.error(`${TAG}Failed to getAllSyncFolders. Code: ${err.code}, message: ${err.message}`);
    });
} catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error(`${TAG}getAllSyncFolders failed. Code: ${error.code}, message: ${error.message}`);
}
```
