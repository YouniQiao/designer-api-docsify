# onRotationAxesStatusChange (System API)

## onRotationAxesStatusChange

```TypeScript
function onRotationAxesStatusChange(callback: Callback<RotationAxesStateChangeInfo>): void
```

Register a listener for axis state changes.The status of the rotation axis changes dynamically, which needs to be monitored.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-mechanicManager-function onRotationAxesStatusChange(callback: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function onRotationAxesStatusChange(callback: Callback<RotationAxesStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;RotationAxesStateChangeInfo&gt; | Yes | Rotate axis state changes callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

