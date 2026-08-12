# ExtendableImage

Defines the Extendable Image.

**Inheritance/Implementation:** ExtendableImage implements [ImageAttribute](arkts-arkui-image-imageattribute-i.md#ImageAttribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableImage implements ImageAttribute--><!--Device-unnamed-export declare abstract class ExtendableImage implements ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions,
    reloadKey?: string
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    reloadKey?: string
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableImage>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>
  ): void
```

Entry of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void--><!--Device-ExtendableImage-static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |

## setImageOptions

```TypeScript
public setImageOptions(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
    imageAIOptions?: ImageAIOptions
  ): this
```

Set the Image Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setImageOptions

```TypeScript
public setImageOptions(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
    imageAIOptions?: ImageAIOptions,
    reloadKey?: string
  ): this
```

Set the Image Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setImageOptions

```TypeScript
public setImageOptions(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
    reloadKey?: string
  ): this
```

Set the Image Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

