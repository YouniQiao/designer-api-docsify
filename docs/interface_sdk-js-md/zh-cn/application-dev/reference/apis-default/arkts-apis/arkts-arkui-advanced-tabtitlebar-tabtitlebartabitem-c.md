# TabTitleBarTabItem

Declaration of the tab item.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class TabTitleBarTabItem--><!--Device-unnamed-export declare class TabTitleBarTabItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## icon

```TypeScript
public icon?: ResourceStr
```

页签图标资源。若设置了symbolStyle，则该属性不生效。若不设置，页签仅显示文字内容。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBarTabItem-public icon?: ResourceStr--><!--Device-TabTitleBarTabItem-public icon?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
public symbolStyle?: SymbolGlyphModifier
```

Symbol图标资源，优先级大于icon。当需要使用Symbol图标作为页签时传入此参数，不传入时使用icon参数设置的图片页签。

**类型：** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBarTabItem-public symbolStyle?: SymbolGlyphModifier--><!--Device-TabTitleBarTabItem-public symbolStyle?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
public title: ResourceStr
```

页签项显示的文字内容。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBarTabItem-public title: ResourceStr--><!--Device-TabTitleBarTabItem-public title: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

