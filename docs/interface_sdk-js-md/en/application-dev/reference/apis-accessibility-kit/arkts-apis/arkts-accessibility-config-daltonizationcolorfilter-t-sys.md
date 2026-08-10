# DaltonizationColorFilter (System API)

```TypeScript
type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'
```

颜色滤镜功能开启时（[daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationstate)设置为true)，颜色滤镜的配置(即设置的DaltonizationColorFilter的值)生效；颜色滤镜功能关闭时（[daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationstate)设置为false)，显示为正常类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'--><!--Device-config-type DaltonizationColorFilter = 'Normal' | 'Protanomaly' | 'Deuteranomaly' | 'Tritanomaly'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| 'Normal' | 表示正常类型。 |
| 'Protanomaly' | 表示红色弱视类型。 |
| 'Deuteranomaly' | 表示绿色弱视类型。 |
| 'Tritanomaly' | 表示蓝色弱视类型。 |

