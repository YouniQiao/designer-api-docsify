# offFoldDisplayModeChange

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offFoldDisplayModeChange

```TypeScript
function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void
```

Unregister the callback for fold display mode changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void--><!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldDisplayMode&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

