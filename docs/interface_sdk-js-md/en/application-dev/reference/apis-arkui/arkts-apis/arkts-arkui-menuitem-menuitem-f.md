# MenuItem

## MenuItem

```TypeScript
export declare function MenuItem(
    value?: MenuItemOptions | CustomBuilder,
    content_?: CustomBuilder,
): MenuItemAttribute
```

Defines MenuItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-export declare function MenuItem(    value?: MenuItemOptions | CustomBuilder,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemOptions](arkts-arkui-menuitem-menuitemoptions-i.md) \| CustomBuilder | No | the options of MenuItem. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |  |


## MenuItem

```TypeScript
export declare function MenuItem(
    style_: CustomBuilderT<MenuItemAttribute>,
    content_?: CustomBuilder,
): MenuItemAttribute
```

Defines MenuItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute--><!--Device-unnamed-export declare function MenuItem(    style_: CustomBuilderT<MenuItemAttribute>,    content_?: CustomBuilder,): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;MenuItemAttribute&gt; | Yes | menuitem attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MenuItemAttribute](arkts-arkui-menuitem-menuitemattribute-i.md) |  |

