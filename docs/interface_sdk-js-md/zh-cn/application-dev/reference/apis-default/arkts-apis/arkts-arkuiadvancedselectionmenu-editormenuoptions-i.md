# EditorMenuOptions

编辑菜单选项。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface EditorMenuOptions--><!--Device-unnamed-export interface EditorMenuOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## action

```TypeScript
action?: VoidCallback
```

点击菜单项的事件回调。

**类型：** [VoidCallback](arkts-voidcallback-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditorMenuOptions-action?: VoidCallback--><!--Device-EditorMenuOptions-action?: VoidCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

点击时显示用户自定义组件，自定义组件在构造时结合@Builder使用。

**类型：** [CustomBuilder](arkts-custombuilder-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditorMenuOptions-builder?: CustomBuilder--><!--Device-EditorMenuOptions-builder?: CustomBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon: ResourceStr | undefined
```

图标资源。

**类型：** [ResourceStr](arkts-resourcestr-t.md) \| undefined

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditorMenuOptions-icon: ResourceStr | undefined--><!--Device-EditorMenuOptions-icon: ResourceStr | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
symbolStyle?: SymbolGlyphModifier
```

Symbol图标资源，优先级大于icon。

**类型：** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditorMenuOptions-symbolStyle?: SymbolGlyphModifier--><!--Device-EditorMenuOptions-symbolStyle?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

