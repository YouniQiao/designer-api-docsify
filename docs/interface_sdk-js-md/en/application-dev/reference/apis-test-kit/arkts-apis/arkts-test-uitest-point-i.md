# Point

Represents the point on the device screen.

**Since:** 9

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## Modules to Import

```TypeScript
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## displayId

```TypeScript
displayId?: number
```

ID of the display to which the coordinate point belongs. The default value is the default screen ID of the device.

**Type:** number

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## x

```TypeScript
x: number
```

Horizontal coordinate of a coordinate point, in pixels. The value is an integer greater than or equal to 0.

@readonly [since 9-19]

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## y

```TypeScript
y: number
```

Vertical coordinate of a coordinate point, in pixels. The value is an integer greater than or equal to 0.

@readonly [since 9-19]

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.
