# getAbilityIcon

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## getAbilityIcon

```TypeScript
function getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void
```

Obtains the [PixelMap](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md#@ohos.multimedia.image) of the icon corresponding to a given bundle name and ability name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void--><!--Device-bundle-function getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| abilityName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |


## getAbilityIcon

```TypeScript
function getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>
```

Obtains the [PixelMap](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md#@ohos.multimedia.image) of the icon corresponding to a given bundle name and ability name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>--><!--Device-bundle-function getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| abilityName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |
