# unmount（系统接口）

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## unmount

```TypeScript
function unmount(volumeId: string, callback: AsyncCallback<void>): void
```

卸载指定卷设备，使用callback异步回调。

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
| 13600004 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.unmount(volumeId).then(() => {
  // 卸载指定卷设备成功后的回调
}).catch((error: BusinessError) => {
  console.error(`Failed to unmount. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.unmount(volumeId).then(() => {
  // 卸载指定卷设备成功后的回调
}).catch((error: BusinessError): void => {
  console.error(`Failed to unmount. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.unmount(volumeId, (error: BusinessError) => {
  if (error) {
    console.error(`unmount failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 卸载指定卷设备成功后的回调
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// volumeId可通过getAllVolumes()接口获取
let volumeId: string = "";
volumeManager.unmount(volumeId, (error: BusinessError | null) => {
  if (error) {
    console.error(`unmount failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 卸载指定卷设备成功后的回调
});
```


## unmount

```TypeScript
function unmount(volumeId: string): Promise<void>
```

卸载指定卷设备，使用Promise异步回调。

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
| 13600004 |
| 13600005 |
| 13600008 |
| 13900042 |

**示例**

参见 [unmount](#unmount)
