# ImmersiveOptions

沉浸式材质参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-uiMaterial-export interface ImmersiveOptions--><!--Device-uiMaterial-export interface ImmersiveOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## applyShadow

```TypeScript
applyShadow?: boolean
```

是否添加材质的阴影效果。

当该参数为true时，材质中的阴影效果固定生效，优先于[shadow](arkts-arkui-common-commonmethod-i.md#shadow)通用属性。当该参数为false时，shadow通用属性生效，材质的阴影效果不生效。

**说明：**该参数仅对所有档位的算力设备的显示效果生效。

默认值：true

**类型：** boolean

**默认值：** true

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-applyShadow?: boolean--><!--Device-ImmersiveOptions-applyShadow?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## colorInvert

```TypeScript
colorInvert?: boolean
```

设置了材质对象的节点的子树是否自动适配材质到背景色的反色。

若为false，则不会自动反色。

若为true，则只有材质参数足够薄时才会自动反色。具体能反色的材质由系统定义，材质样式至少为THIN或ULTRA_THIN，且与设置应用的沉浸光感的强弱配置相关。材质越薄、沉浸光感越强，越容易符合反色材质的要求。

自动反色能力仅对部分属性接口设置特殊资源值时生效，生效的属性接口包括：Text组件的[fontColor](arkts-arkui-text-textattribute-i.md#fontcolor)，Button组件的  
[fontColor](arkts-arkui-button-buttonattribute-i.md#fontcolor)，SymbolGlyph组件的  
[fontColor](arkts-arkui-symbolglyph-symbolglyphattribute-i.md#fontcolor)，Image组件的  
[fillColor](arkts-arkui-image-imageattribute-i.md#fillcolor)，Search组件的  
[placeholderColor](arkts-arkui-search-searchattribute-i.md#placeholdercolor)、[fontColor](arkts-arkui-search-searchattribute-i.md#fontcolor)、  
[searchIcon](arkts-arkui-search-searchattribute-i.md#searchicon)中的图标颜色、[cancelButton](arkts-arkui-search-searchattribute-i.md#cancelbutton)中的图标颜色、  
[caretStyle](arkts-arkui-search-searchattribute-i.md#caretstyle)中的光标颜色，TabContent组件的  
[tabBar](arkts-arkui-tabcontent-tabcontentattribute-i.md#tabbar)属性使用  
[BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md)样式时其中的文本和图标颜色。

**说明：**该参数仅对高档和中档算力设备的显示效果生效。

默认值：false

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-colorInvert?: boolean--><!--Device-ImmersiveOptions-colorInvert?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## interactive

```TypeScript
interactive?: boolean
```

是否为设置材质的组件设置交互形变效果。

**说明：**该参数对所有档位的算力设备的显示效果生效。

默认值：false

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-interactive?: boolean--><!--Device-ImmersiveOptions-interactive?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lightEffect

```TypeScript
lightEffect?: LightEffectOptions | null
```

是否为设置材质的组件设置光感交互反馈效果。当该参数为null时，禁用光感交互反馈效果。

**说明：**该参数对所有档位的算力设备的显示效果生效。

默认值：undefined，不设置光感交互反馈效果。

**类型：** [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) \| null

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-lightEffect?: LightEffectOptions | null--><!--Device-ImmersiveOptions-lightEffect?: LightEffectOptions | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## materialColor

```TypeScript
materialColor?: ResourceColor
```

材质层赋色，该参数会为材质滤镜再混合一层纯色效果。该颜色需要带一定的透明度值，不能为纯不透明的颜色，否则会将材质滤镜效果完全遮挡。

**说明：**该参数仅对高档和中档算力设备的显示效果生效。

默认值：Color.Transparent

**类型：** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**默认值：** Color.Transparent

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-materialColor?: ResourceColor--><!--Device-ImmersiveOptions-materialColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ImmersiveStyle
```

材质样式。不同样式对应不同的材质参数，影响材质的厚度。

**说明：**该参数仅对高档和中档算力设备的显示效果生效。

默认值：ImmersiveStyle.REGULAR

**类型：** [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md)

**默认值：** uiMaterial.ImmersiveStyle.REGULAR

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImmersiveOptions-style?: ImmersiveStyle--><!--Device-ImmersiveOptions-style?: ImmersiveStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

