# FolderStack

## FolderStack

```TypeScript
export declare function FolderStack(
    options?: FolderStackOptions, 
    content_?: CustomBuilder
): FolderStackAttribute
```

FolderStack的配置项。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute--><!--Device-unnamed-export declare function FolderStack(    options?: FolderStackOptions,     content_?: CustomBuilder): FolderStackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstack-folderstackoptions-i.md) | 否 | FolderStack的配置项。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |  |


## FolderStack

```TypeScript
export declare function FolderStack(
    style: CustomBuilderT<FolderStackAttribute>,
    content_?: CustomBuilder,
): FolderStackAttribute
```

Defines FolderStack Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute--><!--Device-unnamed-export declare function FolderStack(    style: CustomBuilderT<FolderStackAttribute>,    content_?: CustomBuilder,): FolderStackAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |  |

