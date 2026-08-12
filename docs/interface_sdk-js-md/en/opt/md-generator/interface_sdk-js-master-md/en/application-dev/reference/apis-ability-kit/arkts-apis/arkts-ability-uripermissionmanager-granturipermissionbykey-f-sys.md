# grantUriPermissionByKey (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';
```

## grantUriPermissionByKey

```TypeScript
function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: number): Promise<void>
```

Grants the URI access permission of the current application to the target application through the unique key of the  Unified Data Management Framework (UDMF) data. The permission will be revoked after the target application exits.This API uses a promise to return the result.This API can be properly called only on phones, 2-in-1 devices, and tablets. If it is called on other device types, error code 801 is returned.  
**System API**: This is a system API.

**Since:** 20

<!--Device-uriPermissionManager-function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermissionByKey(key: string, flag: wantConstant.Flags, targetTokenId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| flag | wantConstant.Flags | Yes |
| targetTokenId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000060](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000060-sandbox-applications-cannot-grant-uri-permission) |
| [16000092](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000092-no-permission-to-authorize-uri) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000094](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000094-invalid-target-token-id) |
| [16000058](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000058-specified-uri-flag-is-invalid) |
| [16000091](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000091-failed-to-obtain-a-file-uri-by-key) |

## Examples

```TypeScript
// The bundle name of the API caller is com.example.test.
// ExntryAbility.ets
import { AbilityConstant, UIAbility, Want, wantConstant, uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    try {
      // You can generate a key using unifiedDataChannel.insertData.
      let key: string = 'udmf://SystemShare/com.example.test/ap\\t5kKMYTOSHBh9\\f1@817VnBBvxI[e';
      // You can obtain targetTokenId by calling bundleManager.getApplicationInfo.
      // Assume that the obtained targetTokenId is 1001.
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
