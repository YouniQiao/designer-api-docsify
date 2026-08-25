# ExtendableList

定义可扩展List组件。

**继承/实现关系：** ExtendableList implements [ListAttribute](arkts-arkui-list-listattribute-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableList>(
    factory: ConstructorT<T>, 
    options?: ListOptions, 
    content_?: CustomBuilder
  ): T
```

可扩展List组件的构造函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |
| options | [ListOptions](arkts-arkui-list-listoptions-i.md) | 否 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableList>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): void
```

扩展列表组件入口

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

## setListOptions

```TypeScript
public setListOptions(options?: ListOptions): this
```

设置List组件参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ListOptions](arkts-arkui-list-listoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ExtendableList](arkts-arkui-list-extendablelist-c.md) |
