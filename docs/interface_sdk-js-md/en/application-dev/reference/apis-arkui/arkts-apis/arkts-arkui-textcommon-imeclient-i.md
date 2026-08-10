# IMEClient

输入控件绑定输入法客户端类型。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare interface IMEClient--><!--Device-unnamed-export declare interface IMEClient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setExtraConfig

```TypeScript
setExtraConfig(config: InputMethodExtraConfig): void
```

设置输入法扩展信息。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMEClient-setExtraConfig(config: InputMethodExtraConfig): void--><!--Device-IMEClient-setExtraConfig(config: InputMethodExtraConfig): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [InputMethodExtraConfig](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md) | Yes | 输入法扩展信息。 |

## nodeId

```TypeScript
nodeId: long
```

当前输入控件的组件UniqueId。取值范围大于等于0。

**Type:** long

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMEClient-nodeId: long--><!--Device-IMEClient-nodeId: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

