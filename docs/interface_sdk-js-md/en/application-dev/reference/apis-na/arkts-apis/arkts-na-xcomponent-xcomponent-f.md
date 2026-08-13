# XComponent

## XComponent

```TypeScript
@ComponentBuilder
export declare function XComponent(
    params: XComponentParameters | XComponentOptions | NativeXComponentParameters
): XComponentAttribute
```

XComponent is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function XComponent(    params: XComponentParameters | XComponentOptions | NativeXComponentParameters): XComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function XComponent(    params: XComponentParameters | XComponentOptions | NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [XComponentParameters](arkts-na-xcomponent-xcomponentparameters-i.md) \| [XComponentOptions](arkts-na-xcomponent-xcomponentoptions-i.md) \| [NativeXComponentParameters](arkts-na-xcomponent-nativexcomponentparameters-i.md) | Yes | The options to create an XComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](arkts-na-xcomponent-xcomponentattribute-i.md) | The attribute of the XComponent |


## XComponent

```TypeScript
@Builder
export declare function XComponent(
    style: CustomBuilderT<XComponentAttribute>
): XComponentAttribute
```

Defines XComponent Component.It requires call setXComponentOptions at start of the component attribute set-up, and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function XComponent(    style: CustomBuilderT<XComponentAttribute>): XComponentAttribute--><!--Device-unnamed-@Builderexport declare function XComponent(    style: CustomBuilderT<XComponentAttribute>): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[XComponentAttribute](arkts-na-xcomponent-xcomponentattribute-i.md)&gt; | Yes | the callback to set up xcomponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](arkts-na-xcomponent-xcomponentattribute-i.md) | The attribute of the XComponent. |

