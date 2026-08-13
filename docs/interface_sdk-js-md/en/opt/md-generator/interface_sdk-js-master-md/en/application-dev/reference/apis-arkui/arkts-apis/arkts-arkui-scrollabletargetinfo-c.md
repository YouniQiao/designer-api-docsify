# ScrollableTargetInfo

Provides the information about the scrollable container component corresponding to the gesture recognizer. It inherits from [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md#EventTargetInfo).

**Inheritance/Implementation:** ScrollableTargetInfo extends [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md#EventTargetInfo)

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare class ScrollableTargetInfo--><!--Device-unnamed-declare class ScrollableTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isBegin

```TypeScript
isBegin(): boolean
```

Checks whether this scrollable container component is scrolled to the top. If it is a **Swiper** component in loop mode, **false** is returned.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableTargetInfo-isBegin(): boolean--><!--Device-ScrollableTargetInfo-isBegin(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEnd

```TypeScript
isEnd(): boolean
```

Checks whether the current scroll container is scrolled to the bottom. If the container is a **Swiper** component and is in loop mode, **false** is returned.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableTargetInfo-isEnd(): boolean--><!--Device-ScrollableTargetInfo-isEnd(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
