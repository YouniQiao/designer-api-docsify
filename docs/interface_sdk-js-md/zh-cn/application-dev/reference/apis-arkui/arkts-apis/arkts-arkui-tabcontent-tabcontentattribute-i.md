# TabContentAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** TabContentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置TabContent组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## onWillHide

```TypeScript
onWillHide(event: VoidCallback | undefined): this
```

逻辑回调，TabContent将要隐藏的时候触发该回调。场景包括TabContent切换，页面切换，窗口前后台切换。取值为undefined时，不使用回调函数。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## onWillShow

```TypeScript
onWillShow(event: VoidCallback | undefined): this
```

逻辑回调，TabContent将要显示的时候触发该回调。场景包括TabContent首次显示，TabContent切换，页面切换，窗口前后台切换。取值为undefined时，不使用回调函数。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## setTabContentOptions

```TypeScript
default setTabContentOptions(): this
```

设置tabContent选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## tabBar

```TypeScript
tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this
```

设置TabBar上显示内容。使用BottomTabBarStyle或TabBarOptions类型作为入参并设置icon，icon异常时显示灰色图块。如果icon采用svg格式图源，需删除svg图源内置的宽高属性值。否则，icon大小将使用svg图源内置的宽 高属性值。设置的内容超出TabBar页签时进行裁切。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) \| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) \| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) \| string \| [Resource](arkts-arkui-resource-t.md) \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [TabBarOptions](arkts-arkui-tabcontent-tabbaroptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |
