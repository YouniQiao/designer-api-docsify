# getAllLauncherAbilityInfos (System API)

## Modules to Import

```TypeScript
import { BundleStatusCallback } from '@kit.AbilityKit';
```

## getAllLauncherAbilityInfos

```TypeScript
function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void
```

Obtains the information about all launcher abilities. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API)) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API))(userId: int, callback: AsyncCallback&lt;Array&lt;LauncherAbilityInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void--><!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-launcherabilityinfo-depr-i-sys.md)&gt;&gt; | Yes |


## getAllLauncherAbilityInfos

```TypeScript
function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>
```

Obtains the information about all launcher abilities. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API)) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API))(userId: int, callback: AsyncCallback&lt;Array&lt;LauncherAbilityInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>--><!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-launcherabilityinfo-depr-i-sys.md)&gt;&gt; |
