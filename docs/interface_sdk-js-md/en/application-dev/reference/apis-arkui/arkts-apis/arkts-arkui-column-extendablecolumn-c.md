# ExtendableColumn

Defines the Extendable Column.

**Inheritance/Implementation:** ExtendableColumn implements ColumnAttribute

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableColumn--><!--Device-unnamed-export declare abstract class ExtendableColumn-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableColumn>(
        factory: ConstructorT<T>, 
        options?: ColumnOptions | ColumnOptionsV2, 
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Column.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-@ComponentBuilder    static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T--><!--Device-ExtendableColumn-@ComponentBuilder    static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-na/arkts-apis/arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableColumn>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Column.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-@Builder    static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableColumn-@Builder    static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-na/arkts-apis/arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

## setColumnOptions

```TypeScript
public setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this
```

Set the Column Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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

