# IMEClient

输入控件绑定输入法客户端类型。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface IMEClient--><!--Device-unnamed-declare interface IMEClient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setExtraConfig

```TypeScript
setExtraConfig(config: InputMethodExtraConfig): void
```

设置输入法扩展信息。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-IMEClient-setExtraConfig(config: InputMethodExtraConfig): void--><!--Device-IMEClient-setExtraConfig(config: InputMethodExtraConfig): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [InputMethodExtraConfig](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md) | Yes | 输入法扩展信息。 |

## nodeId

```TypeScript
nodeId: number
```

当前输入控件的组件UniqueId。取值范围大于等于0。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-IMEClient-nodeId: number--><!--Device-IMEClient-nodeId: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

