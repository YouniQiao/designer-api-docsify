# offChange (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
import { screenshot } from '@kit.ArkUI';
```

## offChange

```TypeScript
function offChange(callback?: Callback<long>): void
```

Unregister the callback for screen changes.

**Since:** 23

<!--Device-screen-function offChange(callback?: Callback<long>): void--><!--Device-screen-function offChange(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

