# @ohos.arkui.uiMaterial

本模块提供系统材质的接口定义。不同的系统材质对应不同的UI效果，包括背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)、边框颜色  
[borderColor](CommonMethod#borderColor)、边框宽度[borderWidth](CommonMethod#borderWidth)、阴影  
[shadow](CommonMethod#shadow(value: ShadowOptions | ShadowStyle))效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uiMaterial--><!--Device-unnamed-declare namespace uiMaterial-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [getMaterialInfo](arkts-arkui-uimaterial-getmaterialinfo-f.md#getmaterialinfo) |

### 类

| 名称 |
| --- |
| [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) | 沉浸式材质类，继承自[Material](arkts-arkui-uimaterial-materialtype-e.md#MaterialType)。  沉浸式材质根据设备算力有分档表现，设备算力的高、中、低档由设备厂商决定，定义在系统配置文件中。在高档和中档算力设备上，影响材质层滤镜效果和阴影  [shadow](CommonMethod#shadow(value: ShadowOptions \| ShadowStyle))效果。在低档算力设备上，影响背景色  [backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](CommonMethod#borderColor)、边框宽度[borderWidth](CommonMethod#borderWidth)、阴影  [shadow](CommonMethod#shadow(value: ShadowOptions \|
| [Material](arkts-arkui-uimaterial-material-c.md) |

### 接口

| 名称 |
| --- |
| [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) |
| [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) |
| [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md) |
| [MaterialState](arkts-arkui-uimaterial-materialstate-e.md) |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e.md) |
