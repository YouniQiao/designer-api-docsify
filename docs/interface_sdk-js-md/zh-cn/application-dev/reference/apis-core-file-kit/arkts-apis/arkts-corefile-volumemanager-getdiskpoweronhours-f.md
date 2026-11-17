# getDiskPowerOnHours

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getDiskPowerOnHours

```TypeScript
function getDiskPowerOnHours(sysPath: string): Promise<number>
```

获取指定磁盘自出厂以来的总通电时长，使用Promise异步回调。如果ioctl读取失败（如SATA HDD不支持），返回0。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DISK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-volumeManager-function getDiskPowerOnHours(sysPath: string): Promise<int>--><!--Device-volumeManager-function getDiskPowerOnHours(sysPath: string): Promise<int>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sysPath | string | 是 | 磁盘设备节点的物理路径，如/sys/block/nvme0n1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回磁盘通电时长。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| 13600001 | IPC error. |
| 13600002 | The file system is not supported. |
| 13600008 | The object does not exist. |
