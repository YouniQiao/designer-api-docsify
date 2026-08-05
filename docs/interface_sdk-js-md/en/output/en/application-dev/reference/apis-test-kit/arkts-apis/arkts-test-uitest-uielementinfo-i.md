# UIElementInfo

Provides information about the UI event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface UIElementInfo--><!--Device-unnamed-declare interface UIElementInfo-End-->

**System capability:** SystemCapability.Test.UiTest

## bundleName

```TypeScript
readonly bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly bundleName: string--><!--Device-UIElementInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.Test.UiTest

## componentEventType

```TypeScript
readonly componentEventType?: ComponentEventType
```

Component operation event type. If it is not a component operation event, \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is returned.

**Type:** ComponentEventType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIElementInfo-readonly componentEventType?: ComponentEventType--><!--Device-UIElementInfo-readonly componentEventType?: ComponentEventType-End-->

**System capability:** SystemCapability.Test.UiTest

## componentId

```TypeScript
readonly componentId?: string
```

Component ID. If it is not a component operation event, an empty string is returned.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIElementInfo-readonly componentId?: string--><!--Device-UIElementInfo-readonly componentId?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## componentRect

```TypeScript
readonly componentRect?: Rect
```

The rect of the component, set all attributes of rect to 0 if it's a window.

**Type:** Rect

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIElementInfo-readonly componentRect?: Rect--><!--Device-UIElementInfo-readonly componentRect?: Rect-End-->

**System capability:** SystemCapability.Test.UiTest

## text

```TypeScript
readonly text: string
```

Text information of the component or window.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly text: string--><!--Device-UIElementInfo-readonly text: string-End-->

**System capability:** SystemCapability.Test.UiTest

## type

```TypeScript
readonly type: string
```

Component or window type.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIElementInfo-readonly type: string--><!--Device-UIElementInfo-readonly type: string-End-->

**System capability:** SystemCapability.Test.UiTest

## windowChangeType

```TypeScript
readonly windowChangeType?: WindowChangeType
```

Window change event type. If the event is not a window change event, \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is returned.

**Type:** WindowChangeType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIElementInfo-readonly windowChangeType?: WindowChangeType--><!--Device-UIElementInfo-readonly windowChangeType?: WindowChangeType-End-->

**System capability:** SystemCapability.Test.UiTest

## windowId

```TypeScript
readonly windowId?: int
```

ID of the window where the component belongs.

**Type:** int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIElementInfo-readonly windowId?: int--><!--Device-UIElementInfo-readonly windowId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

