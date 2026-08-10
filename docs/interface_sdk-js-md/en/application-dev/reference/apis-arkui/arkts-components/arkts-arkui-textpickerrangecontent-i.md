# TextPickerRangeContent

单列数据选择器的数据选项内容。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface TextPickerRangeContent--><!--Device-unnamed-declare interface TextPickerRangeContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon: string | Resource
```

图片资源。当icon为string类型时，表示图片存放的路径，例如"/common/hello.png"；当icon为Resource类型时，表示资源引用。

**Type:** string \| Resource

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerRangeContent-icon: string | Resource--><!--Device-TextPickerRangeContent-icon: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: string | Resource
```

文本信息。

> 默认值：空字符串

> **说明：**
> 
> 1. 未设置该属性时，使用默认值。
> 2. 当文本长度大于列宽时，文本被截断。

**Type:** string \| Resource

**Default:** ""

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerRangeContent-text?: string | Resource--><!--Device-TextPickerRangeContent-text?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

