# ExtendableColumn

Defines the Extendable Column.

**Inheritance/Implementation:** ExtendableColumn implements [ColumnAttribute](arkts-arkui-column-columnattribute-i.md#ColumnAttribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableColumn implements ColumnAttribute--><!--Device-unnamed-export declare abstract class ExtendableColumn implements ColumnAttribute-End-->

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T--><!--Device-ExtendableColumn-static $_instantiate<T extends ExtendableColumn>(        factory: ConstructorT<T>,         options?: ColumnOptions | ColumnOptionsV2,         content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | No |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableColumn-static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableColumn-static _instantiateImpl<T extends ExtendableColumn>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

## setColumnOptions

```TypeScript
public setColumnOptions(options?: ColumnOptions | ColumnOptionsV2): this
```

Set the Column Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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
| this |  |

