# @ohos.arkui.uiExtension

用于[EmbeddedUIExtensionAbility](../../../application-models/embeddeduiextensionability.md)（或  
[UIExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)）中获取宿主应用的窗口信息或对应的  
[EmbeddedComponent](../../apis-arkui/arkts-components/arkts-arkui-embedded_component-i)&lt;!--Del--&gt;（或  
[UIExtensionComponent](../../apis-arkui/arkts-components/arkts-arkui-ui_extension_component-i)）&lt;!--DelEnd--&gt;组件的信息。

> **说明：**
> 
> 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiExtension--><!--Device-unnamed-declare namespace uiExtension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiExtension } from 'kits/@kit.ArkUI';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AvoidAreaInfo](arkts-arkui-uiextension-avoidareainfo-i.md) | 用于表示窗口避让区的信息。 |
| [RectChangeOptions](arkts-arkui-uiextension-rectchangeoptions-i.md) | 组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化返回的值及变化原因。 |
| [WindowProxy](arkts-arkui-uiextension-windowproxy-i.md) | UIExtension窗口代理。 |
| [WindowProxyProperties](arkts-arkui-uiextension-windowproxyproperties-i.md) | 用于表示组件的相关信息。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [WindowProxy](arkts-arkui-uiextension-windowproxy-i-sys.md) | UIExtension窗口代理。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [EventFlag](arkts-arkui-uiextension-eventflag-e.md) | 事件类型枚举。 |
| [RectChangeReason](arkts-arkui-uiextension-rectchangereason-e.md) | 组件（EmbeddedComponent或UIExtensionComponent）矩形（位置及尺寸）变化的原因。 |

