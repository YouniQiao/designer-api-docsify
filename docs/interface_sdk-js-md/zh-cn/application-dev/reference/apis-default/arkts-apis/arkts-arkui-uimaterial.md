# @ohos.arkui.uiMaterial

本模块提供系统材质的接口定义。不同的系统材质对应不同的UI效果，包括背景色 [backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)、边框颜色 borderColor、边框宽度borderWidth、阴影 shadow效果。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uiMaterial--><!--Device-unnamed-declare namespace uiMaterial-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getMaterialInfo](arkts-uimaterial-getmaterialinfo-f.md) | 获取当前应用的材质配置信息。返回的配置信息来自应用在[module.json5](../../../quick-start/module-configuration-file.md)中配置的metadata。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [ImmersiveMaterial](arkts-uimaterial-immersivematerial-c.md) | 沉浸式材质类，继承自[Material](arkts-uimaterial-materialtype-e.md)。 |

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [Material](arkts-uimaterial-material-c-sys.md) | UI侧的系统材质对象。 |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [ImmersiveOptions](arkts-uimaterial-immersiveoptions-i.md) | 沉浸式材质参数。 |
| [LightEffectOptions](arkts-uimaterial-lighteffectoptions-i.md) | 沉浸式材质的光感交互反馈配置。用于自定义反馈光感的颜色。 |
| [MaterialInfo](arkts-uimaterial-materialinfo-i.md) | 材质配置信息，包含材质使能状态和材质类型。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [MaterialOptions](arkts-uimaterial-materialoptions-i-sys.md) | 系统材质选项。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ImmersiveStyle](arkts-uimaterial-immersivestyle-e.md) | 沉浸式材质样式枚举。不同的材质样式对应不同的材质参数，主要包括材质的模糊程度、高光效果等。 |
| [MaterialState](arkts-uimaterial-materialstate-e.md) | 材质使能状态枚举，表示应用级沉浸式系统材质配置的状态。 |
| [MaterialType](arkts-uimaterial-materialtype-e.md) | 系统材质类型枚举。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [MaterialType](arkts-uimaterial-materialtype-e-sys.md) | 系统材质类型枚举。 |
<!--DelEnd-->

