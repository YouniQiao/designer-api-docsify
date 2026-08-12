# getAllDesktopShortcutInfo

## Modules to Import

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
```

## getAllDesktopShortcutInfo

```TypeScript
function getAllDesktopShortcutInfo(userId: number): Promise<Array<ShortcutInfo>>
```

Obtains the information about all shortcuts of the given user.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_SHORTCUTS

<!--Device-shortcutManager-function getAllDesktopShortcutInfo(userId: int): Promise<Array<ShortcutInfo>>--><!--Device-shortcutManager-function getAllDesktopShortcutInfo(userId: int): Promise<Array<ShortcutInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ShortcutInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700004-user-id-does-not-exist) |
