# Menu

## Menu

```TypeScript
@ComponentBuilder
export declare function Menu(

    content_?: CustomBuilder,
): MenuAttribute
```

Defines Menu Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Menu(    content_?: CustomBuilder,): MenuAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Menu(    content_?: CustomBuilder,): MenuAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuAttribute](arkts-menu-attribute.md) |  |


## Menu

```TypeScript
@Builder
export declare function Menu(
    style_: CustomBuilderT<MenuAttribute>,
    content_?: CustomBuilder,
): MenuAttribute
```

Defines Menu Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Menu(    style_: CustomBuilderT<MenuAttribute>,    content_?: CustomBuilder,): MenuAttribute--><!--Device-unnamed-@Builderexport declare function Menu(    style_: CustomBuilderT<MenuAttribute>,    content_?: CustomBuilder,): MenuAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[MenuAttribute](arkts-menu-attribute.md)&gt; | Yes | menu attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuAttribute](arkts-menu-attribute.md) |  |

