# ToolBarV2SymbolGlyph

ToolBarV2SymbolGlyph定义Symbol图标的属性。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ToolBarV2SymbolGlyph--><!--Device-unnamed-export declare class ToolBarV2SymbolGlyph-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2SymbolGlyphOptions)
```

ToolBarV2SymbolGlyph的构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)--><!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2SymbolGlyphOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2symbolglyphoptions-i.md) | 是 | symbol info. |

## activated

```TypeScript
@Trace
  public activated?: SymbolGlyphModifier
```

工具栏symbol图标激活态样式。

默认值：fontColor：\$r('sys.color.icon_emphasize')，fontSize：24vp。

**类型：** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2SymbolGlyph-@Trace  public activated?: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  public activated?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
@Trace
  public normal: SymbolGlyphModifier
```

工具栏symbol图标普通态样式。

**类型：** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2SymbolGlyph-@Trace  public normal: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  public normal: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

