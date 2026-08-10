# ActionSheet

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 26.0.0

**Substitutes:** ohos.arkui.UIContext.UIContext#showActionSheet

<!--Device-unnamed-declare class ActionSheet--><!--Device-unnamed-declare class ActionSheet-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(value: ActionSheetOptions)
```

定义列表弹窗并弹出。

> **说明：**

showActionSheet需先获取[UIContext](arkts-arkui-uicontext.md)实例后再进行调用。

> 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [showActionSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#showactionsheet)来明确UI的执行上下文。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#showActionSheet

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ActionSheet-static show(value: ActionSheetOptions)--><!--Device-ActionSheet-static show(value: ActionSheetOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ActionSheetOptions](arkts-arkui-actionsheet-actionsheetoptions-i.md) | Yes | 配置列表选择弹窗的参数。 |

