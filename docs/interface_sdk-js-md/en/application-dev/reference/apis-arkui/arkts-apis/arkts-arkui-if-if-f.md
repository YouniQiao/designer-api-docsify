# If

## If

```TypeScript
export declare function If(
  condition: boolean,
  content_: CustomBuilder
): IfAttribute
```

Defines If Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | condition of the branch. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | code for the branch |

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

Defines If Component. It requires calling setIfOptions at start of component attribute set-up,and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;IfAttribute&gt; | Yes | callback to set up If's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | code for the branch |

**Return value:**

| Type | Description |
| --- | --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) | The attribute of If. |

