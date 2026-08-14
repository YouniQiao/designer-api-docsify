# offRotationAxesStatusChange (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'mechanicManager';
```

## offRotationAxesStatusChange

```TypeScript
function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void
```

Unregister a listener for axis state changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-mechanicManager-function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function offRotationAxesStatusChange(callback?: Callback<RotationAxesStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationAxesStateChangeInfo](arkts-mechanic-mechanicmanager-rotationaxesstatechangeinfo-i-sys.md)&gt; | No | Rotate axis state changes callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

