# ExtendableListItem

可扩展的ListItem组件。

**继承/实现关系：** ExtendableListItem implements [ListItemAttribute](arkts-arkui-listitem-listitemattribute-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableListItem>(
    factory: ConstructorT<T>, 
    value?: ListItemOptions, 
    content_?: CustomBuilder
  ): T
```

可扩展的ListItem组件的构造函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |
| value | [ListItemOptions](arkts-arkui-listitem-listitemoptions-i.md) | 否 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableListItem>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

扩展列表项组件入口

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | 是 |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

## setListItemOptions

```TypeScript
public setListItemOptions(value?: ListItemOptions): this
```

设置ListItem组件参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ListItemOptions](arkts-arkui-listitem-listitemoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ExtendableListItem](arkts-arkui-listitem-extendablelistitem-c.md) |
