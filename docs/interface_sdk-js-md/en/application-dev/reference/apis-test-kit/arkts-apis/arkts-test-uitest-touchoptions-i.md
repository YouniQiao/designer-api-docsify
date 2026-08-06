# TouchOptions

Common options for touch operations.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-declare interface TouchOptions--><!--Device-unnamed-declare interface TouchOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## duration

```TypeScript
duration?: int
```

Duration of the operation in milliseconds.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range: The value should be >= 1500\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Unit: ms\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Default value: 1500

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-duration?: int--><!--Device-TouchOptions-duration?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## pressure

```TypeScript
pressure?: double
```

The pressure of the touch.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range:[0.0, 1.0]\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: 1.0

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-pressure?: double--><!--Device-TouchOptions-pressure?: double-End-->

**System capability:** SystemCapability.Test.UiTest

## speed

```TypeScript
speed?: int
```

Speed of touch action.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range:[200, 40000]\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Unit: px/s.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Throws error code 17000007 if negative.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Default value: 600

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TouchOptions-speed?: int--><!--Device-TouchOptions-speed?: int-End-->

**System capability:** SystemCapability.Test.UiTest

