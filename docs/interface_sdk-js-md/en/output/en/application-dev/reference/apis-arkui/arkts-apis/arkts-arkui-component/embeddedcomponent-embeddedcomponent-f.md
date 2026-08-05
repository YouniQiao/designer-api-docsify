# EmbeddedComponent

## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | indicates initialization parameter. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | indicates type of the EmbeddedComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | indicates initialization parameter. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | indicates type of the EmbeddedComponent. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | indicates type of the EmbeddedComponent options. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    style: CustomBuilderT<EmbeddedComponentAttribute>
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.It requires call setEmbeddedComponentOptions at start of the component attribute set-up, and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | the callback to set up embeddedcomponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The attribute of the EmbeddedComponent. |

