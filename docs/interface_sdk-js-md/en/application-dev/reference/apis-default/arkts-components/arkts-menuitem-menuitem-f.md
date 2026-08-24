# MenuItem

## MenuItem

```TypeScript
@ComponentBuilder
export declare function MenuItem(
    value?: MenuItemOptions | CustomBuilder,
    content_?: CustomBuilder,
): MenuItemAttribute
```

Defines MenuItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemOptions](arkts-menuitem-menuitemoptions-i.md) \| [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | the options of MenuItem. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-menuitem-attribute.md) |  |


## MenuItem

```TypeScript
@Builder
export declare function MenuItem(
    style_: CustomBuilderT<MenuItemAttribute>,
    content_?: CustomBuilder,
): MenuItemAttribute
```

Defines MenuItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-@Builderexport declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[MenuItemAttribute](arkts-menuitem-attribute.md)&gt; | Yes | menuitem attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-menuitem-attribute.md) |  |

