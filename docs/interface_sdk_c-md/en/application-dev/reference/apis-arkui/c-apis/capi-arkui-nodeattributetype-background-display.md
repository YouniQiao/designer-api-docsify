# Background Display

## Overview

Defines the ArkUI style attributes that can be set on the native side.

**Since**: 12

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [native_node.h](capi-native-node-h.md)

### NODE_BACKGROUND_COLOR

```c
NODE_BACKGROUND_COLOR
```

**Description**

Background color attribute, which can be set, reset, and obtained as required through APIs. The format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute and the format of the return value **ArkUI_AttributeItem** are as follows. **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].u32: background color, in 0xARGB format. The value range is from 0x00000000 to 0xFFFFFFFF. For example, `0xFFFF0000` indicates red.</li> </ul><br> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].u32: background color, in 0xARGB format. For example, **0xFFFF0000** indicates red.</li> </ul>

**Since**: 12

### NODE_BACKGROUND_IMAGE

```c
NODE_BACKGROUND_IMAGE
```

**Description**

Background image attribute, which can be set, reset, and obtained as required through APIs. The format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute and the format of the return value **ArkUI_AttributeItem** are as follows. **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.string: image address. In API version 22 and earlier versions, the value can be a network image resource address, local image resource address, Base64 string, or [PixelMap](../../apis-image-kit/c-apis/capi-image-pixel-map-mdk-h.md#oh_pixelmap_antialiasinglevel) resource, but cannot be the address of an animated image such as an [SVG](capi-native-node-h.md#arkui_nodeattributetype), GIF, or WebP image. In API version 23 and later versions, animated images of the WebP and GIF types are supported. Only the first frame of the animated image is displayed. Other types of animated images are not supported.</li> <li>.value[0]?.i32: whether the image is repeated. This parameter is optional. The parameter type is [ArkUI_ImageRepeat](capi-image-h.md#arkui_imagerepeat). The default value is **ARKUI_IMAGE_REPEAT_NONE**.</li> <li>.object: **PixelMap** object. The parameter type is [ArkUI_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md). Either **.object** or **.string** must be set.</li> </ul><br> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.string: image address. In API version 22 and earlier versions, the value can be a network image resource address, local image resource address, Base64 string, or PixelMap resource, but cannot be the address of an animated image such as an SVG, GIF, or WebP image. In API version 23 and later versions, animated images of the WebP and GIF types are supported. Only the first frame of the animated image is displayed. Other types of animated images are not supported.</li> <li>.value[0].i32: whether the image is repeated. The parameter type is [ArkUI_ImageRepeat](capi-image-h.md#arkui_imagerepeat).</li> <li>.object: **PixelMap** object. The parameter type is [ArkUI_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md).</li> </ul>

**Since**: 12

### NODE_BACKGROUND_IMAGE_SIZE

```c
NODE_BACKGROUND_IMAGE_SIZE
```

**Description**

Background image size attribute, which can be set, reset, and obtained as required through APIs. The format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute and the format of the return value **ArkUI_AttributeItem** are as follows. **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].f32: width of the image. The value range is [0,+∞), and the unit is vp.</li> <li>.value[1].f32: height of the image. The value range is [0,+∞), and the unit is vp.</li> </ul> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].f32: width of the image, in vp.</li> <li>.value[1].f32: height of the image, in vp.</li> </ul>

**Since**: 12

### NODE_BACKGROUND_IMAGE_SIZE_WITH_STYLE

```c
NODE_BACKGROUND_IMAGE_SIZE_WITH_STYLE
```

**Description**

Background image size with style. This attribute can be set, reset, and obtained as required through APIs. The format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute and the format of the return value **ArkUI_AttributeItem** are as follows. **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].i32: background image size with style. The value is an enumerated value of [ArkUI_ImageSize](capi-image-h.md#arkui_imagesize). Different enumerated values determine how the background image is scaled and cropped, such as displaying at the original size, covering the component area while maintaining the aspect ratio, or displaying completely while maintaining the aspect ratio.</li> </ul> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].i32: background image size with style. The value is an enumerated value of [ArkUI_ImageSize](capi-image-h.md#arkui_imagesize).</li> </ul>

**Since**: 12

### NODE_BACKGROUND_BLUR_STYLE

```c
NODE_BACKGROUND_BLUR_STYLE
```

**Description**

Defines the background blur attribute, which can be set, reset, and obtained as required through APIs.<br> **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].i32: blue type. The value is an enum of [ArkUI_BlurStyle](capi-native-type-visual-h.md#arkui_blurstyle).</li> <li>.value[1]?.i32: color mode. The value is an enum of [ArkUI_ColorMode](capi-native-type-h.md#arkui_colormode).</li> <li>.value[2]?.i32: adaptive color mode. The value is an enum of [ArkUI_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor).</li> <li>.value[3]?.f32: blur degree. The value range is [0.0, 1.0].</li> <li>.value[4]?.f32: start boundary of grayscale blur.</li> <li>.value[5]?.f32: end boundary of grayscale blur.</li> </ul> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].i32: blue type. The value is an enum of [ArkUI_BlurStyle](capi-native-type-visual-h.md#arkui_blurstyle).</li> <li>.value[1].i32: color mode. The value is an enum of [ArkUI_ColorMode](capi-native-type-h.md#arkui_colormode).</li> <li>.value[2].i32: adaptive color mode. The value is an enum of [ArkUI_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor).</li> <li>.value[3].f32: blur degree. The value range is [0.0, 1.0].</li> <li>.value[4].f32: start boundary of grayscale blur.</li> <li>.value[5].f32: end boundary of grayscale blur.</li> </ul>

**Since**: 12

### NODE_BACKGROUND_IMAGE_POSITION

```c
NODE_BACKGROUND_IMAGE_POSITION
```

**Description**

Position of the background image in the component, that is, the coordinates relative to the upper left corner of the component. This attribute can be set, reset, and obtained as required through APIs. The format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute and the format of the return value **ArkUI_AttributeItem** are as follows. **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].f32: position along the x-axis, in px.</li> <li>.value[1].f32: position along the y-axis, in px.</li> <li>.value[2]?.i32: alignment mode. This parameter is optional. The parameter type is [ArkUI_Alignment](capi-layout-h.md#arkui_alignment). The default value is **ARKUI_ALIGNMENT_TOP_START**. This parameter is supported since API version 21.</li> <li>.value[3]?.i32: layout direction. This parameter is optional. The parameter type is [ArkUI_Direction](capi-layout-h.md#arkui_direction). The default value is **ARKUI_DIRECTION_AUTO**. In most scenarios, you are advised to set this parameter to **AUTO**, so that the system automatically handles the layout direction. If a fixed direction is required, set this parameter to **LTR** or **RTL**. This parameter is supported since API version 21.</li> </ul> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].f32: position along the x-axis, in px.</li> <li>.value[1].f32: position along the y-axis, in px.</li> <li>.value[2].i32: alignment mode. The parameter type is [ArkUI_Alignment](capi-layout-h.md#arkui_alignment). This return value is supported since API version 21.</li> <li>.value[3].i32: layout direction. The parameter type is [ArkUI_Direction](capi-layout-h.md#arkui_direction). This return value is supported since API version 21.</li> </ul>

**Since**: 12

### NODE_BACKGROUND_IMAGE_RESIZABLE_WITH_SLICE

```c
NODE_BACKGROUND_IMAGE_RESIZABLE_WITH_SLICE = 100
```

**Description**

Defines the background image resizable attribute, which can be set, reset, and obtained as required through APIs.<br> **Format of the [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) parameter for setting the attribute:**<br><ul> <li>.value[0].f32: width of the left edge. The unit is vp. </li> <li>.value[1].f32: width of the top edge. The unit is vp. </li> <li>.value[2].f32: width of the right edge. The unit is vp. </li> <li>.value[3].f32: width of the bottom edge. The unit is vp. </li> </ul> **Format of the return value [ArkUI_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md):**<br><ul> <li>.value[0].f32: width of the left edge. The unit is vp. </li> <li>.value[1].f32: width of the top edge. The unit is vp. </li> <li>.value[2].f32: width of the right edge. The unit is vp. </li> <li>.value[3].f32: width of the bottom edge. The unit is vp. </li> </ul>

**Since**: 19


