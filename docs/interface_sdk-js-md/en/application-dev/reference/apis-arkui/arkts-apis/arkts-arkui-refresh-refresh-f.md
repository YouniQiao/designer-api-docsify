# Refresh

## Refresh

```TypeScript
export declare function Refresh(
    value: RefreshOptions,
    content_?: CustomBuilder,
): RefreshAttribute
```

Defines Refresh Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Refresh(    value: RefreshOptions,    content_?: CustomBuilder,): RefreshAttribute--><!--Device-unnamed-export declare function Refresh(    value: RefreshOptions,    content_?: CustomBuilder,): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RefreshOptions](arkts-arkui-refresh-refreshoptions-i.md) | Yes | value |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md) | The attribute of the grid |


## Refresh

```TypeScript
export declare function Refresh(
    style_: CustomBuilderT<RefreshAttribute>,
    content_?: CustomBuilder
): RefreshAttribute
```

Defines Refresh Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute--><!--Device-unnamed-export declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md)&gt; | Yes | The style to create a Refresh. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md) | The attribute of the Refresh. |

