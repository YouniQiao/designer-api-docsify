# @ohos.arkui.inspector

Used to do observer layout and draw event for component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace inspector--><!--Device-unnamed-declare namespace inspector-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getInspectorByKey](arkts-arkui-inspector-getinspectorbykey-f.md#getinspectorbykey) | Obtains all attributes of the component with the specified ID. |
| [getInspectorTree](arkts-arkui-inspector-getinspectortree-f.md#getinspectortree) | Get components tree. |
| [sendEventByKey](arkts-arkui-inspector-sendeventbykey-f.md#sendeventbykey) | Sends an event to the component with the specified ID. |

### Interfaces

| Name | Description |
| --- | --- |
| [ComponentObserver](arkts-arkui-inspector-componentobserver-i.md) | The ComponentObserver is used to listen for layout, draw and drawChildren events. |

