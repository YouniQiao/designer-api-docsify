# partition（系统接口）

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## partition

```TypeScript
function partition(diskId: string, type: int, callback: AsyncCallback<void>): void
```

对磁盘进行分区，使用callback异步回调。当前仅支持将磁盘设备重新分区为一个分区，系统是支持读取多分区的磁盘设备。 不支持对光盘进行分区。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_FORMAT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [diskId](arkts-corefile-volumemanager-volume-i-sys.md) | string | 是 |
| type | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600008 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// diskId可通过getAllDisks()接口获取
let diskId: string = "";
let type: number = 0;
volumeManager.partition(diskId, type).then(() => {
  console.info("partition successfully");
}).catch((error: BusinessError) => {
  console.error(`Failed to partition. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// diskId可通过getAllDisks()接口获取
let diskId: string = "";
let type: int = 0;
volumeManager.partition(diskId, type).then(() => {
  console.info("partition successfully");
}).catch((error: BusinessError): void => {
  console.error(`Failed to partition. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// diskId可通过getAllDisks()接口获取
let diskId: string = "";
let type: number = 0;
volumeManager.partition(diskId, type, (error: BusinessError) => {
  if (error) {
    console.error(`partition failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 对磁盘设备分区成功后的回调
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// diskId可通过getAllDisks()接口获取
let diskId: string = "";
let type: int = 0;
volumeManager.partition(diskId, type, (error: BusinessError | null) => {
  if (error) {
    console.error(`partition failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 对磁盘设备分区成功后的回调
});
```


## partition

```TypeScript
function partition(diskId: string, type: int): Promise<void>
```

对磁盘设备进行分区，使用Promise异步回调。当前仅支持将磁盘设备重新分区为一个分区，系统是支持读取多分区的磁盘设备。 不支持对光盘进行分区。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_FORMAT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [diskId](arkts-corefile-volumemanager-volume-i-sys.md) | string | 是 |
| type | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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
| 13600008 |
| 13900042 |

**示例**

参见 [partition](#partition)
