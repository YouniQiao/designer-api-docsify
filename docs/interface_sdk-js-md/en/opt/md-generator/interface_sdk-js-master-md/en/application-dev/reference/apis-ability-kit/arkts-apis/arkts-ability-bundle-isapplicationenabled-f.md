# isApplicationEnabled

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## isApplicationEnabled

```TypeScript
function isApplicationEnabled(bundleName: string, callback: AsyncCallback<boolean>): void
```

Checks whether an application is enabled based on a given bundle name. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

<!--Device-bundle-function isApplicationEnabled(bundleName: string, callback: AsyncCallback<boolean>): void--><!--Device-bundle-function isApplicationEnabled(bundleName: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isApplicationEnabled

```TypeScript
function isApplicationEnabled(bundleName: string): Promise<boolean>
```

Checks whether an application is enabled based on a given bundle name. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

<!--Device-bundle-function isApplicationEnabled(bundleName: string): Promise<boolean>--><!--Device-bundle-function isApplicationEnabled(bundleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
