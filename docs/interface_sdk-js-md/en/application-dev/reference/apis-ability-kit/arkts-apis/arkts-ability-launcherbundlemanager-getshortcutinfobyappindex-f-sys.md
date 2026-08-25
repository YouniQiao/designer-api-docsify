# getShortcutInfoByAppIndex (System API)

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## getShortcutInfoByAppIndex

```TypeScript
function getShortcutInfoByAppIndex(bundleName: string, appIndex: number): Array<ShortcutInfo>
```

Obtains the shortcut information of the current user based on the index of an application clone.No permission is required for obtaining the caller's own information.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;ShortcutInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
