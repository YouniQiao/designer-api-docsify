# listUserdataDirInfo（系统接口）

## 导入模块

```TypeScript
```

## listUserdataDirInfo

```TypeScript
function listUserdataDirInfo(): Promise<Array<UserdataDirInfo>>
```

查询用户设备中/data目录下的空间占用详情，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-storageStatistics-function listUserdataDirInfo(): Promise<Array<UserdataDirInfo>>--><!--Device-storageStatistics-function listUserdataDirInfo(): Promise<Array<UserdataDirInfo>>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[UserdataDirInfo](arkts-corefile-storagestatistics-userdatadirinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600015 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

**示例**

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.listUserdataDirInfo().then((dirInfos: storageStatistics.UserdataDirInfo[]) => {
  console.info("listUserdataDirInfo successfully.");
}).catch((err: BusinessError) => {
  console.error(`listUserdataDirInfo failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
