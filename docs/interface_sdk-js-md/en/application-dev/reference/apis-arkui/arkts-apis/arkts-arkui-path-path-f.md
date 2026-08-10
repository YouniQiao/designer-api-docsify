# Path

## Path

```TypeScript
export declare function Path(
    options?: PathOptions
): PathAttribute
```

路径绘制组件，根据绘制路径生成封闭的自定义形状。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Path(    options?: PathOptions): PathAttribute--><!--Device-unnamed-export declare function Path(    options?: PathOptions): PathAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathOptions](../arkts-components/arkts-arkui-pathoptions-i.md) | No | Path绘制区域。 &lt;br&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |  |


## Path

```TypeScript
export declare function Path(
    style: CustomBuilderT<PathAttribute>,
): PathAttribute
```

Defines Path Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Path(    style: CustomBuilderT<PathAttribute>,): PathAttribute--><!--Device-unnamed-export declare function Path(    style: CustomBuilderT<PathAttribute>,): PathAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PathAttribute&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |  |

