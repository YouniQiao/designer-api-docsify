# EffectType

使用效果模板种类的枚举值。

 **效果模板：**

| 设备类型 | 模糊半径(单位: px) | 饱和度 | 亮度 | 颜色 |  
| -------- | ---- | ---------------------- | -------- | -------- |  
| 移动设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |  
| 2in1设备：深色模式 | 80 | 1.5 | 1.0 | '#e52e3033'，显示为淡红色的半透明效果。 |  
| 2in1设备：浅色模式 | 80 | 1.9 | 1.0 | '#e5ffffff'，显示为半透明的深红色。 |  
| Tablet设备 | 0 | 0 | 0 | '#ffffffff'，显示为白色。 |

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare enum EffectType--><!--Device-unnamed-declare enum EffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

使用&lt;!--Del--&gt;父级EffectComponent定义的&lt;!--DelEnd--&gt;效果模板进行定义。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-EffectType-DEFAULT = 0--><!--Device-EffectType-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WINDOW_EFFECT

```TypeScript
WINDOW_EFFECT = 1
```

使用窗口定义的效果模板进行定义。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-EffectType-WINDOW_EFFECT = 1--><!--Device-EffectType-WINDOW_EFFECT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

