# ExtendableGrid

可扩展Grid组件。

**继承/实现关系：** ExtendableGrid implements [GridAttribute](arkts-arkui-grid-gridattribute-i.md#GridAttribute)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare abstract class ExtendableGrid implements GridAttribute--><!--Device-unnamed-export declare abstract class ExtendableGrid implements GridAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableGrid>(
    factory: ConstructorT<T>, 
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions, 
    content_?: CustomBuilder
  ): T
```

创建可扩展Grid组件实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableGrid-static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableGrid-static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |  |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 否 |  |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | 否 |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Grid组件实例。 |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableGrid>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

扩展网格组件入口

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableGrid-static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableGrid-static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | 是 |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | 是 |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

## setGridOptions

```TypeScript
public setGridOptions(
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions
  ): this
```

设置Grid组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this--><!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 否 |  |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Grid组件实例。 |

