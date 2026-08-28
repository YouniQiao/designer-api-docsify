# TouchOptions

Common options for touch operations.

**Since:** 26.0.0

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## Modules to Import

```TypeScript
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## duration

```TypeScript
duration?: number
```

Duration of the operation in milliseconds. Value range: The value should be &gt;= 1500 Unit: ms Default value: 1500

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## pressure

```TypeScript
pressure?: number
```

Pressure value of the touch. The value range is [0, 1]. The default value is **0**. If the value is **null** or **undefined**, the default value is used. If the value is out of the value range, the 17000007 error code is thrown.

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## speed

```TypeScript
speed?: number
```

Speed of touch action. Value range:[200, 40000] Unit: px/s. If the value is out of range or null/undefined, the default value 600 is used. Default value: 600

**Type:** number

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.
