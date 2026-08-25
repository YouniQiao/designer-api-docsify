# IMEClient

Defines the input method client type bound to an input component.

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## setExtraConfig

```TypeScript
setExtraConfig(config: InputMethodExtraConfig): void
```

Sets the extension configuration of an input method.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [InputMethodExtraConfig](arkts-arkui-inputmethodextraconfig-t.md) | Yes |

## nodeId

```TypeScript
nodeId: number
```

Unique ID of the current input component. The value must be greater than or equal to 0.

**Type:** number

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
