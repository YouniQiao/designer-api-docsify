# setVolumeDescription（系统接口）

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## setVolumeDescription

```TypeScript
function setVolumeDescription(uuid: string, description: string, callback: AsyncCallback<void>): void
```

修改指定卷设备描述，使用callback异步回调。当前仅支持修改ntfs和exfat两种文件系统类型的设备描述， 只有处于卸载状态的卷设备可以修改设备描述。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |
| description | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600002 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
let description: string = "";
volumeManager.setVolumeDescription(uuid, description).then(() => {
  console.info("setVolumeDescription successfully");
}).catch((error: BusinessError) => {
  console.error(`Failed to setVolumeDescription. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
let description: string = "";
volumeManager.setVolumeDescription(uuid, description).then(() => {
  console.info("setVolumeDescription successfully");
}).catch((error: BusinessError): void => {
  console.error(`Failed to setVolumeDescription. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
let description: string = "";
volumeManager.setVolumeDescription(uuid, description, (error: BusinessError) => {
  if (error) {
    console.error(`setVolumeDescription failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 设置卷设备描述成功的回调
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
let description: string = "";
volumeManager.setVolumeDescription(uuid, description, (error: BusinessError | null) => {
  if (error) {
    console.error(`setVolumeDescription failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 设置卷设备描述成功的回调
});
```


## setVolumeDescription

```TypeScript
function setVolumeDescription(uuid: string, description: string): Promise<void>
```

修改指定卷设备描述，使用Promise异步回调。当前仅支持修改ntfs和exfat两种文件系统类型的设备描述， 只有处于卸载状态的卷设备可以修改设备描述。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |
| description | string | 是 |

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
| 13600002 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

参见 [setVolumeDescription](#setvolumedescription)
