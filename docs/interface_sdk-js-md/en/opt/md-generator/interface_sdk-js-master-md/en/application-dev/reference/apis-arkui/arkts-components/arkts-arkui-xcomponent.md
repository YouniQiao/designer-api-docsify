# XComponent

**XComponent** provides a [surface](../../../ui/napi-xcomponent-guidelines.md#overview) for graphics rendering and media data input into your view. You can customize the position and size of the surface as needed. For details, see [Native XComponent](../../../ui/napi-xcomponent-guidelines.md). > **NOTE**

## Child Components Not supported

## XComponent

```TypeScript
XComponent(value: { id: string; type: string; libraryname?: string; controller?: XComponentController })
```

Constructor parameters

**Since:** 8

**Deprecated since:** 12

**Substitutes:** (value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController })

<!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { id: string; type: string; libraryname?: string; controller?: XComponentController } | Yes |

## XComponent

```TypeScript
XComponent(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController })
```

Creates an **XComponent** component, whose lifecycle callbacks can be triggered from the native side. This API is deprecated since API version 12. You are advised to use [XComponent(options: XComponentOptions)](../../../reference/apis-arkui/arkui-ts/ts-basic-components-xcomponent.md#xcomponent12) instead.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController } | Yes |

## XComponent

```TypeScript
XComponent(options: XComponentOptions)
```

Creates an **XComponent** component, allowing you to obtain the **SurfaceId** value on the ArkTS side, register the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events such as touch, mouse, and key events, and configure the AI analyzer feature.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute--><!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [XComponentOptions](arkts-arkui-xcomponentoptions-i.md) | Yes |

## XComponent

```TypeScript
XComponent(params: NativeXComponentParameters)
```

Obtains an **XComponent** node instance on the native side, and registers the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events, such as touch, mouse, and key events.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute--><!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [NativeXComponentParameters](arkts-arkui-nativexcomponentparameters-i.md) | Yes |

## Summary

- [NativeXComponentParameters](arkts-arkui-nativexcomponentparameters-i.md)
- [SurfaceConfig](arkts-arkui-surfaceconfig-i.md)
- [SurfaceRect](arkts-arkui-surfacerect-i.md)
- [SurfaceRotationOptions](arkts-arkui-surfacerotationoptions-i.md)
- [XComponentOptions](arkts-arkui-xcomponentoptions-i.md)
- [OnNativeLoadCallback](arkts-arkui-onnativeloadcallback-t.md)
- [HdrType](arkts-arkui-hdrtype-e.md)
