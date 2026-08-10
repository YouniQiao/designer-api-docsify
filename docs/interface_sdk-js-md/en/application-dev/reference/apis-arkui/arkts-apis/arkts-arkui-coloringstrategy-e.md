# ColoringStrategy

智能取色枚举类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum ColoringStrategy--><!--Device-unnamed-declare enum ColoringStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## INVERT

```TypeScript
INVERT = 'invert'
```

设置前景色为控件背景色的反色。仅支持在[foregroundColor](arkts-arkui-common-commonmethod-i.md#foregroundcolor)中设置该枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColoringStrategy-INVERT = 'invert'--><!--Device-ColoringStrategy-INVERT = 'invert'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AVERAGE

```TypeScript
AVERAGE = 'average'
```

设置控件背景阴影色为控件背景阴影区域的平均色。仅支持在入参类型为ShadowOptions的  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)中设置该枚举。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColoringStrategy-AVERAGE = 'average'--><!--Device-ColoringStrategy-AVERAGE = 'average'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PRIMARY

```TypeScript
PRIMARY = 'primary'
```

设置控件背景阴影色为控件背景阴影区域的主色。仅支持在入参类型为ShadowOptions的  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)中设置该枚举。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ColoringStrategy-PRIMARY = 'primary'--><!--Device-ColoringStrategy-PRIMARY = 'primary'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

