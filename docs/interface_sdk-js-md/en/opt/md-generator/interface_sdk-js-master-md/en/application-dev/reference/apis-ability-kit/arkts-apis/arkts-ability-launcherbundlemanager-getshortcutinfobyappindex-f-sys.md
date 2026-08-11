# getShortcutInfoByAppIndex (System API)

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## getShortcutInfoByAppIndex

```TypeScript
function getShortcutInfoByAppIndex(bundleName: string, appIndex: number): Array<ShortcutInfo>
```

Obtains the [shortcut information](arkts-ability-launcherbundlemanager-shortcutinfo-t.md) of the current user based on the index of an application clone.

No permission is required for obtaining the caller's own information.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-launcherBundleManager-function getShortcutInfoByAppIndex(bundleName: string, appIndex: int): Array<ShortcutInfo>--><!--Device-launcherBundleManager-function getShortcutInfoByAppIndex(bundleName: string, appIndex: int): Array<ShortcutInfo>-End-->

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
| Array&lt;ShortcutInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getShortcutInfoByAppIndex("com.example.demo", 1);
  console.info('getShortcutInfoByAppIndex successfully, data is ' + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`Failed to getShortcutInfoByAppIndex. Code: ${code}, message: ${message}`);
}
```
