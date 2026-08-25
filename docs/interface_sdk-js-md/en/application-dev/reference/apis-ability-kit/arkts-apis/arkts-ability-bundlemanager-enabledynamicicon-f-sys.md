# enableDynamicIcon (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## enableDynamicIcon

```TypeScript
function enableDynamicIcon(bundleName: string, moduleName: string): Promise<void>
```

Enables the dynamic icon based on the given bundle name and module name. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_DYNAMIC_ICON

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700304](../errorcode-bundle.md#17700304-failed-to-enable-the-dynamic-icon) |
| [17700307](../errorcode-bundle.md#17700307-dynamic-icon-does-not-take-effect-because-of-a-custom-theme) |


## enableDynamicIcon

```TypeScript
function enableDynamicIcon(bundleName: string, moduleName: string, option?: BundleOptions): Promise<void>
```

Enables the dynamic icon based on the given bundle name, module name, and bundle options. This API uses a promise to return the result.To enable the dynamic icon for the current user, you must request the ohos.permission.ACCESS_DYNAMIC_ICON permission.To enable the dynamic icon for another user, you must request the ohos.permission.ACCESS_DYNAMIC_ICON and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permissions.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_DYNAMIC_ICON or (ohos.permission.ACCESS_DYNAMIC_ICON and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| option | [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700304](../errorcode-bundle.md#17700304-failed-to-enable-the-dynamic-icon) |
| [17700307](../errorcode-bundle.md#17700307-dynamic-icon-does-not-take-effect-because-of-a-custom-theme) |
