# Hyperlink

## Hyperlink

```TypeScript
export declare function Hyperlink(
    address: string | Resource | undefined, content?: string | Resource, 
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string \| Resource \| undefined | Yes | The link address of component. The default value is an empty string. Passing \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ resets it to the default value. |
| content | string \| Resource | No | The title of the component. |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The node of component. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |


## Hyperlink

```TypeScript
export declare function Hyperlink(
    style: CustomBuilderT<HyperlinkAttribute>,
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Hyperlink attribute instance. |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

