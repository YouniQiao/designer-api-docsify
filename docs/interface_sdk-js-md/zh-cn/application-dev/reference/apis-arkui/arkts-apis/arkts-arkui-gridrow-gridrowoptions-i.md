# GridRowOptions

设置栅格行布局容器的布局选项。@interface GridRowOptions

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## breakpoints

```TypeScript
breakpoints?: BreakPoints
```

设置断点值的断点数组以及基于应用窗口或容器尺寸的相应参照。

**类型：** [BreakPoints](arkts-arkui-gridrow-breakpoints-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## columns

```TypeScript
columns?: int | GridRowColumnOption
```

设置布局列数。

**类型：** int \| [GridRowColumnOption](arkts-arkui-gridrow-gridrowcolumnoption-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: GridRowDirection
```

栅格布局排列方向。

**类型：** [GridRowDirection](arkts-arkui-gridrow-gridrowdirection-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: Length | GutterOption
```

栅格布局间距。

**类型：** [Length](arkts-arkui-length-t.md) \| [GutterOption](arkts-arkui-gridrow-gutteroption-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
