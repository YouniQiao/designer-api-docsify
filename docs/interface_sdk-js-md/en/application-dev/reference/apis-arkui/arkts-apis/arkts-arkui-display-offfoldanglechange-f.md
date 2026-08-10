# offFoldAngleChange

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offFoldAngleChange

```TypeScript
function offFoldAngleChange(callback?: Callback<Array<double>>): void
```

Unregister the callback for fold angle changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function offFoldAngleChange(callback?: Callback<Array<double>>): void--><!--Device-display-function offFoldAngleChange(callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;double&gt;&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

