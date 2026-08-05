# WindowInfo

Describes the window information.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-window-interface WindowInfo--><!--Device-window-interface WindowInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## abilityName

```TypeScript
abilityName: string
```

abilityName of window

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WindowInfo-abilityName: string--><!--Device-WindowInfo-abilityName: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WindowInfo-bundleName: string--><!--Device-WindowInfo-bundleName: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
displayId?: int
```

Indicates the ID of the display where the window is located.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowInfo-displayId?: int--><!--Device-WindowInfo-displayId?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## globalDisplayRect

```TypeScript
globalDisplayRect?: Rect
```

Window size in the global coordinate system. In extended screen scenarios, the top-left corner of the primary screen is used as the coordinate origin. In virtual screen scenarios, the top-left corner of the virtual screen is used as the coordinate origin. The default value is [0, 0, 0, 0].

**Type:** Rect

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WindowInfo-globalDisplayRect?: Rect--><!--Device-WindowInfo-globalDisplayRect?: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## globalRect

```TypeScript
globalRect?: Rect
```

Indicates the actual display size and position of the window.

**Type:** Rect

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowInfo-globalRect?: Rect--><!--Device-WindowInfo-globalRect?: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## isFocused

```TypeScript
isFocused?: boolean
```

Whether the window gains focus. **true** if the window gains focus, **false** otherwise. The return value is the same as that of the [isFocused()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-WindowInfo-isFocused?: boolean--><!--Device-WindowInfo-isFocused?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## rect

```TypeScript
rect: Rect
```

Window size.

**Type:** Rect

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WindowInfo-rect: Rect--><!--Device-WindowInfo-rect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowId

```TypeScript
windowId: int
```

Window ID.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WindowInfo-windowId: int--><!--Device-WindowInfo-windowId: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowStatusType

```TypeScript
windowStatusType: WindowStatusType
```

Window mode.

**Type:** WindowStatusType

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WindowInfo-windowStatusType: WindowStatusType--><!--Device-WindowInfo-windowStatusType: WindowStatusType-End-->

**System capability:** SystemCapability.Window.SessionManager

