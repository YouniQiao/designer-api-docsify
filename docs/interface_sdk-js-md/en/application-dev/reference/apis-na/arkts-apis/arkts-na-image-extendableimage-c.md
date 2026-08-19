# ExtendableImage

Defines the Extendable Image.

**Inheritance/Implementation:** ExtendableImage implements ImageAttribute

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableImage--><!--Device-unnamed-export declare abstract class ExtendableImage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T--><!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-na-imagecommon-imageaioptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions,
    reloadKey?: string
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T--><!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-na-imagecommon-imageaioptions-i.md) | No |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableImage>(
    factory: ConstructorT<T>, 
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    reloadKey?: string
  ): T
```

Constructor of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T--><!--Device-ExtendableImage-@ComponentBuilder  static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableImage>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>
  ): void
```

Entry of Extendable Image.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-@Builder  static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void--><!--Device-ExtendableImage-@Builder  static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |

## setImageOptions

```TypeScript
public setImageOptions(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
    imageAIOptions?: ImageAIOptions
  ): this
```

Set the Image Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-na-imagecommon-imageaioptions-i.md) | No |  |

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-na-imagecommon-imageaioptions-i.md) | No |  |
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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-na-image-imagecontent-e.md) \| undefined | Yes |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

