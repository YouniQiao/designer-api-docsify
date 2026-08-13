# getShortcutInfoByAbility (System API)

## Modules to Import

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
```

## getShortcutInfoByAbility

```TypeScript
function getShortcutInfoByAbility(bundleName: string, moduleName: string, abilityName: string, userId?: number, appIndex?: number): Array<ShortcutInfo>
```

Obtains shortcut info by bundleName, moduleName, abilityName, userId and appIndex. If you need to obtains shortcut info under the current user, ohos.permission.GET_BUNDLE_INFO_PRIVILEGED needs to be applied for. If you need to obtains shortcut info under other users, ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS need to be applied for.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**Model restriction:** This API can be used only in the stage model.

<!--Device-shortcutManager-function getShortcutInfoByAbility(bundleName: string, moduleName: string, abilityName: string, userId?: int, appIndex?: int): Array<ShortcutInfo>--><!--Device-shortcutManager-function getShortcutInfoByAbility(bundleName: string, moduleName: string, abilityName: string, userId?: int, appIndex?: int): Array<ShortcutInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| abilityName | string | Yes |
| userId | number | No |
| appIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;ShortcutInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
