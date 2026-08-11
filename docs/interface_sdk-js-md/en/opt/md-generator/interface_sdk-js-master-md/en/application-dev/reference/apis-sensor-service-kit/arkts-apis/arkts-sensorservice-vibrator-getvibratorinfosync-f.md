# getVibratorInfoSync

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## getVibratorInfoSync

```TypeScript
function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>
```

Queries the vibrator list of one or all devices.

**Since:** 19

<!--Device-vibrator-function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>--><!--Device-vibrator-function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [VibratorInfoParam](arkts-sensorservice-vibrator-vibratorinfoparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;VibratorInfo&gt; |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const vibratorInfoList: vibrator.VibratorInfo[] = vibrator.getVibratorInfoSync({ deviceId: 1, vibratorId: 3 });
  console.info(`vibratorInfoList: ${JSON.stringify(vibratorInfoList)}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
