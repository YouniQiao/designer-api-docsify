# TouchPadSwipeOptions

Describes information about the touchpad swipe gesture option.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface TouchPadSwipeOptions--><!--Device-unnamed-declare interface TouchPadSwipeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## speed

```TypeScript
speed?: int
```

Swipe speed.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range:[200, 40000]\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Unit: px/s.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Throws error code 17000007 if negative.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Default value: 2000

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TouchPadSwipeOptions-speed?: int--><!--Device-TouchPadSwipeOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## stay

```TypeScript
stay?: boolean
```

Whether the swipe gesture stays on the touchpad for 1s before it is lifted.The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: false

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TouchPadSwipeOptions-stay?: boolean--><!--Device-TouchPadSwipeOptions-stay?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

