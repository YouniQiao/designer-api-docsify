# offSystemBarTintChange (System API)

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## offSystemBarTintChange

```TypeScript
function offSystemBarTintChange(callback?: Callback<SystemBarTintState>): void
```

Unsubscribes from the property change event of the status bar and navigation bar.

**Since:** 23

**Deprecated since:** -1

<!--Device-window-function offSystemBarTintChange(callback?: Callback<SystemBarTintState>): void--><!--Device-window-function offSystemBarTintChange(callback?: Callback<SystemBarTintState>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
