# AccessibilityNextFocusParams

定义无障碍自定义下一个焦点处理过程中可使用的详细参数对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface AccessibilityNextFocusParams--><!--Device-unnamed-export declare interface AccessibilityNextFocusParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isConsiderDescendants

```TypeScript
isConsiderDescendants?: boolean
```

是否在无障碍自定义下一个焦点处理过程中查找后代节点中的焦点。

true表示在无障碍自定义下一个焦点处理过程中查找后代节点中的焦点；false表示在无障碍自定义下一个焦点处理过程中不查找后代节点中的焦点。

默认值：false

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityNextFocusParams-isConsiderDescendants?: boolean--><!--Device-AccessibilityNextFocusParams-isConsiderDescendants?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

