# TouchPadEventContact

```TypeScript
declare interface TouchPadEventContact
```

Describes a contact in a raw touchpad event.

**Since:** 26.1.0

<!--Device-unnamed-declare interface TouchPadEventContact--><!--Device-unnamed-declare interface TouchPadEventContact-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: number
```

Unique identifier of the contact. The identifier remains unchanged from the beginning until the end or cancellation of the contact. The value should be an integer.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEventContact-id: int--><!--Device-TouchPadEventContact-id: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## phase

```TypeScript
phase: TouchPadEventPhase
```

Phase of the contact.

**Type:** [TouchPadEventPhase](../arkts-apis/arkts-arkui-touchpadeventphase-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEventContact-phase: TouchPadEventPhase--><!--Device-TouchPadEventContact-phase: TouchPadEventPhase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## positionX

```TypeScript
positionX: number
```

X coordinate of the contact normalized to the logical coordinate range of the touchpad. Value range: [0,1].

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEventContact-positionX: double--><!--Device-TouchPadEventContact-positionX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## positionY

```TypeScript
positionY: number
```

Y coordinate of the contact normalized to the logical coordinate range of the touchpad. Value range: [0,1].

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-TouchPadEventContact-positionY: double--><!--Device-TouchPadEventContact-positionY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
