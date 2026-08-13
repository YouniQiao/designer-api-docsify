# rotateToEulerAngles (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## rotateToEulerAngles

```TypeScript
function rotateToEulerAngles(mechId: number, angles: EulerAngles, duration: number): Promise<Result>
```

Rotates a mechanical device to the absolute angles.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |
| angles | [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) | Yes |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |

## Examples

```TypeScript
let degree: mechanicManager.EulerAngles = {
  yaw: 0.9 * Math.PI,
  roll: 0.9 * Math.PI,
  pitch: 0.9 * Math.PI
}
mechanicManager.rotateToEulerAngles(0, degree, 500)
  .then((result: mechanicManager.Result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('End rotation');
```
