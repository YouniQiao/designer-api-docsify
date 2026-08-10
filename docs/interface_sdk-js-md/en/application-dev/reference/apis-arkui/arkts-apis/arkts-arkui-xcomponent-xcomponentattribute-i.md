# XComponentAttribute

定义XComponent属性。

**Inheritance/Implementation:** XComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置XComponent组件的属性修改器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-XComponentAttribute-default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | XComponent组件的属性修改器。取值为undefined时，不使用attributeModifier。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default enableAnalyzer(enable: boolean | undefined): this--><!--Device-XComponentAttribute-default enableAnalyzer(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | 是否启用AI分析功能。&lt;br&gt;true：开启AI分析；false：关闭AI分析。 &lt;br&gt;默认值：false&lt;br&gt;ArkTS-Sta模式下可不传，不传时使用默认值false。&lt;br&gt;**说明：**仅type为SURFACE或TEXTURE时该功能有效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableSecure

```TypeScript
default enableSecure(isSecure: boolean | undefined): this
```

防止组件内自绘制内容被截屏、录屏。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default enableSecure(isSecure: boolean | undefined): this--><!--Device-XComponentAttribute-default enableSecure(isSecure: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSecure | boolean \| undefined | Yes | 是否开启隐私图层模式。&lt;br&gt;true：开启隐私图层模式；false：关闭隐私图层模式。&lt;br&gt;默认值：false。 &lt;br&gt;ArkTS-Sta模式下可不传，不传时使用默认值false。&lt;br&gt;**说明：**仅type为SURFACE时有效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined): this
```

用于调整组件播放HDR视频的亮度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined): this--><!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes | HDR视频的亮度。&lt;br&gt;默认值：1.0&lt;br&gt;取值范围：[0.0, 1.0]。 小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。&lt;br&gt;0.0表示视频按照SDR亮度显示，1.0表示视频按照当前允许的最高HDR亮度显示。 &lt;br&gt;**说明：**仅type为SURFACE时有效。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined, type?: HdrType): this
```

调整组件播放HDR视频时的亮度，该接口仅对HDR视频生效。

**说明：**仅XComponent构造参数中的type为SURFACE时该接口生效，否则该接口不生效。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined, type?: HdrType): this--><!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined, type?: HdrType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes | HDR内容的亮度。&lt;br&gt;默认值：1.0&lt;br&gt;取值范围：[0.0, 1.0]。 小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。&lt;br&gt;0.0表示内容按照SDR亮度显示，1.0表示内容按照当前允许的最高HDR亮度显示。 &lt;br&gt;ArkTS-Sta模式下可不传，不传时使用默认值1.0。 |
| type | [HdrType](../../apis-media-kit/arkts-apis/arkts-media-media-hdrtype-e.md) | No | 显示HDR内容时的HDR类型。&lt;br&gt;默认值：HdrType.DEFAULT |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDestroy

```TypeScript
default onDestroy(event: VoidCallback | undefined): this
```

插件卸载完成时回调事件。与onSurfaceDestroyed的区别：onDestroy适用于设置libraryname参数的场景，回调无参数；onSurfaceDestroyed适用于未设置libraryname参数的场景，回调参数为surfaceId。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default onDestroy(event: VoidCallback | undefined): this--><!--Device-XComponentAttribute-default onDestroy(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | 插件卸载完成时回调事件。&lt;br&gt;ArkTS-Sta模式下可不传。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onLoad

```TypeScript
default onLoad(callback: VoidCallback | undefined): this
```

插件加载完成时回调事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default onLoad(callback: VoidCallback | undefined): this--><!--Device-XComponentAttribute-default onLoad(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | 插件加载完成时回调事件，用于获取XComponent实例对象的context。&lt;br&gt;ArkTS-Sta模式下可不传。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setXComponentOptions

```TypeScript
setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this
```

设置XComponent选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this--><!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) \| XComponentOptions \| NativeXComponentParameters | Yes | 用于创建XComponent的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | XComponentAttribute实例 |

