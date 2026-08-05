# off (System API)

## off('rotationAxesStatusChange')

```TypeScript
function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void
```

Unregister a listener for axis state changes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-mechanicManager-function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'rotationAxesStatusChange' | Yes | Event type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;RotationAxesStateChangeInfo&gt; | No | Rotate axis state changes callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

**Example**

```TypeScript
console.info('Unregister Axis Status listener');
mechanicManager.off("rotationAxesStatusChange", (result: mechanicManager.RotationAxesStateChangeInfo) => {
  console.info(`'result:' ${result}`);
});
console.info('Unregister successfully');
```

