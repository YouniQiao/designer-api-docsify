# offPrivateModeChange (System API)

## Modules to Import

```TypeScript
import { display } from 'display';
```

## offPrivateModeChange

```TypeScript
function offPrivateModeChange(callback?: Callback<boolean>): void
```

Unregister the callback for private mode changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-display-function offPrivateModeChange(callback?: Callback<boolean>): void--><!--Device-display-function offPrivateModeChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

