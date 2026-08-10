# VibratorInfo

表示查询的马达信息。通过[vibrator.getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md#getvibratorinfosync)返回此对象，用于获取设备马达能力和选择合适的马达触发振动。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorInfo--><!--Device-vibrator-interface VibratorInfo-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId: int
```

设备ID。可用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)和[stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)等接口指定目标设备。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfo-deviceId: int--><!--Device-VibratorInfo-deviceId: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## deviceName

```TypeScript
deviceName: string
```

设备名称。

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfo-deviceName: string--><!--Device-VibratorInfo-deviceName: string-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## isHdHapticSupported

```TypeScript
isHdHapticSupported: boolean
```

是否支持高清振动。true表示支持高清振动，可使用VibrateFromFile和VibrateFromPattern类型触发振动；false表示不支持，使用自定义振动类型可能效果不佳。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfo-isHdHapticSupported: boolean--><!--Device-VibratorInfo-isHdHapticSupported: boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## isLocalVibrator

```TypeScript
isLocalVibrator: boolean
```

是否为本地设备。true表示本地设备，可直接触发振动；false表示远程设备，需在分布式场景下使用。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfo-isLocalVibrator: boolean--><!--Device-VibratorInfo-isLocalVibrator: boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## vibratorId

```TypeScript
vibratorId: int
```

马达ID。可用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)和[stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)等接口指定目标马达。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfo-vibratorId: int--><!--Device-VibratorInfo-vibratorId: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

