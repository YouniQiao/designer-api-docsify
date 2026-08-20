# ExtendableRow

Defines the Extendable Row.

@implements RowAttribute

**Inheritance/Implementation:** ExtendableRow implements [RowAttribute](arkts-arkui-row-attribute.md#rowattribute)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableRow--><!--Device-unnamed-export declare abstract class ExtendableRow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableRow>(
        factory: ConstructorT<T>, 
        options?: RowOptions | RowOptionsV2,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Row.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRow-@ComponentBuilder    static $_instantiate<T extends ExtendableRow>(        factory: ConstructorT<T>,         options?: RowOptions | RowOptionsV2,        content_?: CustomBuilder    ): T--><!--Device-ExtendableRow-@ComponentBuilder    static $_instantiate<T extends ExtendableRow>(        factory: ConstructorT<T>,         options?: RowOptions | RowOptionsV2,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | No |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableRow>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Row.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRow-@Builder    static _instantiateImpl<T extends ExtendableRow>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableRow-@Builder    static _instantiateImpl<T extends ExtendableRow>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

## setRowOptions

```TypeScript
public setRowOptions(options?: RowOptions | RowOptionsV2): this
```

Set the Row Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRow-public setRowOptions(options?: RowOptions | RowOptionsV2): this--><!--Device-ExtendableRow-public setRowOptions(options?: RowOptions | RowOptionsV2): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-row-rowoptionsv2-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableRow](arkts-arkui-row-extendablerow-c.md) |  |

