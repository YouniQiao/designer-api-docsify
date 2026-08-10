# TextController

Text组件的控制器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextController--><!--Device-unnamed-export declare class TextController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

关闭自定义选择菜单或系统默认选择菜单。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-closeSelectionMenu(): void--><!--Device-TextController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager | undefined
```

获取布局管理器对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-getLayoutManager(): LayoutManager | undefined--><!--Device-TextController-getLayoutManager(): LayoutManager | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LayoutManager](arkts-arkui-layoutmanager-i.md) | 布局管理器对象。 |

## setStyledString

```TypeScript
setStyledString(value: StyledString): void
```

触发绑定或更新属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setStyledString(value: StyledString): void--><!--Device-TextController-setStyledString(value: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [StyledString](arkts-arkui-styledstring-c.md) | Yes |  |

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void
```

设置文本选择区域并高亮显示。

> **说明：**
> 
> 当[copyOption](copyOption)设置为CopyOptions.None时，设置setTextSelection不生效。
> 
> 当[textOverflow](arkts-arkui-enums-textoverflow-e.md)设置为TextOverflow.MARQUEE时，设置setTextSelection不生效。
> 
> 当selectionStart大于等于selectionEnd时不选中。可选范围为[0, textSize]，其中textSize为文本内容最大字符数，入参小于0时处理为0，大于textSize时处理为textSize。
> 
> 当selectionStart或selectionEnd位于截断的不可见区域时，文本不选中。截断为false时，超出父组件的文本选中区域生效。
> 
> 如果设备为PC/2in1，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。
> 
> 当emoji表情被选中区域截断时，若表情的起始位置包含在设置的文本选中区域内，该表情就会被选中。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void--><!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int \| undefined | Yes | 文本选择区域起始位置。&lt;br /&gt;取值范围：[0, +∞），值为负数或undefined时按0处理。 |
| selectionEnd | int \| undefined | Yes | 文本选择区域结束位置。&lt;br /&gt;取值范围：[0, +∞），值为负数或undefined时按0处理。 |
| options | [SelectionOptions](../arkts-components/arkts-arkui-selectionoptions-i.md) | No | 选中文字时的配置。&lt;br /&gt;默认值：SelectionOptions中MenuPolicy.DEFAULT |

