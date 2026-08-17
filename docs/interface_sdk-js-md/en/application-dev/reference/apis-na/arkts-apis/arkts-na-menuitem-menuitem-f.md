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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemOptions](arkts-na-menuitem-menuitemoptions-i.md) \| CustomBuilder | No | the options of MenuItem. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-na-menuitem-menuitemattribute-i.md) |  |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-@Builderexport declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[MenuItemAttribute](arkts-na-menuitem-menuitemattribute-i.md)&gt; | Yes | menuitem attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-na-menuitem-menuitemattribute-i.md) |  |

