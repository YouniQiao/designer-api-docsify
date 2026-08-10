# borderRadiuses

## borderRadiuses

```TypeScript
export declare function borderRadiuses(all: double): NodeBorderRadiuses
```

获取所有边都设置为相同半径的BorderRadiuses对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function borderRadiuses(all: double): NodeBorderRadiuses--><!--Device-unnamed-export declare function borderRadiuses(all: double): NodeBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| all | double | Yes | 边框圆角。&lt;br/&gt;单位：vp&lt;br/&gt;。 &lt;br&gt;取值范围：[0, +∞)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NodeBorderRadiuses](arkts-arkui-nodeborderradiuses-t.md) | 边框圆角均设置为传入值的边框圆角对象。 |

