# @ohos.graphics.displaySync(Variable Frame Rate)

Variable frame rate support allows developers to run UI services at a specified frame rate. It is generally used in scenarios where developers draw the UI themselves and have specific requirements for the frame rate. The system adjusts the drawing frequency based on the set expected frame rate, minimum frame rate, and maximum frame rate to meet the requirements of different scenarios.

**Since:** 11

<!--Device-unnamed-declare namespace displaySync--><!--Device-unnamed-declare namespace displaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [create](arkts-arkgraphics2d-displaysync-create-f.md#create-1) | Creates a DisplaySync object, through which you can set the frame rate of the custom UI content. |

### Interfaces

| Name | Description |
| --- | --- |
| [DisplaySync](arkts-arkgraphics2d-displaysync-displaysync-i.md) | An instance for setting the expected frame rate and callback function. It is used to set the expected frame rate range, register the frame callback function, and start and stop the frame callback. Before calling any of the following APIs, you must use displaySync.create() to create a DisplaySync instance and then call the corresponding method through this instance. |
| [IntervalInfo](arkts-arkgraphics2d-displaysync-intervalinfo-i.md) | Developers can obtain the timestamp information of frame drawing from the callback function, including the timestamp when the current frame arrives and the targetTimestamp when the next frame is expected to arrive. |
