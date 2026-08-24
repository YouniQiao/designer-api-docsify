# EditableLeftIconV2

Declaration of the left icon configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class EditableLeftIconV2--><!--Device-unnamed-export declare class EditableLeftIconV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: EditableLeftIconV2Options)
```

Constructor of EditableLeftIconV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableLeftIconV2-constructor(options?: EditableLeftIconV2Options)--><!--Device-EditableLeftIconV2-constructor(options?: EditableLeftIconV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableLeftIconV2Options](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-editabletitlebarv2-editablelefticonv2options-i.md) | No | The options of the left icon |

## defaultFocus

```TypeScript
public defaultFocus: boolean
```

Whether to get focus by default.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableLeftIconV2-@Trace  public defaultFocus: boolean--><!--Device-EditableLeftIconV2-@Trace  public defaultFocus: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconType

```TypeScript
public iconType: EditableLeftIconTypeV2
```

Icon type, Back or Cancel.

**Type:** [EditableLeftIconTypeV2](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-editabletitlebarv2-editablelefticontypev2-e.md)

**Default:** EditableLeftIconTypeV2.Back

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableLeftIconV2-@Trace  public iconType: EditableLeftIconTypeV2--><!--Device-EditableLeftIconV2-@Trace  public iconType: EditableLeftIconTypeV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
public onAction?: OnActionCallback
```

Callback function when click on the left icon.

**Type:** [OnActionCallback](../../apis-arkui/arkts-apis/arkts-arkui-onactioncallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableLeftIconV2-@Trace  public onAction?: OnActionCallback--><!--Device-EditableLeftIconV2-@Trace  public onAction?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

