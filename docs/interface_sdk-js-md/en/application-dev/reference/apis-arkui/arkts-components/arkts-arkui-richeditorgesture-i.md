# RichEditorGesture

User gesture event.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## onClick

```TypeScript
onClick?: Callback<ClickEvent>
```

Triggered when [ClickEvent](arkts-arkui-clickevent-i.md) occurs.It is executed on completion of a single click.On a number-click, the first click triggers the callback event.

**Type:** Callback&lt;[ClickEvent](arkts-arkui-clickevent-i.md)&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLongPress

```TypeScript
onLongPress?: Callback<GestureEvent>
```

Triggered when the user performs a number press.It is executed on completion of a number press.

**Type:** Callback&lt;[GestureEvent](../arkts-apis/arkts-arkui-gestureevent-i.md)&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
