# off (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## off('rotationAxesStatusChange')

```TypeScript
function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void
```

Unregister a listener for axis state changes.

**Since:** 20

<!--Device-mechanicManager-function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rotationAxesStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RotationAxesStateChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
console.info('Unregister Axis Status listener');
mechanicManager.off("rotationAxesStatusChange", (result: mechanicManager.RotationAxesStateChangeInfo) => {
  console.info(`'result:' ${result}`);
});
console.info('Unregister successfully');
```
