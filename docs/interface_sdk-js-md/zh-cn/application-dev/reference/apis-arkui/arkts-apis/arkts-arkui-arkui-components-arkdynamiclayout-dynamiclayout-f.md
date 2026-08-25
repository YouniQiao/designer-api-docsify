# DynamicLayout

## 导入模块

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## DynamicLayout

```TypeScript
export declare function DynamicLayout (
    algorithm: LayoutAlgorithm,
    content_: CustomBuilder,
): DynamicLayoutAttribute
```

动态布局容器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | 是 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) |
