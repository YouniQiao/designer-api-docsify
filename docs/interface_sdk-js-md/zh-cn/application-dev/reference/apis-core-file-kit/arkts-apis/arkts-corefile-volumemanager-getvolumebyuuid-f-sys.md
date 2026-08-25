# getVolumeByUuid（系统接口）

## 导入模块

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getVolumeByUuid

```TypeScript
function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void
```

通过卷设备uuid获得指定卷设备信息，使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; | 是 |

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

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
volumeManager.getVolumeByUuid(uuid).then((volume: volumeManager.Volume) => {
  console.info("getVolumeByUuid successfully:" + JSON.stringify(volume));
}).catch((error: BusinessError) => {
  console.error(`Failed to getVolumeByUuid. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
volumeManager.getVolumeByUuid(uuid).then((volume: volumeManager.Volume) => {
  console.info("getVolumeByUuid successfully:" + JSON.stringify(volume));
}).catch((error: BusinessError): void => {
  console.error(`Failed to getVolumeByUuid. Code: ${error.code}, message: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
volumeManager.getVolumeByUuid(uuid, (error: BusinessError, volume: volumeManager.Volume) => {
  if (error) {
    console.error(`getVolumeByUuid failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 获取到卷设备信息
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// uuid可通过getAllVolumes()接口获取卷设备信息后获得
let uuid: string = "";
volumeManager.getVolumeByUuid(uuid, (error: BusinessError | null, volume: volumeManager.Volume | undefined) => {
  if (error) {
    console.error(`getVolumeByUuid failed, code is: ${error.code}, message is: ${error.message}`);
    return;
  }
  // 获取到卷设备信息
});
```


## getVolumeByUuid

```TypeScript
function getVolumeByUuid(uuid: string): Promise<Volume>
```

通过卷设备uuid获得指定卷设备信息，使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; |

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

参见 [getVolumeByUuid](#getvolumebyuuid)
