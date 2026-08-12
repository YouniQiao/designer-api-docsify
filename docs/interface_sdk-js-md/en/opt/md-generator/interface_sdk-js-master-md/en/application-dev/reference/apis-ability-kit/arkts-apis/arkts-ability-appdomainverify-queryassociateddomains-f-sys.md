# queryAssociatedDomains (System API)

## Modules to Import

```TypeScript
import { appDomainVerify } from '@kit.AbilityKit';
```

## queryAssociatedDomains

```TypeScript
function queryAssociatedDomains(bundleName: string): string[]
```

query domains verify associated with bundleName.

**Since:** 13

**Required permissions:** ohos.permission.GET_APP_DOMAIN_BUNDLE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-appDomainVerify-function queryAssociatedDomains(bundleName: string): string[]--><!--Device-appDomainVerify-function queryAssociatedDomains(bundleName: string): string[]-End-->

**System capability:** SystemCapability.BundleManager.AppDomainVerify

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [29900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-appDomainVerify-sys.md#29900001-internal-system-service-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appDomainVerify } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Obtain the list of domain names associated with the bundle name "com.example.app1".
let bundleName = "com.example.app1";
let domains = appDomainVerify.queryAssociatedDomains(bundleName);
domains.forEach(domain => {
  hilog.info(0x0000, 'testTag', `app:${bundleName} associate with domain:${domain}`);
});
```
