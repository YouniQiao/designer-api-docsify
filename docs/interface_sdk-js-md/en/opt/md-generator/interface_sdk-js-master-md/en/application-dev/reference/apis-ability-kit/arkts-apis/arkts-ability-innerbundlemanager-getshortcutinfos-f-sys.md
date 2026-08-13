# getShortcutInfos (System API)

## Modules to Import

```TypeScript
import { BundleStatusCallback } from '@kit.AbilityKit';
```

## getShortcutInfos

```TypeScript
function getShortcutInfos(bundleName: string, callback: AsyncCallback<Array<ShortcutInfo>>): void
```

Obtains an array of the shortcut information based on a given bundle name. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API)) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API))(bundleName :string, callback: AsyncCallback&lt;Array&lt;ShortcutInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getShortcutInfos(bundleName: string, callback: AsyncCallback<Array<ShortcutInfo>>): void--><!--Device-innerBundleManager-function getShortcutInfos(bundleName: string, callback: AsyncCallback<Array<ShortcutInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ShortcutInfo](arkts-ability-shortcutinfo-shortcutinfo-depr-i.md)&gt;&gt; | Yes |


## getShortcutInfos

```TypeScript
function getShortcutInfos(bundleName: string): Promise<Array<ShortcutInfo>>
```

Obtains an array of the shortcut information based on a given bundle name. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API)) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API))(bundleName :string, callback: AsyncCallback&lt;Array&lt;ShortcutInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getShortcutInfos(bundleName: string): Promise<Array<ShortcutInfo>>--><!--Device-innerBundleManager-function getShortcutInfos(bundleName: string): Promise<Array<ShortcutInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ShortcutInfo](arkts-ability-shortcutinfo-shortcutinfo-depr-i.md)&gt;&gt; |
