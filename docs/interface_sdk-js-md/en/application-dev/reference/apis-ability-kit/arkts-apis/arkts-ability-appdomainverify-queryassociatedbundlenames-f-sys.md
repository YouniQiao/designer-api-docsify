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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [29900001](../errorcode-appDomainVerify-sys.md#29900001-internal-system-service-error) |
