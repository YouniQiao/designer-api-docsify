# TextOverflowOptions

文本超长显示方式对象。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextOverflowOptions--><!--Device-unnamed-export declare interface TextOverflowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow: TextOverflow | undefined
```

文本超长时的显示方式。

默认值：TextOverflow.Clip

取值undefined时，按默认值处理。

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md) \| undefined

**Default:** TextOverflow.Clip

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextOverflowOptions-overflow: TextOverflow | undefined--><!--Device-TextOverflowOptions-overflow: TextOverflow | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

