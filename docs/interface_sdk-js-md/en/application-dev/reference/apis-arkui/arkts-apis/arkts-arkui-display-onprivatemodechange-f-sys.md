# onPrivateModeChange (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onPrivateModeChange

```TypeScript
function onPrivateModeChange(callback: Callback<boolean>): void
```

Register the callback for private mode changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function onPrivateModeChange(callback: Callback<boolean>): void--><!--Device-display-function onPrivateModeChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result whether display is on private mode or not |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

