# offApplicationFocusStateChange

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## offApplicationFocusStateChange

```TypeScript
function offApplicationFocusStateChange(callback?: Callback<boolean>): void
```

Unregister the callback for application process focus state changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function offApplicationFocusStateChange(callback?: Callback<boolean>): void--><!--Device-window-function offApplicationFocusStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | Callback used to return the result whether application process focused or not. If not provided, all callbacks for the given event type will be removed. |

