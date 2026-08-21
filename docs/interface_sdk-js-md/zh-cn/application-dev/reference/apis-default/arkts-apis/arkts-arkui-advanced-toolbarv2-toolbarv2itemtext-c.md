# ToolBarV2ItemText

定义工具栏子项的文本。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ToolBarV2ItemText--><!--Device-unnamed-export declare class ToolBarV2ItemText-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemTextOptions)
```

ToolBarV2ItemText的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)--><!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemTextOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemtextoptions-i.md) | 是 | text info. |

## activatedColor

```TypeScript
@Trace
  public activatedColor?: ColorMetrics
```

工具栏子项在激活态下文本的颜色。

&lt;/div&gt;默认值：\$r('sys.color.font_emphasize')

**类型：** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemText-@Trace  public activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  public activatedColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  public color?: ColorMetrics
```

工具栏子项的文本的颜色。

默认值：\$r('sys.color.font_primary')

**类型：** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemText-@Trace  public color?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  public color?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
  public text: ResourceStr
```

工具栏子项的文本。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2ItemText-@Trace  public text: ResourceStr--><!--Device-ToolBarV2ItemText-@Trace  public text: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

