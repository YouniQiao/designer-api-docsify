# MenuItemGroup

## MenuItemGroup

```TypeScript
@ComponentBuilder
export declare function MenuItemGroup(
    value?: MenuItemGroupOptions,
    content_?: CustomBuilder,
): MenuItemGroupAttribute
```

Defines MenuItem Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function MenuItemGroup(    value?: MenuItemGroupOptions,    content_?: CustomBuilder,): MenuItemGroupAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MenuItemGroup(    value?: MenuItemGroupOptions,    content_?: CustomBuilder,): MenuItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemGroupOptions](arkts-menuitemgroup-menuitemgroupoptions-i.md) | No | The options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemGroupAttribute](arkts-menuitemgroup-attribute.md) |  |


## MenuItemGroup

```TypeScript
@Builder
export declare function MenuItemGroup(
    style_: CustomBuilderT<MenuItemGroupAttribute>,
    content_?: CustomBuilder,
): MenuItemGroupAttribute
```

Defines MenuItemGroup Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function MenuItemGroup(    style_: CustomBuilderT<MenuItemGroupAttribute>,    content_?: CustomBuilder,): MenuItemGroupAttribute--><!--Device-unnamed-@Builderexport declare function MenuItemGroup(    style_: CustomBuilderT<MenuItemGroupAttribute>,    content_?: CustomBuilder,): MenuItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[MenuItemGroupAttribute](arkts-menuitemgroup-attribute.md)&gt; | Yes | menuitemgroup attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemGroupAttribute](arkts-menuitemgroup-attribute.md) |  |

