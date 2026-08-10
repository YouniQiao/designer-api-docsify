# StyledStringController

定义StyledString控制器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface StyledStringController--><!--Device-unnamed-export declare interface StyledStringController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getStyledString

```TypeScript
getStyledString(): MutableStyledString | undefined
```

ArkTS-Sta: getStyledString(): MutableStyledString | undefined

获取富文本组件显示的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledStringController-getStyledString(): MutableStyledString | undefined--><!--Device-StyledStringController-getStyledString(): MutableStyledString | undefined-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [MutableStyledString](arkts-arkui-mutablestyledstring-c.md) | 富文本组件显示的属性字符串。 |

## setStyledString

```TypeScript
setStyledString(styledString: StyledString): void
```

设置富文本组件显示的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledStringController-setStyledString(styledString: StyledString): void--><!--Device-StyledStringController-setStyledString(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c.md) | Yes | 属性字符串。&lt;br/&gt;**说明：** &lt;br/&gt;StyledString的子类 [MutableStyledString](../../../reference/apis-arkui/arkui-ts/ts-universal-styled-string.md#mutablestyledstring) 也可以作为入参值。 |

