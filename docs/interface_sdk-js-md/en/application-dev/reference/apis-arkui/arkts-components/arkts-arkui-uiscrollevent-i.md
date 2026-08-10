# UIScrollEvent

frameNode中[getEvent('Scroll')](../arkts-apis/arkts-arkui-typenode-getevent-f.md/arkts-arkui-typenode-getevent-f.md#getevent)方法的返回值，可用于给Scroll节点设置滚动事件。

UIScrollEvent继承于[UIScrollableCommonEvent](../arkts-apis/arkts-arkui-common-uiscrollablecommonevent-i.md/arkts-arkui-common-uiscrollablecommonevent-i.md)。

**Inheritance/Implementation:** UIScrollEvent extends [UIScrollableCommonEvent](../arkts-apis/arkts-arkui-common-uiscrollablecommonevent-i.md/arkts-arkui-common-uiscrollablecommonevent-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-unnamed-declare interface UIScrollEvent extends UIScrollableCommonEvent--><!--Device-unnamed-declare interface UIScrollEvent extends UIScrollableCommonEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnDidScroll

```TypeScript
setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void
```

[onDidScroll](ScrollAttribute#onDidScroll)事件的回调。

方法入参为undefined时，会重置事件回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIScrollEvent-setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void--><!--Device-UIScrollEvent-setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) \| undefined | Yes | onDidScroll事件的回调函数。 |

## setOnWillScroll

```TypeScript
setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void
```

[onWillScroll](ScrollAttribute#onWillScroll)事件的回调。

方法入参为undefined时，会重置事件回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIScrollEvent-setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void--><!--Device-UIScrollEvent-setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ScrollOnWillScrollCallback](../arkts-apis/arkts-arkui-scrollonwillscrollcallback-t.md) \| undefined | Yes | onWillScroll事件的回调函数。 |

