# Progress

## Progress

```TypeScript
export declare function Progress(
    options: ProgressOptions
): ProgressAttribute
```

创建进度条组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Progress(    options: ProgressOptions): ProgressAttribute--><!--Device-unnamed-export declare function Progress(    options: ProgressOptions): ProgressAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ProgressOptions](../arkts-components/arkts-arkui-progressoptions-i.md) | Yes | 按进度条类型不同，设置不同属性的进度条组件参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |  |


## Progress

```TypeScript
export declare function Progress(
    style: CustomBuilderT<ProgressAttribute>,
): ProgressAttribute
```

定义Progress组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Progress(    style: CustomBuilderT<ProgressAttribute>,): ProgressAttribute--><!--Device-unnamed-export declare function Progress(    style: CustomBuilderT<ProgressAttribute>,): ProgressAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ProgressAttribute&gt; | Yes | Progress属性实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |  |

