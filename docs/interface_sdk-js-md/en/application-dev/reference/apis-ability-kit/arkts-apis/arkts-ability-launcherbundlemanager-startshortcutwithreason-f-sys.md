# startShortcutWithReason (System API)

## Modules to Import

```TypeScript
import { launcherBundleManager } from 'launcherBundleManager';
```

## startShortcutWithReason

```TypeScript
function startShortcutWithReason(shortcutInfo: ShortcutInfo, startReason: string, options?: StartOptions): Promise<void>
```

Starts an ability based on the specified shortcut information, and carries the reason for the shortcut launch. This API uses a promise to return the result. The launched ability can obtain the launch reason through the **launchReasonMessage** field of [LaunchParam](arkts-ability-abilityconstant-launchparam-i.md#launchparam) and handle service logic accordingly.

**Since:** 23

**Required permissions:** ohos.permission.START_SHORTCUT and ohos.permission.SET_LAUNCH_REASON_MESSAGE

<!--Device-launcherBundleManager-function startShortcutWithReason(shortcutInfo: ShortcutInfo, startReason: string, options?: StartOptions): Promise<void>--><!--Device-launcherBundleManager-function startShortcutWithReason(shortcutInfo: ShortcutInfo, startReason: string, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shortcutInfo | ShortcutInfo | Yes | Shortcut information of the application. |
| startReason | string | Yes | Reason for launching the shortcut. The value can be [AbilityConstant.REASON_MESSAGE_DESKTOP_SHORTCUT](arkts-app-ability-abilityconstant.md#constants) , indicating a home screen shortcut launch. |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No | Parameters used to specify the window mode of the target ability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not support. |
| [201](../../errorcode-universal.md#201-permission-denied) | Verify permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700065](../errorcode-bundle.md#17700065-ability-specified-by-want-in-the-shortcutinfo-struct-cannot-be-started) | The specified shortcut want in shortcut info is not supported to be started. |

**Examples**

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant } from '@kit.AbilityKit';

try {
  let data: Array<launcherBundleManager.ShortcutInfo> =
    launcherBundleManager.getShortcutInfoSync("com.example.myapplication");
  console.info('startShortcutWithReason data is ' + JSON.stringify(data));
  let startReason = AbilityConstant.REASON_MESSAGE_DESKTOP_SHORTCUT;
  if (data) {
    try {
      launcherBundleManager.startShortcutWithReason(data[0], startReason)
        .then(() => {
          console.info('startShortcutWithReason success');
        }).catch((err: BusinessError) => {
        console.error(`startShortcutWithReason errData is errCode:${err.code}  message:${err.message}`);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`startShortcutWithReason error is errCode:${code}  message:${message}`);
    }
  }
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`startShortcutWithReason errData is errCode:${code}  message:${message}`);
}
```

