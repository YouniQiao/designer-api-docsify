# DynamicLayoutAttribute

支持通用属性。支持通用事件。

**继承/实现关系：** DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为24。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(
      modifier: AttributeModifier<DynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | AttributeModifier&lt;[DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md)&gt; \| AttributeModifier & lt;CommonMethod & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
