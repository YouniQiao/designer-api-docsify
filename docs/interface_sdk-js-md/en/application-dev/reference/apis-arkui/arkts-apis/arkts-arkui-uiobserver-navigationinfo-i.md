# NavigationInfo

Provides information about the **Navigation** component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-uiObserver-export interface NavigationInfo--><!--Device-uiObserver-export interface NavigationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## navigationId

```TypeScript
navigationId: string
```

ID of the **Navigation** component.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationInfo-navigationId: string--><!--Device-NavigationInfo-navigationId: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pathStack

```TypeScript
pathStack: NavPathStack
```

Navigation controller of the **Navigation** component.

**Type:** NavPathStack

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationInfo-pathStack: NavPathStack--><!--Device-NavigationInfo-pathStack: NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uniqueId

```TypeScript
uniqueId?: number
```

Unique ID of the **Navigation** component, which can be obtained through queryNavigationInfo.

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-NavigationInfo-uniqueId?: number--><!--Device-NavigationInfo-uniqueId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

