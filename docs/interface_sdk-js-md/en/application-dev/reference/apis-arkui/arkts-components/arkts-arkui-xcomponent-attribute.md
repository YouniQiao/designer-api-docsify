# XComponent properties/events

定义XComponentAttribute。

除通用属性外，还支持以下属性。

从API版本12开始，当type设置为**SURFACE**或**TEXTURE**时，支持[通用事件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)。

**Inheritance/Implementation:** XComponentAttribute extends [CommonMethod<XComponentAttribute>](CommonMethod<XComponentAttribute>)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class XComponentAttribute extends CommonMethod<XComponentAttribute>--><!--Device-unnamed-declare class XComponentAttribute extends CommonMethod<XComponentAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

设置是否启用AI图像分析器，支持主体识别、文字识别和查找对象。

要使设置生效，此属性必须与XComponentController的[StartImageAnalyzer](arkts-arkui-xcomponentcontroller-c.md#startimageanalyzer)和[StopImageAnalyzer](arkts-arkui-xcomponentcontroller-c.md#stopimageanalyzer)一起使用。

此特性不能与[overlay](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-overlay.md#overlay)属性同时使用。如果两者都设置，overlay中的CustomBuilder属性将不生效。此特性还依赖于设备能力。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-enableAnalyzer(enable: boolean): XComponentAttribute--><!--Device-XComponentAttribute-enableAnalyzer(enable: boolean): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否启用AI图像分析器。&lt;br&gt;**true**：启用；**false**：禁用。&lt;br&gt; 默认值：**false**。 |

## enableSecure

```TypeScript
enableSecure(isSecure: boolean)
```

设置是否启用安全surface，以保护组件内渲染的内容不被截屏或录屏。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-XComponentAttribute-enableSecure(isSecure: boolean): XComponentAttribute--><!--Device-XComponentAttribute-enableSecure(isSecure: boolean): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSecure | boolean | Yes | 是否启用安全surface。&lt;br&gt;值**true**表示启用安全surface，**false**表示相反的情况。&lt;br&gt; 默认值：**false**。 |

## hdrBrightness

```TypeScript
hdrBrightness(brightness: number)
```

用于调整组件播放HDR视频的亮度。

**说明：**仅XComponent构造参数中的type为**XComponentType**.SURFACE时该接口生效，否则该接口不生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-XComponentAttribute-hdrBrightness(brightness: number): XComponentAttribute--><!--Device-XComponentAttribute-hdrBrightness(brightness: number): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | number | Yes | HDR视频的亮度。&lt;br/&gt;取值范围：[0.0, 1.0]。小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。 &lt;br/&gt;**0.0**表示视频按照SDR亮度显示，**1.0**表示视频按照当前允许的最高HDR亮度显示。&lt;br/&gt;默认值：**1.0**。 |

## hdrBrightness

```TypeScript
hdrBrightness(brightness: number, type?: HdrType)
```

用于调整组件显示HDR内容时的亮度。&lt;br/&gt;当参数type设置为非**HdrType**.DEFAULT时，调用该接口前需先检查Display的hdrFormats属性是否包含对应的HDRFormat。仅当hdrFormats包含对应的HDRFormat时，当前设备才支持对应的HDR类型，参数设置才会生效；否则将使用默认值**HdrType**.DEFAULT。其映射关系如下：&lt;br/&gt;| type取值 | hdrFormats需包含的HDRFormat |&lt;br/&gt;| -------- | -------- |&lt;br/&gt;| **HdrType**.AIHDR | HDRFormat.VIDEO_AIHDR |

**说明：**仅XComponent构造参数中的type为**XComponentType**.SURFACE时该接口生效，否则该接口不生效。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-XComponentAttribute-hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute--><!--Device-XComponentAttribute-hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | number | Yes | HDR内容的亮度。&lt;br/&gt;取值范围：[0.0, 1.0]。小于0.0的值按0.0处理，大于1.0的值按1.0处理，其他异常值按1.0处理。 &lt;br/&gt;**0.0**表示内容按照SDR亮度显示，**1.0**表示内容按照当前允许的最高HDR亮度显示。&lt;br/&gt;默认值：**1.0**。 |
| type | [HdrType](../../apis-media-kit/arkts-apis/arkts-media-media-hdrtype-e.md) | No | 显示HDR内容时的HDR类型。&lt;br/&gt;默认值：**HdrType.DEFAULT |

## onDestroy

```TypeScript
onDestroy(event: VoidCallback)
```

当插件销毁时触发。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-onDestroy(event: VoidCallback): XComponentAttribute--><!--Device-XComponentAttribute-onDestroy(event: VoidCallback): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | XComponent销毁后的回调。<br>**Since:** 18 |

## onLoad

```TypeScript
onLoad(callback: OnNativeLoadCallback)
```

插件加载完成时回调事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-onLoad(callback: OnNativeLoadCallback): XComponentAttribute--><!--Device-XComponentAttribute-onLoad(callback: OnNativeLoadCallback): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeLoadCallback](arkts-arkui-onnativeloadcallback-t.md) | Yes | 插件加载完成时回调事件，用于获取XComponent实例对象的context。<br>**Since:** 18 |

