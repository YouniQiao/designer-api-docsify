# TouchPadSwipeOptions

Describes information about the touchpad swipe gesture option.

**Since:** 18

**System capability:** SystemCapability.Test.UiTest

**Test API:** This API is used only in automated test scripts.

## Modules to Import

```TypeScript
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## speed

```TypeScript
speed?: number
```

Swipe speed. Value range:[200, 40000] Unit: px/s. Throws error code 17000007 if negative. Default value: 2000

**Type:** number

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This API is used only in automated test scripts.

## stay

```TypeScript
stay?: boolean
```

Whether the swipe gesture stays on the touchpad for 1s before it is lifted. The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite. Default value: false

**Type:** boolean

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This API is used only in automated test scripts.
