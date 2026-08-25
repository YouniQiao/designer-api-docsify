# setShortcutVisibleForSelf

## Modules to Import

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## setShortcutVisibleForSelf

```TypeScript
function setShortcutVisibleForSelf(id: string, visible: boolean): Promise<void>
```

Sets whether to display the specified shortcut for the current application. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| visible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17700070](../errorcode-bundle.md#17700070-invalid-shortcut-id) |
