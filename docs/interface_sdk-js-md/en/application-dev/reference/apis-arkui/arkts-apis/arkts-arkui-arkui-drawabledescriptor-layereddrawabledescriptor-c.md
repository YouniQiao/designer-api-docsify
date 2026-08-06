# LayeredDrawableDescriptor

Use the LayeredDrawableDescriptor class to get the foreground, the background and the mask DrawableDescriptor.

**Inheritance/Implementation:** LayeredDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LayeredDrawableDescriptor extends DrawableDescriptor--><!--Device-unnamed-export declare class LayeredDrawableDescriptor extends DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(
    foreground?: DrawableDescriptor,
    background?: DrawableDescriptor,
    mask?: DrawableDescriptor
  )
```

Creates a new LayeredDrawableDescriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-constructor(    foreground?: DrawableDescriptor,    background?: DrawableDescriptor,    mask?: DrawableDescriptor  )--><!--Device-LayeredDrawableDescriptor-constructor(    foreground?: DrawableDescriptor,    background?: DrawableDescriptor,    mask?: DrawableDescriptor  )-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| foreground | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the foreground option to create LayeredDrawableDescriptor. |
| background | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the background option to create LayeredDrawableDescriptor. |
| mask | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the mask option to create LayeredDrawableDescriptor. |

## getBackground

```TypeScript
getBackground(): DrawableDescriptor | undefined
```

Get DrawableDescriptor for the background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getBackground(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getBackground(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return the DrawableDescriptor object of background. |

## getForeground

```TypeScript
getForeground(): DrawableDescriptor | undefined
```

Get DrawableDescriptor for the foreground.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getForeground(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getForeground(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return the DrawableDescriptor object of foreground. |

## getMask

```TypeScript
getMask(): DrawableDescriptor | undefined
```

Get DrawableDescriptor for the mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getMask(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getMask(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return the DrawableDescriptor object of mask. |

## getMaskClipPath

```TypeScript
static getMaskClipPath(): string
```

Get the clip path info of the adaptive icon mask.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-static getMaskClipPath(): string--><!--Device-LayeredDrawableDescriptor-static getMaskClipPath(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the clip path info of mask. |

## setBlendMode

```TypeScript
setBlendMode(mode: drawing.BlendMode | undefined): void
```

Set the composition mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-setBlendMode(mode: drawing.BlendMode | undefined): void--><!--Device-LayeredDrawableDescriptor-setBlendMode(mode: drawing.BlendMode | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | drawing.BlendMode \| undefined | Yes | Indicates the composition mode to set. |

