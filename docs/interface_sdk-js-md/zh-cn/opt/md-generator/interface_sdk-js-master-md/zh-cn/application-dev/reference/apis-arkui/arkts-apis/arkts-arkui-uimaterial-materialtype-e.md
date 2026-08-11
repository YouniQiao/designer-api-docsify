# MaterialType

系统材质类型枚举。

**起始版本：** 26.0.0

<!--Device-uiMaterial-enum MaterialType--><!--Device-uiMaterial-enum MaterialType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

无系统材质效果。对应的效果为背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)为透明色，边框颜色[borderColor](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#bordercolor)为透明色，边框宽度[borderWidth](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#borderwidth)为0，无阴影  
[shadow](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#shadow)。

**系统接口：** 此接口为系统接口。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-MaterialType-NONE = 0--><!--Device-MaterialType-NONE = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SEMI_TRANSPARENT

```TypeScript
SEMI_TRANSPARENT = 1
```

半透明系统材质效果。对应的效果为：

背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)：浅色模式为"#f2f1f3f5"，深色模式为"#f2303131"。

边框颜色[borderColor](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#bordercolor)为混合10%的透明度的theme.colors.compForegroundPrimary的  
[token](../../../ui/theme_skinning.md#系统缺省token色值)值。

边框宽度[borderWidth](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#borderwidth)为1vp。

阴影[shadow](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#shadow)为ShadowStyle.OUTER_DEFAULT_SM。

**系统接口：** 此接口为系统接口。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-MaterialType-SEMI_TRANSPARENT = 1--><!--Device-MaterialType-SEMI_TRANSPARENT = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## IMMERSIVE

```TypeScript
IMMERSIVE = 2
```

沉浸式材质类型。仅用于[MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md)接口的type属性标识当前配置的材质类型，不映射到底层功能。实际材质效果通过  
[ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md)类实现。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MaterialType-IMMERSIVE = 2--><!--Device-MaterialType-IMMERSIVE = 2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
