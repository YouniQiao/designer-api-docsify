# MaterialType

系统材质类型枚举。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-uiMaterial-export enum MaterialType--><!--Device-uiMaterial-export enum MaterialType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

无系统材质效果。对应的效果为背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)为透明色，边框颜色[borderColor](arkts-arkui-common-commonmethod-i.md#bordercolor)为透明色，边框宽度[borderWidth](arkts-arkui-common-commonmethod-i.md#borderwidth)为0，无阴影  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-NONE = 0--><!--Device-MaterialType-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_TRANSPARENT

```TypeScript
SEMI_TRANSPARENT = 1
```

半透明系统材质效果。对应的效果为：

背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)：浅色模式为"#f2f1f3f5"，深色模式为"#f2303131"。

边框颜色[borderColor](arkts-arkui-common-commonmethod-i.md#bordercolor)为混合10%的透明度的theme.colors.compForegroundPrimary的  
[token](../../../ui/theme_skinning.md#系统缺省token色值)值。

边框宽度[borderWidth](arkts-arkui-common-commonmethod-i.md#borderwidth)为1vp。

阴影[shadow](arkts-arkui-common-commonmethod-i.md#shadow)为ShadowStyle.OUTER_DEFAULT_SM。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-SEMI_TRANSPARENT = 1--><!--Device-MaterialType-SEMI_TRANSPARENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMMERSIVE

```TypeScript
IMMERSIVE = 2
```

沉浸式材质类型。仅用于[MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md)接口的type属性标识当前配置的材质类型，不映射到底层功能。实际材质效果通过  
[ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md)类实现。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialType-IMMERSIVE = 2--><!--Device-MaterialType-IMMERSIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

