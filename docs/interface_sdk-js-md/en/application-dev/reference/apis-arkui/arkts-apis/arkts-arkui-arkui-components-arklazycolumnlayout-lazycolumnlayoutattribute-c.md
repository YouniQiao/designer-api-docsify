# LazyColumnLayoutAttribute

Defines the lazy column layout attribute.

**Inheritance/Implementation:** LazyColumnLayoutAttribute extends CommonMethod<LazyColumnLayoutAttribute>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class LazyColumnLayoutAttribute--><!--Device-unnamed-export declare class LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LazyColumnLayout } from 'LazyColumnLayout';
import { LazyColumnLayoutAttribute } from 'LazyColumnLayoutAttribute';
```

## alignItems

```TypeScript
alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute
```

Sets the horizontal alignment of the row content.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [HorizontalAlign](../../apis-na/arkts-apis/arkts-na-enums-horizontalalign-e.md) \| undefined | Yes | the horizontal alignment of the row content. <br>Default value HorizontalAlign.Center. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

## footer

```TypeScript
footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute
```

Sets the footer of the lazy column layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | CustomBuilder \| undefined | Yes | The footer builder function <br>Passing undefined will remove the footer. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

## header

```TypeScript
header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute
```

Sets the header of the lazy column layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | CustomBuilder \| undefined | Yes | The header builder function <br>Passing undefined will remove the header. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute
```

Triggered when the index of child components in the visible area changes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../../apis-na/arkts-apis/arkts-na-onvisibleindexeschangecallback-t.md) \| undefined | Yes | callback function, triggered when the index of child components in the visible area changes. <br>Passing undefined will unregister the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

## space

```TypeScript
space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute
```

The spacing between rows.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| space | [LengthMetrics](../../apis-na/arkts-apis/arkts-na-graphics-lengthmetrics-c.md) \| undefined | Yes | the spacing between rows. <br>Default value: 0. <br>Range: [0, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

## sticky

```TypeScript
sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute
```

Sets sticky style for header and footer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyColumnLayoutAttribute-sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute--><!--Device-LazyColumnLayoutAttribute-sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sticky | [StickyStyle](../../apis-na/arkts-apis/arkts-na-list-stickystyle-e.md) \| undefined | Yes | The sticky style for header and footer. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-c.md) |  |

