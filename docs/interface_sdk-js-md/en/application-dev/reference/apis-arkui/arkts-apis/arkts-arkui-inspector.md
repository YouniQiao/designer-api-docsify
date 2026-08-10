# @ohos.arkui.inspector

提供注册组件布局和组件绘制送显完成回调通知的能力。

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
| [getInspectorByKey](arkts-arkui-inspector-getinspectorbykey-f.md#getinspectorbykey) | 获取指定id组件的所有属性，不包括子组件信息。  此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用。由于耗时长，不建议测试之外的场景使用。 |
| [getInspectorTree](arkts-arkui-inspector-getinspectortree-f.md#getinspectortree) | 获取组件树及组件属性。  此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。 |
| [sendEventByKey](arkts-arkui-inspector-sendeventbykey-f.md#sendeventbykey) | 给指定id的组件发送事件。  此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ComponentObserver](arkts-arkui-inspector-componentobserver-i.md) | 组件布局和组件绘制送显完成回调的句柄，通过该句柄可调用以下方法。 |

