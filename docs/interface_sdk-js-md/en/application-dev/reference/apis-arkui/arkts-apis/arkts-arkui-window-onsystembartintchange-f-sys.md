# onSystemBarTintChange (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
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
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;SystemBarTintState&gt; | Yes | Callback used to return the properties of the system bar. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

