# FolderStack

## FolderStack

```TypeScript
@ComponentBuilder
export declare function FolderStack(
    options?: FolderStackOptions, 
    content_?: CustomBuilder
): FolderStackAttribute
```

Defines FolderStack Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstack-folderstackoptions-i.md) | No | FolderStack options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| FolderStackAttribute |  |


## FolderStack

```TypeScript
@Builder
export declare function FolderStack(
    style: CustomBuilderT<FolderStackAttribute>,
    content_?: CustomBuilder,
): FolderStackAttribute
```

Defines FolderStack Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute--><!--Device-unnamed-@Builderexport declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;FolderStackAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| FolderStackAttribute |  |

