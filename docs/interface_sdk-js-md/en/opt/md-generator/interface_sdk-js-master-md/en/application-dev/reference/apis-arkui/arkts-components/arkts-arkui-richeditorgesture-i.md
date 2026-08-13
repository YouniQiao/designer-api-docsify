# RichEditorGesture

User gesture event.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-declare interface RichEditorGesture--><!--Device-unnamed-declare interface RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick?: Callback<ClickEvent>
```

Triggered when [ClickEvent](arkts-arkui-clickevent-i.md#ClickEvent) occurs. It is executed on completion of a single click. On a double-click, the first click triggers the callback event.

**Type:** Callback&lt;[ClickEvent](arkts-arkui-clickevent-i.md)&gt;

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorGesture-onClick?: Callback<ClickEvent>--><!--Device-RichEditorGesture-onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLongPress

```TypeScript
onLongPress?: Callback<GestureEvent>
```

Triggered when the user performs a long press. It is executed on completion of a long press.

**Type:** Callback&lt;[GestureEvent](../arkts-apis/arkts-arkui-gestureevent-i.md)&gt;

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorGesture-onLongPress?: Callback<GestureEvent>--><!--Device-RichEditorGesture-onLongPress?: Callback<GestureEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
