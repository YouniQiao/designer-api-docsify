# mount（系统接口）

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## mount

```TypeScript
function mount(volumeId: string, callback: AsyncCallback<void>): void
```

挂载指定卷设备，使用callback异步回调。当前仅支持vfat、exfat以及ntfs三种文件系统的卷设备挂载。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600002 |
| 13600003 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.mount(volumeId).then(() => {
  // 挂载指定卷设备成功后的回调
}).catch((error: BusinessError) => {
  console.error(`Failed to mount. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.mount(volumeId).then(() => {
  // 挂载指定卷设备成功后的回调
}).catch((error: BusinessError): void => {
  console.error(`Failed to mount. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.mount(volumeId, (error: BusinessError) => {
  if (error) {
    console.error(`mount failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 挂载指定卷设备成功后的回调
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.mount(volumeId, (error: BusinessError | null) => {
  if (error) {
    console.error(`mount failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 挂载指定卷设备成功后的回调
});
```


## mount

```TypeScript
function mount(volumeId: string): Promise<void>
```

挂载指定卷设备，使用Promise异步回调。当前仅支持vfat、exfat以及ntfs三种文件系统的卷设备挂载。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MOUNT_UNMOUNT_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volumeId | string | 是 |

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
| 13600003 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

参见 [mount](#mount)
