# WindowChangeOptions

Describes the extended configuration of window change event listening, which is used to specify the listening process configuration and event filtering conditions.

**Since:** 22

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the window to be listened for. By default, all windows are listened for.

**Type:** string

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: number
```

Listening timeout interval, in milliseconds. The value is an integer greater than or equal to 500. The default value is **10000**. If the value is out of range, an error code is thrown.

**Type:** number

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest
