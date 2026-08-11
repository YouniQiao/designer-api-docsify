# queryAssociatedBundleNames (System API)

## Modules to Import

```TypeScript
import { appDomainVerify } from 'kits/@kit.AbilityKit';
```

## queryAssociatedBundleNames

```TypeScript
function queryAssociatedBundleNames(domain: string): string[]
```

query bundleNames associated with domain.

**Since:** 13

**Required permissions:** ohos.permission.GET_APP_DOMAIN_BUNDLE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-appDomainVerify-function queryAssociatedBundleNames(domain: string): string[]--><!--Device-appDomainVerify-function queryAssociatedBundleNames(domain: string): string[]-End-->

**System capability:** SystemCapability.BundleManager.AppDomainVerify

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [29900001](../errorcode-appDomainVerify-sys.md#29900001-internal-system-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appDomainVerify } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Obtain the list of bundle names associated with the domain name "example.com".
let domain = "example.com";
let bundleNames = appDomainVerify.queryAssociatedBundleNames(domain);
bundleNames.forEach(bundleName => {
  hilog.info(0x0000, 'testTag', `domain:${domain} associate with app:${bundleName}`);
});
```
