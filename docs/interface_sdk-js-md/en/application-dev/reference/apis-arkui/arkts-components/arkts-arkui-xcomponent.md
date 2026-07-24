# XComponent

**XComponent** provides a [surface](docroot://ui/napi-xcomponent-guidelines.md#overview) for graphics rendering and
media data input into your view. You can customize the position and size of the surface as needed. For details, see
[Native XComponent](docroot://ui/napi-xcomponent-guidelines.md).

> **NOTE**

## Child Components

Not supported

## XComponent

```TypeScript
XComponent(value: { id: string; type: string; libraryname?: string; controller?: XComponentController })
```

Constructor parameters

**Since:** 8

**Deprecated since:** 12

**Substitutes:** <!--SUBSTITUTE_API-->(value:<!--/SUBSTITUTE_API-->

<!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { id: string; type: string; libraryname?: string; controller?: XComponentController } | Yes | Indicates the options of the xcomponent.  |

## XComponent

```TypeScript
XComponent(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController })
```

Creates an **XComponent** component, whose lifecycle callbacks can be triggered from the native side.

This API is deprecated since API version 12. You are advised to use [XComponent(options: XComponentOptions)](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-xcomponent.md#xcomponent12)instead.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController } | Yes | Indicates the options of the xcomponent.  |

## XComponent

```TypeScript
XComponent(options: XComponentOptions)
```

Creates an **XComponent** component, allowing you to obtain the **SurfaceId** value on the ArkTS side, register the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events such as touch, mouse, and key events, and configure the AI analyzer feature.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute--><!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [XComponentOptions](arkts-arkui-xcomponentoptions-i.md) | Yes | Options of the **XComponent**.  |

## XComponent

```TypeScript
XComponent(params: NativeXComponentParameters)
```

Obtains an **XComponent** node instance on the native side, and registers the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events, such as touch, mouse, and key events.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute--><!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [NativeXComponentParameters](arkts-arkui-nativexcomponentparameters-i.md) | Yes | Options of the **XComponent**.  |

## Summary

- [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md)
- [SurfaceConfig](arkts-arkui-xcomponent-surfaceconfig-i.md)
- [SurfaceRect](arkts-arkui-xcomponent-surfacerect-i.md)
- [SurfaceRotationOptions](arkts-arkui-xcomponent-surfacerotationoptions-i.md)
- [XComponentOptions](arkts-arkui-xcomponent-xcomponentoptions-i.md)
- [OnNativeLoadCallback](arkts-arkui-xcomponent-onnativeloadcallback-t.md)
- [HdrType](arkts-arkui-xcomponent-hdrtype-e.md)
