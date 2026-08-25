# startShortcutWithReason (System API)

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## startShortcutWithReason

```TypeScript
function startShortcutWithReason(shortcutInfo: ShortcutInfo, startReason: string, options?: StartOptions): Promise<void>
```

Starts an ability based on the specified shortcut information, and carries the reason for the shortcut launch. This API uses a promise to return the result.The launched ability can obtain the launch reason through the **launchReasonMessage** field of [LaunchParam](arkts-ability-abilityconstant-launchparam-i.md) and handle service logic accordingly.

**Since:** 20

**Required permissions:** ohos.permission.START_SHORTCUT and ohos.permission.SET_LAUNCH_REASON_MESSAGE

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shortcutInfo | [ShortcutInfo](arkts-ability-shortcutinfo-i.md) | Yes |
| startReason | string | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700065](../errorcode-bundle.md#17700065-ability-specified-by-want-in-the-shortcutinfo-struct-cannot-be-started) |
