# EffectInfo

查询的预置效果信息。通过[vibrator.getEffectInfoSync](arkts-sensorservice-vibrator-geteffectinfosync-f.md#geteffectinfosync)返回此对象，用于判断预置振动效果是否受指定设备的指定马达支持。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-vibrator-interface EffectInfo--><!--Device-vibrator-interface EffectInfo-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## isEffectSupported

```TypeScript
isEffectSupported: boolean
```

预置效果是否受支持。true表示支持该预置振动效果，可用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)；false表示不支持，使用该effectId触发振动可能效果不佳。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-EffectInfo-isEffectSupported: boolean--><!--Device-EffectInfo-isEffectSupported: boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

