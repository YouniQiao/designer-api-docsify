# queryAssociatedDomains (System API)

## Modules to Import

```TypeScript
```

## queryAssociatedDomains

```TypeScript
function queryAssociatedDomains(bundleName: string): string[]
```

query domains verify associated with bundleName.

**Since:** 23

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [29900001](../errorcode-appDomainVerify-sys.md#29900001-internal-system-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

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
