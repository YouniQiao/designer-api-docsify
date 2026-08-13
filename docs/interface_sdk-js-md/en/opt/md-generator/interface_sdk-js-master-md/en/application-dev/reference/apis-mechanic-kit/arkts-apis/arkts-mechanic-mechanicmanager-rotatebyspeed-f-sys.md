# rotateBySpeed (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## rotateBySpeed

```TypeScript
function rotateBySpeed(mechId: number, speed: RotationSpeed, duration: number): Promise<Result>
```

Rotates a mechanical device at the specified speed.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function rotateBySpeed(mechId: int, speed: RotationSpeed, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotateBySpeed(mechId: int, speed: RotationSpeed, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |
| speed | [RotationSpeed](arkts-mechanic-mechanicmanager-rotationspeed-i-sys.md) | Yes |
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
console.info('Start rotate');
let degree: mechanicManager.RotationSpeed = {
  yawSpeed: 3 * Math.PI,
  rollSpeed: 3 * Math.PI,
  pitchSpeed: 3 * Math.PI
}
mechanicManager.rotateBySpeed(0, degree, 500)
  .then((result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('Rotate finish');
```
