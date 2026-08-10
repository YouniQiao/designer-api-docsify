# SpaceType

```TypeScript
declare type SpaceType = string | number | Resource
```

Column组件构造函数中space支持的数据类型，取值类型为下表类型中的并集。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-unnamed-declare type SpaceType = string | number | Resource--><!--Device-unnamed-declare type SpaceType = string | number | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| string | 表示值类型为字符串，取值为可以转换为非负数字的字符串。取负数或不可转换的字符串时，按默认值0处理。 |
| number | 表示类型为数字，取值为大于等于0的数字。取负数或非法值时，按默认值0处理。 |
| Resource | 表示值为资源引用类型，取值为从系统资源或者应用资源中引入的数据值。 |

