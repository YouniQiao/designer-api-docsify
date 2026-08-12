# isSupportEffectSync

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## isSupportEffectSync

```TypeScript
function isSupportEffectSync(effectId: string): boolean
```

Checks whether the preset vibration effect is supported.

**Since:** 12

<!--Device-vibrator-function isSupportEffectSync(effectId: string): boolean--><!--Device-vibrator-function isSupportEffectSync(effectId: string): boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effectId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14600101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-sensor-service-kit/errorcode-vibrator.md#14600101-device-operation-failed) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether the preset 'haptic.notice.success' is supported.
  let ret = vibrator.isSupportEffectSync('haptic.notice.success');
  console.info(`The query result is ${ret}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
