# VibrateTime

指定时长振动类型。仅对振动时长进行启动或停止控制，满足基础功能，无法对振动强度、频率等维度进行个性化设置。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibrateTime--><!--Device-vibrator-interface VibrateTime-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## duration

```TypeScript
duration: int
```

马达持续振动时长。单位：ms。取值范围：(0,1800000]区间内所有整数。由于实际产品厂商驱动对器件保护设计规格不同，不同设备实际最大振动时长会有差异。建议值：单次触发长振动一般建议不超过10000（10秒），以最大化用户体验。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateTime-duration: int--><!--Device-VibrateTime-duration: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## type

```TypeScript
type: 'time'
```

值为'time'，按照指定时长触发马达振动。固定值，不可更改。

**Type:** 'time'

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateTime-type: 'time'--><!--Device-VibrateTime-type: 'time'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

