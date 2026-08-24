# ExtendableColumn

Defines the Extendable Column.@implements ColumnAttribute

**Inheritance/Implementation:** ExtendableColumn implements [ColumnAttribute](arkts-arkui-column-attribute.md#columnattribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableColumn--><!--Device-unnamed-export declare abstract class ExtendableColumn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableColumn>(
        factory: ConstructorT<T>, 
        options?: ColumnOptions | ColumnOptionsV2, 
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Column.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-@ComponentBuilder    static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T--><!--Device-ExtendableColumn-@ComponentBuilder    static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableColumn>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Column.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-@Builder    static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableColumn-@Builder    static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

## setColumnOptions

```TypeScript
public setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this
```

Set the Column Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-public setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this--><!--Device-ExtendableColumn-public setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableColumn](arkts-arkui-column-extendablecolumn-c.md) |  |

