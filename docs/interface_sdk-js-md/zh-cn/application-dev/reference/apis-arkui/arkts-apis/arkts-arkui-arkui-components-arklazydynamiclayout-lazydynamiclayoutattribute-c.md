# LazyDynamicLayoutAttribute

定义LazyDynamicLayout组件。@extends CommonMethod&lt;LazyDynamicLayoutAttribute&gt;

**继承/实现关系：** LazyDynamicLayoutAttribute extends CommonMethod<LazyDynamicLayoutAttribute>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { LazyDynamicLayout, LazyDynamicLayoutAttribute } from '@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(
      modifier: AttributeModifier<LazyDynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用了AttributeModifier。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](arkts-arkui-common-attributemodifier-i.md)&lt;[LazyDynamicLayoutAttribute](arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md)&gt; \| [AttributeModifier](arkts-arkui-common-attributemodifier-i.md)&lt;[CommonMethod](arkts-arkui-common-commonmethod-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute
```

当可见索引更改时调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-t.md)&lt;number[]&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LazyDynamicLayoutAttribute](arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md) |

## setLazyDynamicLayoutOptions

```TypeScript
default setLazyDynamicLayoutOptions(algorithm: LazyLayoutAlgorithm): this
```

设置LazyDynamicLayout选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | [LazyLayoutAlgorithm](arkts-arkui-lazylayoutalgorithm-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
