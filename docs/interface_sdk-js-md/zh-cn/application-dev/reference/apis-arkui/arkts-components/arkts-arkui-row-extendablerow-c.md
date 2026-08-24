# ExtendableRow

Defines the Extendable Row.@implements RowAttribute

**继承/实现关系：** ExtendableRow implements [RowAttribute](arkts-arkui-row-attribute.md#rowattribute)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export declare abstract class ExtendableRow--><!--Device-unnamed-export declare abstract class ExtendableRow-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableRow>(
        factory: ConstructorT<T>,
        options?: RowOptions | RowOptionsV2,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Row.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableRow-@ComponentBuilder    static $_instantiate<T extends ExtendableRow>(        factory: ConstructorT<T>,        options?: RowOptions | RowOptionsV2,        content_?: CustomBuilder    ): T--><!--Device-ExtendableRow-@ComponentBuilder    static $_instantiate<T extends ExtendableRow>(        factory: ConstructorT<T>,        options?: RowOptions | RowOptionsV2,        content_?: CustomBuilder    ): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | 是 |  |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | 否 |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableRow>(
        styles: CustomBuilderT<T>,
        factory: ConstructorT<T>,
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Row.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableRow-@Builder    static _instantiateImpl<T extends ExtendableRow>(        styles: CustomBuilderT<T>,        factory: ConstructorT<T>,        content_?: CustomBuilder    ): void--><!--Device-ExtendableRow-@Builder    static _instantiateImpl<T extends ExtendableRow>(        styles: CustomBuilderT<T>,        factory: ConstructorT<T>,        content_?: CustomBuilder    ): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | 是 |  |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | 是 |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 |  |

## setRowOptions

```TypeScript
public setRowOptions(options?: RowOptions | RowOptionsV2): this
```

Set the Row Options.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableRow-public setRowOptions(options?: RowOptions | RowOptionsV2): this--><!--Device-ExtendableRow-public setRowOptions(options?: RowOptions | RowOptionsV2): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExtendableRow](arkts-arkui-row-extendablerow-c.md) |  |

