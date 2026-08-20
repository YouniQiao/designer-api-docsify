# If

## If

```TypeScript
@ComponentBuilder
export declare function If(
  condition: boolean,
  content_: CustomBuilder
): IfAttribute
```

Defines If Component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | condition of the branch. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | Yes | code for the branch |

**Return value:**

| Type | Description |
| --- | --- |
| [IfAttribute](arkts-if-attribute.md) |  |


## If

```TypeScript
@Builder
export declare function If(
    style: CustomBuilderT<IfAttribute>,
    content_: CustomBuilder
): IfAttribute
```

Defines If Component. It requires calling setIfOptions at start of component attribute set-up, and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute--><!--Device-unnamed-@Builderexport declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[IfAttribute](arkts-if-attribute.md)&gt; | Yes | callback to set up If's attributes. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | Yes | code for the branch |

**Return value:**

| Type | Description |
| --- | --- |
| [IfAttribute](arkts-if-attribute.md) | The attribute of If. |

