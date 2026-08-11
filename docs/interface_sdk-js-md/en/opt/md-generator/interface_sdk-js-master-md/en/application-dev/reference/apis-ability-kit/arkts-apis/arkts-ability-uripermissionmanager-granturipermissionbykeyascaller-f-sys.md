# grantUriPermissionByKeyAsCaller (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermissionByKeyAsCaller

```TypeScript
function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: number, targetTokenId: number): Promise<void>
```

Grants the URI access permission of the specified application to the target application through the unique key of the Unified Data Management Framework (UDMF) data. The permission will be revoked after the target application exits. This API uses a promise to return the result.This API can be properly called only on phones, 2-in-1 devices, and tablets. If it is called on other device types, error code 801 is returned.  
**System API**: This is a system API.

**Since:** 20

**Required permissions:** ohos.permission.GRANT_URI_PERMISSION_AS_CALLER

<!--Device-uriPermissionManager-function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: int, targetTokenId: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: int, targetTokenId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| flag | wantConstant.Flags | Yes |
| callerTokenId | number | Yes |
| targetTokenId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000060](../errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [16000092](../errorcode-ability.md#16000092-no-permission-to-authorize-uri) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000093](../errorcode-ability.md#16000093-invalid-caller-token-id) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000094](../errorcode-ability.md#16000094-invalid-target-token-id) |
| [16000058](../errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000091](../errorcode-ability.md#16000091-failed-to-obtain-a-file-uri-by-key) |

## Examples

```TypeScript
// The bundle name of the caller application is com.example.caller.
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

        Button('Share File')
          .onClick(() => {
            // You can generate a key using unifiedDataChannel.insertData.
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
// The bundle name of the API caller is com.example.test.
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
      // You can obtain targetTokenId by calling bundleManager.getApplicationInfo.
      // Assume that the obtained targetTokenId is 1001.
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
