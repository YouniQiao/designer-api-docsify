# setKeepAliveForBundle (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## setKeepAliveForBundle

```TypeScript
function setKeepAliveForBundle(bundleName: string, userId: number, enable: boolean): Promise<void>
```

Sets or cancels the keep-alive status for an application that belongs to a specified user. This API uses a promise to return the result.Starting from API version 18, this API can be properly called only on 2-in-1 devices and wearables. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

> **NOTE：**
> 
> - To support keep-alive, **mainElement** in the
> [module.json5](../../../quick-start/module-configuration-file.md) file of the application must be a UIAbility.
> The system initiates the keep-alive operation only when this mainElement has been launched.
> 
> - On 2-in-1 devices, the application must appear in the status bar within 5 seconds of launch. Otherwise, the
> system revokes the application's keep-alive status and terminate the restarted process.
> 
> - When the kept-alive application process exits, the system attempts to restart it. If three consecutive restart
> attempts fail, the system stops restarting the process.

**Since:** 14

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

<!--Device-appManager-function setKeepAliveForBundle(bundleName: string, userId: int, enable: boolean): Promise<void>--><!--Device-appManager-function setKeepAliveForBundle(bundleName: string, userId: int, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16300008-specified-package-does-not-have-a-main-uiability) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16300009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16300009-specified-package-does-not-have-a-status-bar) |
| [16300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16300010-running-application-is-not-attached-to-a-status-bar) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16300005-bundle-information-does-not-exist) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.keepaliveapp";
  let userId = 100;
  appManager.setKeepAliveForBundle(bundleName, userId, true).then(() => {
    console.info(`setKeepAliveForBundle success`);
  }).catch((err: BusinessError) => {
    console.error(`setKeepAliveForBundle fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] setKeepAliveForBundle error: ${code}, ${message}`);
}
```
