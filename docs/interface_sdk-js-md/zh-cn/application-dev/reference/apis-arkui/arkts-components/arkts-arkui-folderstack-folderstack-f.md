# FolderStack

## FolderStack

```TypeScript
@ComponentBuilder
export declare function FolderStack(
    options?: FolderStackOptions, 
    content_?: CustomBuilder
): FolderStackAttribute
```

FolderStack的配置项。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstack-folderstackoptions-i.md) | 否 | FolderStack的配置项。 |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FolderStackAttribute](arkts-arkui-folderstack-attribute.md) |  |


## FolderStack

```TypeScript
@Builder
export declare function FolderStack(
    style: CustomBuilderT<FolderStackAttribute>,
    content_?: CustomBuilder,
): FolderStackAttribute
```

Defines FolderStack Component.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute--><!--Device-unnamed-@Builderexport declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[FolderStackAttribute](arkts-arkui-folderstack-attribute.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FolderStackAttribute](arkts-arkui-folderstack-attribute.md) |  |

