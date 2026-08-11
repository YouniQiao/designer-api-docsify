# BundleStatusCallback (System API)

> **NOTE：**
> 
> The initial APIs of this module are supported since API version 8. Newly added APIs will
> be marked with a superscript to indicate their earliest API version.
> 
> The APIs of this module have been deprecated since API version 9. No substitute is provided.
> 
> The APIs provided by this module are system APIs.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor/bundleMonitor

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-unnamed-export interface BundleStatusCallback--><!--Device-unnamed-export interface BundleStatusCallback-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## add

```TypeScript
add: (bundleName: string, userId: number) => void
```

Used to obtain information when a bundle is installed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor/bundleMonitor.BundleChangedInfo

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-BundleStatusCallback-add: (bundleName: string, userId: number) => void--><!--Device-BundleStatusCallback-add: (bundleName: string, userId: number) => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |

## remove

```TypeScript
remove: (bundleName: string, userId: number) => void
```

Used to obtain information when a bundle is uninstalled.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor/bundleMonitor.BundleChangedInfo

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-BundleStatusCallback-remove: (bundleName: string, userId: number) => void--><!--Device-BundleStatusCallback-remove: (bundleName: string, userId: number) => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |

## update

```TypeScript
update: (bundleName: string, userId: number) => void
```

Used to obtain information when a bundle is updated.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor/bundleMonitor.BundleChangedInfo

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-BundleStatusCallback-update: (bundleName: string, userId: number) => void--><!--Device-BundleStatusCallback-update: (bundleName: string, userId: number) => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |
