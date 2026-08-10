# ScrollableTargetInfo

手势识别器对应的滚动类容器组件的信息，继承于[EventTargetInfo](arkts-arkui-eventtargetinfo-c.md)。

**Inheritance/Implementation:** ScrollableTargetInfo extends [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class ScrollableTargetInfo extends EventTargetInfo--><!--Device-unnamed-declare class ScrollableTargetInfo extends EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isBegin

```TypeScript
isBegin(): boolean
```

返回当前滚动类容器组件是否在顶部，如果为Swiper组件且在循环模式下返回false。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableTargetInfo-isBegin(): boolean--><!--Device-ScrollableTargetInfo-isBegin(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前滚动类容器组件是否在顶部。true表示组件在顶部，false表示组件不在顶部。 |

## isEnd

```TypeScript
isEnd(): boolean
```

返回当前滚动类容器组件是否在底部，如果为Swiper组件且在循环模式下返回false。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableTargetInfo-isEnd(): boolean--><!--Device-ScrollableTargetInfo-isEnd(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前滚动类容器组件是否在底部。true表示组件在底部，false表示组件不在底部。 |

