# grantUriPermissionByKey（系统接口）

## 导入模块

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermissionByKey

```TypeScript
function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: int): Promise<void>
```

通过UDMF数据唯一标识key，将当前应用的文件URI访问权限授权给目标应用，权限将在目标应用退出后回收。使用Promise异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。  
**系统接口**：此接口为系统接口。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-uriPermissionManager-function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 目标UDMF数据唯一标识。key必须由调用方通过 [unifiedDataChannel.insertData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-insertdata-f.md/arkts-arkdata-unifieddatachannel-insertdata-f.md#insertdata) 创建，且写入的数据均为有权限授权的文件URI。&lt;br&gt;当前仅支持SYSTEM_SHARE、PICKER和MENU类型的 [UDMF数据通路](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-intention-e.md/arkts-arkdata-unifieddatachannel-intention-e.md)的key。key的创建与使用方法详见 [标准化数据通路实现数据共享](../../../database/unified-data-channels.md)。 |
| flag | wantConstant.Flags | 是 | URI的读权限或写权限。支持的取值如下：&lt;br&gt;- FLAG_AUTH_READ_URI_PERMISSION：读权限。&lt;br&gt;- FLAG_AUTH_WRITE_URI_PERMISSION：写权限。 |
| targetTokenId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标应用的身份标识，可以通过 [bundleManager.getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getapplicationinfo) 获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 16000092 | No permission to authorize the URI. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000094 | The target token ID is invalid. |
| 16000058 | Invalid URI flag. |
| 16000091 | Failed to get the file URI from the key. |

## 示例

```TypeScript
// 接口调用方应用包名为com.example.test
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want, wantConstant, uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    try {
      // 可以通过unifiedDataChannel.insertData生成key
      let key: string = 'udmf://SystemShare/com.example.test/ap\\t5kKMYTOSHBh9\\f1@817VnBBvxI[e';
      // 可以通过bundleManager.getApplicationInfo接口获取targetTokenId
      // 假设获取的targetTokenId为1001
      let targetTokenId: number = 1001;
      uriPermissionManager.grantUriPermissionByKey(key,
        wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetTokenId)
        .then(() => {
          console.info('grantUriPermissionByKey succeeded.');
        }).catch((error: BusinessError) => {
        console.error('grantUriPermissionByKey failed: ' + JSON.stringify(error));
      });
    } catch (error) {
      console.error('grantUriPermissionByKey failed: ' + JSON.stringify(error));
    }
  }
}
```

