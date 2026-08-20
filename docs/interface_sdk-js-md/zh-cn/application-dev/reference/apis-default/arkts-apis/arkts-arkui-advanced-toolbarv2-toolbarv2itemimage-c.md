# ToolBarV2ItemImage

定义工具栏子项的普通图标。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ToolBarV2ItemImage--><!--Device-unnamed-export declare class ToolBarV2ItemImage-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemImageOptions)
```

ToolBarV2ItemImage的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)--><!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemImageOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemimageoptions-i.md) | 是 | text info. |

## activatedColor

```TypeScript
@Trace
  public activatedColor?: ColorMetrics
```

工具栏子项在激活态下图标的颜色。

默认值：\$r('sys.color.icon_emphasize')

**类型：** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemImage-@Trace  public activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  public activatedColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  public color?: ColorMetrics
```

工具栏子项的图标的颜色。

默认值：\$r('sys.color.icon_primary')

**类型：** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemImage-@Trace  public color?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  public color?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
@Trace
  public src: ResourceStr
```

工具栏子项的图标。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemImage-@Trace  public src: ResourceStr--><!--Device-ToolBarV2ItemImage-@Trace  public src: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

