# WindowInfo

Describes the window information.

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import floatingBall from '@kit.ArkUI.floatingBall';
import floatView from '@kit.ArkUI.floatView';
import window from '@kit.ArkUI';
```

## abilityName

```TypeScript
abilityName: string
```

abilityName of window

**Type:** string

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
displayId?: number
```

Indicates the ID of the display where the window is located.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

## globalDisplayRect

```TypeScript
globalDisplayRect?: Rect
```

Window size in the global coordinate system. In extended screen scenarios, the top-left corner of the primary screen is used as the coordinate origin. In virtual screen scenarios, the top-left corner of the virtual screen is used as the coordinate origin. The default value is [0, 0, 0, 0].

**Type:** Rect

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

## globalRect

```TypeScript
globalRect?: Rect
```

Indicates the actual display size and position of the window.

**Type:** Rect

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

## isFocused

```TypeScript
isFocused?: boolean
```

Whether the window gains focus. **true** if the window gains focus, **false** otherwise. The return value is the same as that of the [isFocused()](arkts-arkui-window-window-i.md#isfocused) API.

**Type:** boolean

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

**Examples**

```TypeScript
try {
  let focus = windowClass.isFocused();
  console.info(`Succeeded in checking whether the window is focused. Data: ${focus}`);
} catch (exception) {
  console.error(`Failed to check whether the window is focused. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

## rect

```TypeScript
rect: Rect
```

Window size.

**Type:** Rect

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

## windowId

```TypeScript
windowId: number
```

Window ID.

**Type:** number

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager

## windowStatusType

```TypeScript
windowStatusType: WindowStatusType
```

Window mode.

**Type:** WindowStatusType

**Since:** 18

**System capability:** SystemCapability.Window.SessionManager
