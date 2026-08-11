# setShortcutsEnabled

## Modules to Import

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## setShortcutsEnabled

```TypeScript
function setShortcutsEnabled(shortcutsInfo: Array<ShortcutInfo>, isEnabled: boolean): Promise<void>
```

Enables or disables the specified static shortcuts. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_SHORTCUTS

<!--Device-shortcutManager-function setShortcutsEnabled(shortcutsInfo: Array<ShortcutInfo>, isEnabled: boolean): Promise<void>--><!--Device-shortcutManager-function setShortcutsEnabled(shortcutsInfo: Array<ShortcutInfo>, isEnabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shortcutsInfo | Array&lt;ShortcutInfo&gt; | Yes |
| isEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17700070](../errorcode-bundle.md#17700070-invalid-shortcut-id) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use the actual shortcut ID and bundle name.
const bundleName = "com.example.myapplication";
const arrShortcutInfo: Array<shortcutManager.ShortcutInfo> = [
  {
    id: "1",
    bundleName: bundleName,
    appIndex: 0,
    sourceType: 1
  },
  {
    id: "2",
    bundleName: bundleName,
    appIndex: 0,
    sourceType: 1
  }
]

try {
  shortcutManager.setShortcutsEnabled(arrShortcutInfo, false)
    .then(() => {
      console.info('setShortcutsEnabled success');
    }).catch((err: Error) => {
    console.error(`setShortcutsEnabled errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
  });
} catch (err) {
  console.error(`setShortcutsEnabled errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
}
```
