# DrawableTabBarIndicator

使用图片资源作为下划线的对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: Length
```

下划线的圆角半径（不支持百分比设置）。默认值：0.0单位：vp取值范围：[0, +∞)

**类型：** [Length](arkts-arkui-length-t.md)

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## drawable

```TypeScript
drawable?: DrawableDescriptor
```

下划线的图源。支持[DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)、 [PixelMapDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-pixelmapdrawabledescriptor-c.md)、 [LayeredDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md)和 [AnimatedDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)类型。当传入无效图源时将显示 默认的实线型下划线。

**类型：** [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Length
```

下划线的高度（不支持百分比设置）。默认值：2.0单位：vp取值范围：[0, +∞)

**类型：** [Length](arkts-arkui-length-t.md)

**默认值：** 2vp

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## marginTop

```TypeScript
marginTop?: Length
```

下划线与文字的间距（不支持百分比设置）。默认值：8.0单位：vp取值范围：[0, +∞)

**类型：** [Length](arkts-arkui-length-t.md)

**默认值：** 8vp

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Length
```

下划线的宽度（不支持百分比设置）。默认值：0.0单位：vp取值范围：[0, +∞)宽度设置为0时，按页签文本宽度显示。

**类型：** [Length](arkts-arkui-length-t.md)

**默认值：** 0

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
