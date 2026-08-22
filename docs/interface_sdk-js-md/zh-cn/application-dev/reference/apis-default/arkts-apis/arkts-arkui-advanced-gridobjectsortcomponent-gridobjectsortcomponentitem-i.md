# GridObjectSortComponentItem

网格对象排序组件的组件数据配置信息。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface GridObjectSortComponentItem--><!--Device-unnamed-export interface GridObjectSortComponentItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## id

```TypeScript
id: int | string
```

数据id序号，不可重复。

默认值：空字符串。

**ArkTS-Dyn起始版本：** 11

**ArkTS-Sta起始版本：** 23

**类型：** int \| string

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-id: int | string--><!--Device-GridObjectSortComponentItem-id: int | string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## order

```TypeScript
order: int
```

顺序序号。 取值范围：大于等于0。 取值应≥0。默认值：0 **ArkTS-Dyn起始版本：** 11 **ArkTS-Sta起始版本：** 23。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-order: int--><!--Device-GridObjectSortComponentItem-order: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected: boolean
```

是否已经被添加，已添加：true，未添加：false。

**ArkTS-Dyn起始版本：** 11

**ArkTS-Sta起始版本：** 23

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-selected: boolean--><!--Device-GridObjectSortComponentItem-selected: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
symbolStyle?: SymbolGlyphModifier
```

GridObjectSortComponentType类型为IMAGE_TEXT时，需要传入Symbol图标资源。配置优先级高于url。 **ArkTS-Dyn起始版本：** 18 **ArkTS-Sta起始版本：** 23。

**类型：** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-symbolStyle?: SymbolGlyphModifier--><!--Device-GridObjectSortComponentItem-symbolStyle?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: ResourceStr
```

显示文本信息。

**ArkTS-Dyn起始版本：** 11

**ArkTS-Sta起始版本：** 23

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-text: ResourceStr--><!--Device-GridObjectSortComponentItem-text: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## url

```TypeScript
url?: ResourceStr
```

GridObjectSortComponentType类型为IMAGE_TEXT时，需要传入图片地址。 **ArkTS-Dyn起始版本：** 11 **ArkTS-Sta起始版本：** 23。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GridObjectSortComponentItem-url?: ResourceStr--><!--Device-GridObjectSortComponentItem-url?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

