# offFoldAngleChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offFoldAngleChange

```TypeScript
function offFoldAngleChange(callback?: Callback<Array<double>>): void
```

Unregister the callback for fold angle changes.

**Since:** 23

<!--Device-display-function offFoldAngleChange(callback?: Callback<Array<double>>): void--><!--Device-display-function offFoldAngleChange(callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;double&gt;&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

