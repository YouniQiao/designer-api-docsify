# addDesktopShortcutInfo (System API)

## Modules to Import

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
```

## addDesktopShortcutInfo

```TypeScript
function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: number): Promise<void>
```

Adds a shortcut for the given user. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_SHORTCUTS

<!--Device-shortcutManager-function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: int): Promise<void>--><!--Device-shortcutManager-function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shortcutInfo | [ShortcutInfo](arkts-ability-shortcutinfo-i.md) | Yes |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) |
| [17700070](../errorcode-bundle.md#17700070-invalid-shortcut-id) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
