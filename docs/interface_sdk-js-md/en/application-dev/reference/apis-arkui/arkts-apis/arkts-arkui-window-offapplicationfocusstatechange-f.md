# offApplicationFocusStateChange

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
import { floatView } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
```

## offApplicationFocusStateChange

```TypeScript
function offApplicationFocusStateChange(callback?: Callback<boolean>): void
```

Unregister the callback for application process focus state changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function offApplicationFocusStateChange(callback?: Callback<boolean>): void--><!--Device-window-function offApplicationFocusStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No | Callback used to return the result whether application process focused or not. If not provided, all callbacks for the given event type will be removed. |

