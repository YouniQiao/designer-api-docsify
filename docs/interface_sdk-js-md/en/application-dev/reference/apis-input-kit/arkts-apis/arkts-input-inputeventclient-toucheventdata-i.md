# TouchEventData

触屏注入描述信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-inputEventClient-interface TouchEventData--><!--Device-inputEventClient-interface TouchEventData-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## touchEvent

```TypeScript
touchEvent: TouchEvent
```

触屏输入事件。

**Type:** [TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-TouchEventData-touchEvent: TouchEvent--><!--Device-TouchEventData-touchEvent: TouchEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

## useGlobalCoordinate

```TypeScript
useGlobalCoordinate?: boolean
```

是否使用全局坐标来计算注入的触屏输入事件。默认值为false，取值为false表示使用以指定屏幕左上角为原点的相对坐标系的坐标来计算注入的触屏输入事件。取值为true表示使用以主屏左上角为原点的全局坐标系的坐标来计算注入的触屏输入事件。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TouchEventData-useGlobalCoordinate?: boolean--><!--Device-TouchEventData-useGlobalCoordinate?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

