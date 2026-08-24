# ExtendableToggle

Defines the Extendable Toggle.

**继承/实现关系：** ExtendableToggle implements [ToggleAttribute](arkts-toggle-attribute.md#toggleattribute)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export declare abstract class ExtendableToggle--><!--Device-unnamed-export declare abstract class ExtendableToggle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableToggle>(
        factory: ConstructorT<T>, 
        options: ToggleOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Toggle.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableToggle-@ComponentBuilder    static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableToggle-@ComponentBuilder    static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | 是 |  |
| options | [ToggleOptions](arkts-toggle-toggleoptions-i.md) | 是 |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableToggle>(
        styles: CustomBuilderT<T>,  
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Toggle.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableToggle-@Builder    static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableToggle-@Builder    static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | 是 |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | 是 |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 |  |

## setToggleOptions

```TypeScript
public setToggleOptions(options: ToggleOptions): this
```

Set the Toggle Options.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this--><!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-toggle-toggleoptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExtendableToggle](arkts-toggle-extendabletoggle-c.md) |  |

