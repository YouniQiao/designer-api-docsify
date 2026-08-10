# getVibratorInfoSync

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## getVibratorInfoSync

```TypeScript
function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>
```

查询一个或所有设备的马达信息列表。适用于在触发振动前查询设备马达能力和多马达设备的马达ID，以便选择合适的马达触发振动。不传param时查询所有设备马达信息；传入VibratorInfoParam可查询指定设备或马达。返回VibratorInfo数组，包含deviceId、vibratorId、deviceName、isHdHapticSupported、isLocalVibrator等属性，可用于startVibration (#vibratorstartvibration9)和stopVibration (#vibratorstopvibration19)中指定马达和设备。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-vibrator-function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>--><!--Device-vibrator-function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [VibratorInfoParam](arkts-sensorservice-vibrator-vibratorinfoparam-i.md) | No | 指出需要查询的设备和马达信息。不传param时默认查询所有设备所有马达的信息。deviceId默认值为-1（查询全部设备），vibratorId默认值为0（查询该 设备的全部马达）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;VibratorInfo&gt; | 马达设备的信息数组。每个元素包含deviceId、vibratorId、deviceName、isHdHapticSupported、isLocalVibrator等属性，可 用于选择合适的马达触发振动或判断设备振动能力。 |

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

