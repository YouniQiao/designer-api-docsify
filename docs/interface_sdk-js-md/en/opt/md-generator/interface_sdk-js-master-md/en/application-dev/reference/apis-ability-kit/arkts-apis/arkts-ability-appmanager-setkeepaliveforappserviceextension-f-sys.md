# setKeepAliveForAppServiceExtension (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## setKeepAliveForAppServiceExtension

```TypeScript
function setKeepAliveForAppServiceExtension(bundleName: string, enabled: boolean): Promise<void>
```

Sets or cancels the keep-alive status for an AppServiceExtensionAbility. This API uses a promise to return the result.This API can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code 801 is returned.

> **NOTE：**
> 
> - This API takes effect only when the application is installed under the user with **userId** of 1 and the
> **mainElement** field in the **module.json5** file of the entry HAP is set to **AppServiceExtensionAbility**.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

<!--Device-appManager-function setKeepAliveForAppServiceExtension(bundleName: string, enabled: boolean): Promise<void>--><!--Device-appManager-function setKeepAliveForAppServiceExtension(bundleName: string, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000081](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000081-failed-to-obtain-the-target-application-information) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000204-application-is-not-installed-for-the-user-with-userid-of-1) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000202-keepalive-can-be-set-only-for-an-extensionability-of-the-appservice-type) |
| [16000203](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000203-cannot-change-the-keepalive-status-of-an-appserviceextensionability) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.keepaliveapp";
  appManager.setKeepAliveForAppServiceExtension(bundleName, true).then(() => {
    console.info(`setKeepAliveForAppServiceExtension success`);
  }).catch((err: BusinessError) => {
    console.error(`setKeepAliveForAppServiceExtension fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] setKeepAliveForAppServiceExtension error: ${code}, ${message}`);
}
```
