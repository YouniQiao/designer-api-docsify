# UIElementInfo

Provides information about the UI event.

**Since:** 10

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## Modules to Import

```TypeScript
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## bundleName

```TypeScript
readonly bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## componentEventType

```TypeScript
readonly componentEventType?: ComponentEventType
```

Component operation event type. If it is not a component operation event, [COMPONENT_UNDEFINED](arkts-test-uitest-componenteventtype-e.md#component_undefined) is returned.

**Type:** [ComponentEventType](arkts-test-uitest-componenteventtype-e.md)

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## componentId

```TypeScript
readonly componentId?: string
```

Component ID. If it is not a component operation event, an empty string is returned.

**Type:** string

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## componentRect

```TypeScript
readonly componentRect?: Rect
```

Component border information. If it is not a component operation event, a [Rect](arkts-test-uitest-rect-i.md) object whose attribute values are all **0** is returned.

**Type:** [Rect](arkts-test-uitest-rect-i.md)

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## text

```TypeScript
readonly text: string
```

Text information of the component or window.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // Use the static constructor ON to create an On object and specify the text attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // Use the static constructor BY to create a By object and specify the text attribute of the target component.
```

## type

```TypeScript
readonly type: string
```

Component or window type.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

**Examples**

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // Use the static constructor BY to create a By object and specify the type attribute of the target component.
```

## windowChangeType

```TypeScript
readonly windowChangeType?: WindowChangeType
```

Window change event type. If the event is not a window change event, [WINDOW_UNDEFINED](arkts-test-uitest-windowchangetype-e.md#window_undefined) is returned.

**Type:** [WindowChangeType](arkts-test-uitest-windowchangetype-e.md)

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.

## windowId

```TypeScript
readonly windowId?: number
```

ID of the window to which the component belongs. If it is not a component operation event, **-1** is returned.

**Type:** number

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Test API:** This is a test API.
