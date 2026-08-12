# turnBySpeed (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## turnBySpeed

```TypeScript
function turnBySpeed(mechId: number, angleSpeed: number, duration: number): Promise<Result>
```

Rotate in place according to the speed.

**Since:** 26.0.0

<!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>--><!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |
| angleSpeed | number | Yes |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) |
| [33300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) |
| [33300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300003-function-not-supported) |
