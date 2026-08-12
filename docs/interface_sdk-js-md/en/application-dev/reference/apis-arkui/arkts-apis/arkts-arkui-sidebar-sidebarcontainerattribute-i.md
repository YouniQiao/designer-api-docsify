# SideBarContainerAttribute

The attribute function of sidebar

**Inheritance/Implementation:** SideBarContainerAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SideBarContainerAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of sidebar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SideBarContainerAttribute-default attributeModifier(modifier: AttributeModifier<SideBarContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SideBarContainerAttribute](arkts-arkui-sidebar-sidebarcontainerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of sidebar. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## autoHide

```TypeScript
default autoHide(value: boolean | undefined): this
```

Sets whether to automatically hide when drag sidebar width is less than the minimum width.default value is true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default autoHide(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## controlButton

```TypeScript
default controlButton(value: ButtonStyle | undefined): this
```

Callback controlButton function when setting the style of button

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this--><!--Device-SideBarContainerAttribute-default controlButton(value: ButtonStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ButtonStyle](arkts-arkui-sidebar-buttonstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

Set divider style for sideBarContainer

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this--><!--Device-SideBarContainerAttribute-default divider(value: DividerStyle | null | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | DividerStyle \| null \| undefined | Yes | indicates the style of the divider or whether to show the divider. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## maxSideBarWidth

```TypeScript
default maxSideBarWidth(value: Length | undefined): this
```

Sets the max length of sidebar.default value is 280vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default maxSideBarWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minContentWidth

```TypeScript
default minContentWidth(value: Dimension | undefined): this
```

Sets the min length of content.default value is 360vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this--><!--Device-SideBarContainerAttribute-default minContentWidth(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | min length of content. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minSideBarWidth

```TypeScript
default minSideBarWidth(value: Length | undefined): this
```

Sets the min length of sidebar.default value is 200vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this--><!--Device-SideBarContainerAttribute-default minSideBarWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((value: boolean) => void) | undefined): this
```

Trigger callback when sidebar style of showing change finished.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this--><!--Device-SideBarContainerAttribute-default onChange(callback: ((value: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((value: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setSideBarContainerOptions

```TypeScript
default setSideBarContainerOptions(type?: SideBarContainerType): this
```

Set sidebar container options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this--><!--Device-SideBarContainerAttribute-default setSideBarContainerOptions(type?: SideBarContainerType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | No | Sidebar container type options &lt;br&gt;Default value:SideBarContainerType.Embed |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the SideBarContainerAttribute. |

## showControlButton

```TypeScript
default showControlButton(value: boolean | undefined): this
```

Callback showControlButton function when setting the status of button

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showControlButton(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showSideBar

```TypeScript
default showSideBar(value: boolean | Bindable<boolean> | undefined): this
```

Callback showControlButton function when setting the status of sidebar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBar(value: boolean | Bindable<boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showSideBarWithGesture

```TypeScript
default showSideBarWithGesture(value: boolean | undefined): this
```

Specifies whether sideBar can be presented or dismissed by gesture.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this--><!--Device-SideBarContainerAttribute-default showSideBarWithGesture(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Indicates whether sidebar can be presented or dismissed by gesture. &lt;br&gt;Default value: **false**. **true**: Sidebar can be presented or dismissed by gesture. **false**: Sidebar cannot be presented or dismissed by gesture. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sideBarPosition

```TypeScript
default sideBarPosition(value: SideBarPosition | undefined): this
```

Called when determining the location of the sidebar.default value is SideBarPosition.Start.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarPosition(value: SideBarPosition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SideBarPosition](arkts-arkui-sidebar-sidebarposition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sideBarWidth

```TypeScript
default sideBarWidth(value: Length | Bindable<Length> | undefined): this
```

Sets the length of sidebar.default value is 240vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this--><!--Device-SideBarContainerAttribute-default sideBarWidth(value: Length | Bindable<Length> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Length](arkts-arkui-length-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

