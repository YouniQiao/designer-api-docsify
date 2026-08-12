# setApplicationEnabled (System API)

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## setApplicationEnabled

```TypeScript
function setApplicationEnabled(bundleName: string, isEnable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable an application. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [null](null)

**Required permissions:** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setApplicationEnabled(bundleName: string, isEnable: boolean, callback: AsyncCallback<void>): void--><!--Device-bundle-function setApplicationEnabled(bundleName: string, isEnable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| isEnable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## setApplicationEnabled

```TypeScript
function setApplicationEnabled(bundleName: string, isEnable: boolean): Promise<void>
```

Sets whether to enable an application. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [null](null)

**Required permissions:** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setApplicationEnabled(bundleName: string, isEnable: boolean): Promise<void>--><!--Device-bundle-function setApplicationEnabled(bundleName: string, isEnable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| isEnable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
