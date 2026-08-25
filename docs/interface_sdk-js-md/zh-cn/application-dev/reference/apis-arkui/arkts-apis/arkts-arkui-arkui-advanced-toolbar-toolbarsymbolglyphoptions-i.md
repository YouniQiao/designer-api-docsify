# ToolBarSymbolGlyphOptions

ToolBarSymbolGlyphOptions定义图标的属性。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ItemState, ToolBar, ToolBarOption, ToolBarOptions, ToolBarModifier } from '@kit.ArkUI';
```

## activated

```TypeScript
activated?: SymbolGlyphModifier
```

工具栏symbol图标激活态样式。默认值：fontColor：\$r('sys.color.icon_emphasize')，fontSize：24vp。

**类型：** [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
normal?: SymbolGlyphModifier
```

工具栏symbol图标普通态样式。默认值：fontColor：\$r('sys.color.icon_primary')，fontSize：24vp。

**类型：** [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
