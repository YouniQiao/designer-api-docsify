# If

## If

```TypeScript
export declare function If(
  condition: boolean,
  content_: CustomBuilder
): IfAttribute
```

定义If组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | 'If'分支对应的条件 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | 'If'分支需要运行的代码 |

**Return value:**

| Type | Description |
| --- | --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) |  |


## If

```TypeScript
export declare function If(
    style: CustomBuilderT<IfAttribute>,
    content_: CustomBuilder
): IfAttribute
```

定义If组件。它需要在组件属性设置开始时调用setIfOptions。并且它需要在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;IfAttribute&gt; | Yes | 回调来设置If的属性 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | 分支的逻辑代码。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) | If的属性。 |

