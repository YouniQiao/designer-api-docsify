# ExtendableImage

扩展图像组件定义

**Inheritance/Implementation:** ExtendableImage implements [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md/arkts-arkui-image-attribute.md)

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

扩展图像组件构造器

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No |  |

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

扩展图像组件构造器

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No |  |
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

扩展图像组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T--><!--Device-ExtendableImage-static $_instantiate<T extends ExtendableImage>(    factory: ConstructorT<T>,     src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
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

扩展图像组件构入口

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void--><!--Device-ExtendableImage-static _instantiateImpl<T extends ExtendableImage>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |

## setImageOptions

```TypeScript
public setImageOptions(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
    imageAIOptions?: ImageAIOptions
  ): this
```

设置图像组件选项

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No |  |

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

设置图像组件选项

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     imageAIOptions?: ImageAIOptions,    reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No |  |
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

设置图像组件选项

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this--><!--Device-ExtendableImage-public setImageOptions(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,     reloadKey?: string  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes |  |
| reloadKey | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

