# MenuItemConfiguration

菜单项配置接口，用于ContentModifier中。

**Inheritance/Implementation:** MenuItemConfiguration extends [CommonConfiguration<MenuItemConfiguration>](CommonConfiguration<MenuItemConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MenuItemConfiguration extends CommonConfiguration<MenuItemConfiguration>--><!--Device-unnamed-export declare interface MenuItemConfiguration extends CommonConfiguration<MenuItemConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerSelect

```TypeScript
triggerSelect(index: int, value: string): void
```

下拉菜单选中某一项的回调函数。&lt;br/&gt;index：选中菜单项的索引。&lt;br/&gt;value：选中菜单项的文本。&lt;br/&gt;**说明：** &lt;br/&gt;index会赋值给事件[onSelect](../arkts-components/arkts-arkui-onselectcallback-t.md/arkts-arkui-onselectcallback-t.md)回调中的索引参数； value会返回给Select组件显示，同时会赋值给事件[onSelect](../arkts-components/arkts-arkui-onselectcallback-t.md/arkts-arkui-onselectcallback-t.md)回调中的文本参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-triggerSelect(index: int, value: string): void--><!--Device-MenuItemConfiguration-triggerSelect(index: int, value: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 菜单项的索引。 |
| value | string | Yes | 菜单项的文本内容。 |

## icon

```TypeScript
icon?: ResourceStr
```

菜单项的图标。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-icon?: ResourceStr--><!--Device-MenuItemConfiguration-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

菜单项的索引。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-index: int--><!--Device-MenuItemConfiguration-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected: boolean
```

菜单项是否被选中。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-selected: boolean--><!--Device-MenuItemConfiguration-selected: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIcon

```TypeScript
symbolIcon?: SymbolGlyphModifier
```

下拉选项Symbol图片。

symbolIcon优先级高于icon。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-symbolIcon?: SymbolGlyphModifier--><!--Device-MenuItemConfiguration-symbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr
```

菜单项的文本内容。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-value: ResourceStr--><!--Device-MenuItemConfiguration-value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

