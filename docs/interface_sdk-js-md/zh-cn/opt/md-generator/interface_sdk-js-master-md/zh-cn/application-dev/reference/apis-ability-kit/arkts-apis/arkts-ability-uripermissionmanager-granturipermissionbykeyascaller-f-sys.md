# grantUriPermissionByKeyAsCaller（系统接口）

## grantUriPermissionByKeyAsCaller

```TypeScript
function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: number, targetTokenId: number): Promise<void>
```

通过UDMF数据唯一标识key，将指定应用的文件URI访问权限授权给目标应用，权限将在目标应用退出后回收。使用Promise异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。  
**系统接口**：此接口为系统接口。

**起始版本：** 20

**需要权限：** ohos.permission.GRANT_URI_PERMISSION_AS_CALLER

<!--Device-uriPermissionManager-function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: int, targetTokenId: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: int, targetTokenId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| flag | wantConstant.Flags | 是 |
| callerTokenId | number | 是 |
| targetTokenId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000060](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [16000092](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000092-无权限授权uri) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16000093](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000093-调用方的token-id无效) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [16000094](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000094-目标应用的token-id无效) |
| [16000058](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000091](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000091-根据key获取文件uri数据失败) |

## 示例

```TypeScript
// 拉起方应用包名为com.example.caller
// Index.ets
import { common, Want, wantConstant } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)

        Button('分享文件')
          .onClick(() => {
            // key可以通过unifiedDataChannel.insertData生成
            let udKey: string = 'udmf://SystemShare/com.example.caller/ap\\t5kKMYTOSHBh9\\f1@817VnBBvxI[e';
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let want: Want = {
              bundleName: 'com.example.test',
              abilityName: 'EntryAbility',
              parameters: {
                [wantConstant.Params.ABILITY_UNIFIED_DATA_KEY]: udKey
              }
            };
            context.startAbility(want);
          })
      }
    }
  }
}
```

```TypeScript
// 接口调用方应用包名为com.example.test
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want, wantConstant, uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let udKey: string = want.parameters?.[wantConstant.Params.ABILITY_UNIFIED_DATA_KEY] as string;
    let callerTokenId: number = want.parameters?.['ohos.aafwk.param.callerToken'] as number;
    AppStorage.setOrCreate('udKey', udKey);
    AppStorage.setOrCreate('callerTokenId', callerTokenId);
  }

  onForeground(): void {
    try {
      let udKey: string = AppStorage.get<string>('udKey') as string;
      let callerTokenId: number = AppStorage.get<number>('callerTokenId') as number;
      // 可以通过bundleManager.getApplicationInfo接口获取targetTokenId
      // 假设获取的targetTokenId为1001
      let targetTokenId: number = 1001;

      uriPermissionManager.grantUriPermissionByKeyAsCaller(udKey,
        wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, callerTokenId, targetTokenId)
        .then(() => {
          console.info('grantUriPermissionByKeyAsCaller succeeded.');
        }).catch((error: BusinessError) => {
        console.error('grantUriPermissionByKeyAsCaller failed: ' + JSON.stringify(error));
      });
    } catch (error) {
      console.error('grantUriPermissionByKeyAsCaller failed: ' + JSON.stringify(error));
    }
  }
}
```
