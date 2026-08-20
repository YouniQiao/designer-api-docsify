# Blank属性/事件

除支持通用属性外，还支持以下属性：

支持通用事件。

**继承/实现关系：** BlankAttribute extends CommonMethod<BlankAttribute>

**起始版本：** 7

<!--Device-unnamed-declare class BlankAttribute--><!--Device-unnamed-declare class BlankAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## color

```TypeScript
color(value: ResourceColor)
```

设置空白填充的填充颜色，支持attributeModifier动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-BlankAttribute-color(value: ResourceColor): BlankAttribute--><!--Device-BlankAttribute-color(value: ResourceColor): BlankAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 空白填充的填充颜色。<br/>默认值：Color.Transparent &lt;br /&gt;非法值：按默认值处理。 |

