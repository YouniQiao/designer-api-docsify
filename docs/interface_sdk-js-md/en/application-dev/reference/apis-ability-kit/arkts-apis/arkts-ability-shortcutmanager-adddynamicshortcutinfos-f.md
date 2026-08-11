# addDynamicShortcutInfos

## Modules to Import

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## addDynamicShortcutInfos

```TypeScript
function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: int): Promise<void>
```

Adds dynamic shortcuts for the given user.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MANAGE_SHORTCUTS or (ohos.permission.MANAGE_SHORTCUTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

<!--Device-shortcutManager-function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: int): Promise<void>--><!--Device-shortcutManager-function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shortcutInfo | Array&lt;ShortcutInfo&gt; | Yes | Information about the dynamic shortcuts. When the shortcut information is submitted through this API, the following validations are performed:&lt;br&gt; 1. The **sourceType** field in **ShortcutInfo** is set to **2**.&lt;br&gt; 2. If the **moduleName** field in **ShortcutInfo** does not exist in the corresponding application, error code 17700002 is thrown.&lt;br&gt; 3. If the **hostAbility** field in **ShortcutInfo** is set to a non-empty string, the system checks whether the corresponding ability exists. If it does not exist, error code 17700003 is thrown. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the user to which the dynamic shortcuts belong. The user ID can be obtained by calling [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) . The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) | The specified app index is invalid. |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) | The specified bundle is disabled. |
| [18100001](../errorcode-bundle.md#18100001-inconsistent-bundlename-and-appindex-combinations-in-the-shortcutinfo-list) | A combination of bundleName and appIndex in the shutcutInfo list is different from the others. |
| [17700070](../errorcode-bundle.md#17700070-invalid-shortcut-id) | The specified shortcut id is illegal. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. A non-system application is not allowed to call a system API. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user id is not found. |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) | The specified module is not found. |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) | The specified ability is not found. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle is not found. |

## Examples

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use the actual shortcut ID, bundle name, module name, and user ID.
const bundleName = "com.example.dynamic";
let moduleName = 'entry';
const arrShortcutInfo: Array<shortcutManager.ShortcutInfo> = [
  {
    id: "1",
    bundleName: bundleName,
    moduleName: moduleName,
    appIndex: 0,
    sourceType: 2
  },
  {
    id: "2",
    bundleName: bundleName,
    moduleName: moduleName,
    appIndex: 0,
    sourceType: 2
  }
]

try {
  shortcutManager.addDynamicShortcutInfos(arrShortcutInfo, 100)
    .then(() => {
      console.info('addDynamicShortcutInfos success');
    }).catch((err: Error) => {
    console.error(`addDynamicShortcutInfos errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
  });
} catch (err) {
  console.error(`addDynamicShortcutInfos errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
}
```

