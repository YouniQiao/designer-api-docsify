# VibrateAttribute

马达振动属性。用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)接口的attribute参数，指定马达ID、设备ID和振动使用场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibrateAttribute--><!--Device-vibrator-interface VibrateAttribute-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId?: int
```

设备ID。默认值：-1，表示本地设备。使用场景：在多设备场景下需指定远程设备时设置此参数；不填写时默认控制本地设备。从API version 19开始，设备ID可以使用  
[getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md#getvibratorinfosync)或[on](arkts-sensorservice-vibrator-on-f.md#on)查询。

从API version 19开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VibrateAttribute-deviceId?: int--><!--Device-VibrateAttribute-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## id

```TypeScript
id?: int
```

马达ID。默认值：0。使用场景：当设备存在多个马达时，可通过指定不同的马达ID来选择特定马达触发振动。马达ID可以通过  
[getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md#getvibratorinfosync)查询。不填写时默认使用马达ID为0的马达。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateAttribute-id?: int--><!--Device-VibrateAttribute-id?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## usage

```TypeScript
usage: Usage
```

马达振动的使用场景。默认值：'unknown'。取值范围只允许在[Usage](arkts-sensorservice-vibrator-usage-t.md)提供的类型中选取。不同usage值对应不同的系统振动开关管控规则，开发者需根据实际业务场景选择合适的usage值。

从API version 11开始，该接口支持在原子化服务中使用。

**Type:** [Usage](arkts-sensorservice-vibrator-usage-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateAttribute-usage: Usage--><!--Device-VibrateAttribute-usage: Usage-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

