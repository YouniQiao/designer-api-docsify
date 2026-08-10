# Refresh

## Refresh

```TypeScript
export declare function Refresh(
    value: RefreshOptions, 
    content_?: CustomBuilder,
): RefreshAttribute
```

创建Refresh容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Refresh(    value: RefreshOptions,     content_?: CustomBuilder,): RefreshAttribute--><!--Device-unnamed-export declare function Refresh(    value: RefreshOptions,     content_?: CustomBuilder,): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RefreshOptions](../arkts-components/arkts-arkui-refreshoptions-i.md) | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md) | 返回Refresh组件的属性。 |


## Refresh

```TypeScript
export declare function Refresh(
    style_: CustomBuilderT<RefreshAttribute>,
    content_?: CustomBuilder
): RefreshAttribute
```

定义刷新组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute--><!--Device-unnamed-export declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;RefreshAttribute&gt; | Yes | 创建刷新的样式。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md) | Refresh的属性。 |

