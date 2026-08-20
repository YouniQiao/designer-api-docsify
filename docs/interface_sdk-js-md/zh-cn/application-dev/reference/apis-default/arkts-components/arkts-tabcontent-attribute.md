# TabContentAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** TabContentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface TabContentAttribute--><!--Device-unnamed-export declare interface TabContentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置TabContent组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabContentAttribute-attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TabContentAttribute-attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabContentAttribute](arkts-tabcontent-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## onWillHide

```TypeScript
onWillHide(event: VoidCallback | undefined): this
```

逻辑回调，TabContent将要隐藏的时候触发该回调。场景包括TabContent切换，页面切换，窗口前后台切换。取值为undefined时，不使用回调函数。

> **说明：**
> 
> 从API version 20开始，该接口支持在 &gt; [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier) &gt; 中调用。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabContentAttribute-onWillHide(event: VoidCallback | undefined): this--><!--Device-TabContentAttribute-onWillHide(event: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 | TabContent将要隐藏的回调函数。<br/>取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## onWillShow

```TypeScript
onWillShow(event: VoidCallback | undefined): this
```

逻辑回调，TabContent将要显示的时候触发该回调。场景包括TabContent首次显示，TabContent切换，页面切换，窗口前后台切换。取值为undefined时，不使用回调函数。

> **说明：**
> 
> 从API version 20开始，该接口支持在 &gt; [attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier) &gt; 中调用。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabContentAttribute-onWillShow(event: VoidCallback | undefined): this--><!--Device-TabContentAttribute-onWillShow(event: VoidCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 | TabContent将要显示的回调函数。<br/>取值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## setTabContentOptions

```TypeScript
setTabContentOptions(): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-TabContentAttribute-setTabContentOptions(): this--><!--Device-TabContentAttribute-setTabContentOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## tabBar

```TypeScript
tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this
```

设置TabBar上显示内容。

使用BottomTabBarStyle或TabBarOptions类型作为入参并设置icon，icon异常时显示灰色图块。如果icon采用svg格式图源，需删除svg图源内置的宽高属性值。否则，icon大小将使用svg图源内置的宽 高属性值。

设置的内容超出TabBar页签时进行裁切。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabContentAttribute-tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this--><!--Device-TabContentAttribute-tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContentBase](../arkts-apis/arkts-componentcontent-componentcontentbase-c.md) \| [SubTabBarStyle](arkts-tabcontent-subtabbarstyle-c.md) \| [BottomTabBarStyle](arkts-tabcontent-bottomtabbarstyle-c.md) \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| [TabBarOptions](arkts-tabcontent-tabbaroptions-i.md) \| undefined | 是 | TabBar上显示内容。<br/>ComponentContent/ComponentContentBase： 组件内容的实体封装，可以设置自定义 内容。<br/>SubTabBarStyle：?子页签样式。<br/>BottomTabBarStyle：?底部页签和侧边页签样式，底部样式没有下划线效果。<br/>string： 字符串类型。<br/>Resource： 资源引用类型，引入系统资源或者应用资源中的字符串。<br/>CustomBuilder： 构造器，内部可以传入组件。<br/>TabBarOptions： 设置页签内的图片和文字内容。<br/>取值为undefined时， 无显示内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## default

```TypeScript
default
```

设置tabContent选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabContentAttribute-default--><!--Device-TabContentAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

