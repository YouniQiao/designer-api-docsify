# getLaunchWantForBundle

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getLaunchWantForBundle

```TypeScript
function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void
```

Obtains the Want object that launches the specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void--><!--Device-bundle-function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Yes |


## getLaunchWantForBundle

```TypeScript
function getLaunchWantForBundle(bundleName: string): Promise<Want>
```

Obtains the Want object that launches the specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getLaunchWantForBundle(bundleName: string): Promise<Want>--><!--Device-bundle-function getLaunchWantForBundle(bundleName: string): Promise<Want>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; |
