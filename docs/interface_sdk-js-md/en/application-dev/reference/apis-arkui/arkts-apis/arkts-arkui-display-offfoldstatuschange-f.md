# offFoldStatusChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offFoldStatusChange

```TypeScript
function offFoldStatusChange(callback?: Callback<FoldStatus>): void
```

Unregister the callback for fold status changes.

**Since:** 23

<!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void--><!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldStatus&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

