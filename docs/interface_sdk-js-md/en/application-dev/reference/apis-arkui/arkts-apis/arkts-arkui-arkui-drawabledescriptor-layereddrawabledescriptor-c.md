# LayeredDrawableDescriptor

Creates a **LayeredDrawableDescriptor** object when the passed resource ID or name belongs to a JSON file that contains foreground and background resources. Inherits from [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md).The **drawable.json** file is located under **entry/src/main/resources/base/media** in the project directory. Below shows the file content:

**Inheritance/Implementation:** LayeredDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(
    foreground?: DrawableDescriptor,
    background?: DrawableDescriptor,
    mask?: DrawableDescriptor
  )
```

A constructor used to create a **LayeredDrawableDescriptor** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| foreground | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No |
| background | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No |
| mask | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No |

## getBackground

```TypeScript
getBackground(): DrawableDescriptor
```

Obtains the **DrawableDescriptor** object of the background.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

## getForeground

```TypeScript
getForeground(): DrawableDescriptor
```

Obtains the **DrawableDescriptor** object of the foreground.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

## getMask

```TypeScript
getMask(): DrawableDescriptor
```

Obtains the **DrawableDescriptor** object of the mask.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

## getMaskClipPath

```TypeScript
static getMaskClipPath(): string
```

Obtains the built-in clipping path parameters of the system. It is a static method of **LayeredDrawableDescriptor**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setBlendMode

```TypeScript
setBlendMode(mode: drawing.BlendMode): void
```

Sets the blend mode of **LayeredDrawableDescriptor**. If this API is called for multiple times on the same **LayeredDrawableDescriptor** object, only the last call before the drawing completion takes effect. This API does not support dynamic switching. The default drawing order of **LayeredDrawableDescriptor** is background, mask, and foreground. After the blend mode is set, the drawing order changes to background, foreground, and mask. If the specified value is invalid, the default drawing order is used.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | drawing.BlendMode | Yes |
