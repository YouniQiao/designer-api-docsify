# ExtendableColumn

Defines the Extendable Column.

**Inheritance/Implementation:** ExtendableColumn implements [ColumnAttribute](column-columnattribute-i.md)

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
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ColumnOptionsV2 | No |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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
| styles | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ColumnOptionsV2 | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

