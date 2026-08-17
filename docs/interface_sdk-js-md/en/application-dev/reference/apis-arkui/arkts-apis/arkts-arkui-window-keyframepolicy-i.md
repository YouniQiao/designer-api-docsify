# KeyFramePolicy

Describes the configuration for keyframe policies.

**Since:** 23

<!--Device-window-interface KeyFramePolicy--><!--Device-window-interface KeyFramePolicy-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'window';
```

## animationDelay

```TypeScript
animationDelay?: long
```

Delay before the animation for keyframe layout changes starts, in ms. The default value is **100**. The value is **0** or a positive integer. Floating-point values are rounded down.

**Type:** long

**Default:** 100

**Since:** 23

<!--Device-KeyFramePolicy-animationDelay?: long--><!--Device-KeyFramePolicy-animationDelay?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## animationDuration

```TypeScript
animationDuration?: long
```

Duration of the animation for keyframe layout changes, in ms. The default value is **100**. The value is **0** or a positive integer. Floating-point values are rounded down.

**Type:** long

**Default:** 100

**Since:** 23

<!--Device-KeyFramePolicy-animationDuration?: long--><!--Device-KeyFramePolicy-animationDuration?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## distance

```TypeScript
distance?: int
```

Distance interval for triggering keyframe layout changes via dragging, in px. The default value is **1000**. The value is **0** or a positive integer. Floating-point values are rounded down. If the value is 0, the drag distance is ignored. It works with **interval** using an OR condition. If either of them is met, the layout change starts.

**Type:** int

**Default:** 1000

**Since:** 23

<!--Device-KeyFramePolicy-distance?: int--><!--Device-KeyFramePolicy-distance?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## enable

```TypeScript
enable: boolean
```

Whether to enable keyframes. **true** to enable, **false** otherwise.

**Type:** boolean

**Since:** 23

<!--Device-KeyFramePolicy-enable: boolean--><!--Device-KeyFramePolicy-enable: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## interval

```TypeScript
interval?: long
```

Time interval for triggering keyframe layout changes via dragging, in ms. The default value is **1000**. The value is a positive integer. Floating-point values are rounded down. It works with **distance** using an OR condition. If either of them is met, the layout change starts.

**Type:** long

**Default:** 1000

**Since:** 23

<!--Device-KeyFramePolicy-interval?: long--><!--Device-KeyFramePolicy-interval?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

