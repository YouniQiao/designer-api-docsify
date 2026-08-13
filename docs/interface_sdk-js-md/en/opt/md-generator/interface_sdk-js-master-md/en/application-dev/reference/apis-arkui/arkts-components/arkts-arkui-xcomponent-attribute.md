# XComponent properties/events

In addition to universal attributes, the following attributes are supported. Since API version 12, the universal events are supported when **type** is set to **SURFACE** or **TEXTURE**.

**Inheritance/Implementation:** XComponentAttribute extends CommonMethod<XComponentAttribute>

**Since:** 8

**Deprecated since:** -1

<!--Device-unnamed-declare class XComponentAttribute--><!--Device-unnamed-declare class XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup. For the settings to take effect, this attribute must be used together with [StartImageAnalyzer](arkts-arkui-xcomponentcontroller-c.md#startImageAnalyzer) and [StopImageAnalyzer](arkts-arkui-xcomponentcontroller-c.md#stopImageAnalyzer) of **XComponentController**. This feature cannot be used together with the [overlay](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-overlay.md#overlay) attribute. If they are set at the same time, the **CustomBuilder** attribute in **overlay** has no effect. This feature depends on device capabilities.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-enableAnalyzer(enable: boolean): XComponentAttribute--><!--Device-XComponentAttribute-enableAnalyzer(enable: boolean): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableSecure

```TypeScript
enableSecure(isSecure: boolean)
```

Sets whether to enable the secure surface to protect the content rendered within the component from being captured or recorded.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-XComponentAttribute-enableSecure(isSecure: boolean): XComponentAttribute--><!--Device-XComponentAttribute-enableSecure(isSecure: boolean): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isSecure | boolean | Yes |

## hdrBrightness

```TypeScript
hdrBrightness(brightness: number, type?: HdrType)
```

Set hdrBrightness for XComponent.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-XComponentAttribute-hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute--><!--Device-XComponentAttribute-hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |
| type | [HdrType](arkts-arkui-hdrtype-e.md) | No |

## onDestroy

```TypeScript
onDestroy(event: VoidCallback)
```

Triggered when the plugin is destroyed.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-onDestroy(event: VoidCallback): XComponentAttribute--><!--Device-XComponentAttribute-onDestroy(event: VoidCallback): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes |

## onLoad

```TypeScript
onLoad(callback: OnNativeLoadCallback)
```

Triggered when the plugin is loaded.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentAttribute-onLoad(callback: OnNativeLoadCallback): XComponentAttribute--><!--Device-XComponentAttribute-onLoad(callback: OnNativeLoadCallback): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnNativeLoadCallback](arkts-arkui-onnativeloadcallback-t.md) | Yes |
