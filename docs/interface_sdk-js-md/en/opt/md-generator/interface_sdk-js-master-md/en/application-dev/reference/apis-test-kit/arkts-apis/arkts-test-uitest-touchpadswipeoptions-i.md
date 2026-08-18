# TouchPadSwipeOptions

Describes information about the touchpad swipe gesture option.

**Since:** 23

<!--Device-unnamed-declare interface TouchPadSwipeOptions--><!--Device-unnamed-declare interface TouchPadSwipeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
```

## speed

```TypeScript
speed?: number
```

Swipe speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 2000

**Type:** number

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TouchPadSwipeOptions-speed?: int--><!--Device-TouchPadSwipeOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## stay

```TypeScript
stay?: boolean
```

Whether the swipe gesture stays on the touchpad for 1s before it is lifted. The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite. <br>Default value: false

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TouchPadSwipeOptions-stay?: boolean--><!--Device-TouchPadSwipeOptions-stay?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest
