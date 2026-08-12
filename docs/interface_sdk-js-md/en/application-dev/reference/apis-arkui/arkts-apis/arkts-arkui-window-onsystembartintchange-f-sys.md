# onSystemBarTintChange (System API)

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## onSystemBarTintChange

```TypeScript
function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void
```

Subscribes to the property change event of the status bar and navigation bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-window-function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void--><!--Device-window-function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md)&gt; | Yes | Callback used to return the properties of the system bar. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

