# PasteButton properties/events

不支持通用属性，仅继承[安全控件通用属性](./security_component)。

不支持通用事件，仅支持以下事件。

**Inheritance/Implementation:** PasteButtonAttribute extends [SecurityComponentMethod<PasteButtonAttribute>](SecurityComponentMethod<PasteButtonAttribute>)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class PasteButtonAttribute extends SecurityComponentMethod<PasteButtonAttribute>--><!--Device-unnamed-declare class PasteButtonAttribute extends SecurityComponentMethod<PasteButtonAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback)
```

点击粘贴控件触发该回调，回调返回授权结果。授权成功后应用可临时获取读取剪贴板权限。

> **说明：**
> - 为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../../../security/AccessToken/security-component-overview.md#约束与限制)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback): PasteButtonAttribute--><!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md) | Yes | 点击事件的回调函数，用于处理粘贴控件点击后的授权结果。 &lt;br&gt;从API version 18开始，统一使用[PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md)，可额外获取error信息。<br>**Since:** 18 |

