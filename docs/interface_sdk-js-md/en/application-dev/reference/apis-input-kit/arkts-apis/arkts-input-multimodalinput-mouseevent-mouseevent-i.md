# MouseEvent

鼠标事件。

**Inheritance/Implementation:** MouseEvent extends [InputEvent](arkts-input-multimodalinput-inputevent-inputevent-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface MouseEvent extends InputEvent--><!--Device-unnamed-export declare interface MouseEvent extends InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { MouseAction, AxisValue, MouseEvent, Button, MouseToolType, Axis } from 'kits/@kit.InputKit';
```

## action

```TypeScript
action: Action
```

鼠标事件类型。

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-action: Action--><!--Device-MouseEvent-action: Action-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## altKey

```TypeScript
altKey: boolean
```

当前altKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-altKey: boolean--><!--Device-MouseEvent-altKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## axes

```TypeScript
axes: AxisValue[]
```

鼠标轴类型和轴的值。

**Type:** [AxisValue](arkts-input-multimodalinput-mouseevent-axisvalue-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-axes: AxisValue[]--><!--Device-MouseEvent-axes: AxisValue[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## button

```TypeScript
button: Button
```

鼠标按键。

**Type:** [Button](arkts-input-multimodalinput-mouseevent-button-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-button: Button--><!--Device-MouseEvent-button: Button-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## capsLock

```TypeScript
capsLock: boolean
```

当前capsLock是否处于使能状态。 

true表示使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-capsLock: boolean--><!--Device-MouseEvent-capsLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## ctrlKey

```TypeScript
ctrlKey: boolean
```

当前ctrlKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-ctrlKey: boolean--><!--Device-MouseEvent-ctrlKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## fnKey

```TypeScript
fnKey: boolean
```

当前fnKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-fnKey: boolean--><!--Device-MouseEvent-fnKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## globalX

```TypeScript
globalX?: int
```

该鼠标事件以主屏左上角为原点的全局坐标系的X坐标，单位为像素（px）。&lt;!--Del--&gt;作为入参时，若接口参数中的  
[MouseEventData.useGlobalCoordinate](arkts-input-inputeventclient-mouseeventdata-i.md)为true，该值必填，当前仅支持整数。若为false，该值无需填写，使用指定屏幕左上角为原点的相对坐标系的X坐标计算注入事件。&lt;!--DelEnd--&gt;作为出参时，由系统上报。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MouseEvent-globalX?: int--><!--Device-MouseEvent-globalX?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## globalY

```TypeScript
globalY?: int
```

该鼠标事件以主屏左上角为原点的全局坐标系的Y坐标，单位为像素（px）。&lt;!--Del--&gt;作为入参时，若接口参数中的  
[MouseEventData.useGlobalCoordinate](arkts-input-inputeventclient-mouseeventdata-i.md)为true，该值必填，当前仅支持整数。若为false，该值无需填写，使用指定屏幕左上角为原点的相对坐标系的Y坐标计算注入事件。&lt;!--DelEnd--&gt;作为出参时，由系统上报。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MouseEvent-globalY?: int--><!--Device-MouseEvent-globalY?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## logoKey

```TypeScript
logoKey: boolean
```

当前logoKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-logoKey: boolean--><!--Device-MouseEvent-logoKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## numLock

```TypeScript
numLock: boolean
```

当前numLock是否处于使能状态。 

true表示使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-numLock: boolean--><!--Device-MouseEvent-numLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## pressedButtons

```TypeScript
pressedButtons: Button[]
```

当前处于按下状态的鼠标按键。

**Type:** [Button](arkts-input-multimodalinput-mouseevent-button-e.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-pressedButtons: Button[]--><!--Device-MouseEvent-pressedButtons: Button[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## pressedKeys

```TypeScript
pressedKeys: KeyCode[]
```

当前处于按下状态的键值列表。

**Type:** [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-pressedKeys: KeyCode[]--><!--Device-MouseEvent-pressedKeys: KeyCode[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## rawDeltaX

```TypeScript
rawDeltaX: int
```

鼠标当前事件相对于上次事件的X坐标偏移值。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-rawDeltaX: int--><!--Device-MouseEvent-rawDeltaX: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## rawDeltaY

```TypeScript
rawDeltaY: int
```

鼠标当前事件相对于上次事件的Y坐标偏移值。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-rawDeltaY: int--><!--Device-MouseEvent-rawDeltaY: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## screenX

```TypeScript
screenX: int
```

该鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-screenX: int--><!--Device-MouseEvent-screenX: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## screenY

```TypeScript
screenY: int
```

该鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-screenY: int--><!--Device-MouseEvent-screenY: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## scrollLock

```TypeScript
scrollLock: boolean
```

当前scrollLock是否处于使能状态。 

true表示使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-scrollLock: boolean--><!--Device-MouseEvent-scrollLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## shiftKey

```TypeScript
shiftKey: boolean
```

当前shiftKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-shiftKey: boolean--><!--Device-MouseEvent-shiftKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## toolType

```TypeScript
toolType: ToolType
```

工具类型。

**Type:** [ToolType](arkts-input-multimodalinput-touchevent-tooltype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-MouseEvent-toolType: ToolType--><!--Device-MouseEvent-toolType: ToolType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## windowX

```TypeScript
windowX: int
```

鼠标所在窗口左上角为原点的相对坐标系的X坐标。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-windowX: int--><!--Device-MouseEvent-windowX: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## windowY

```TypeScript
windowY: int
```

鼠标所在窗口左上角为原点的相对坐标系的Y坐标。当前仅支持整数，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MouseEvent-windowY: int--><!--Device-MouseEvent-windowY: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

