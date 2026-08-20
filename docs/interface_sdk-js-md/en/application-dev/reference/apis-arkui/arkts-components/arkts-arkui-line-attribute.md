# Line properties/events

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** LineAttribute extends CommonShapeMethod<LineAttribute>

**Since:** 7

<!--Device-unnamed-declare class LineAttribute--><!--Device-unnamed-declare class LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CommonModifier, ColumnModifier, ColumnSplitModifier, RowModifier, RowSplitModifier, SideBarContainerModifier, BlankModifier, DividerModifier, GridColModifier, GridRowModifier, NavDestinationModifier, NavigatorModifier, StackModifier, NavigationModifier, NavRouterModifier, StepperItemModifier, TabsModifier, GridModifier, GridItemModifier, ListModifier, ListItemModifier, ListItemGroupModifier, ScrollModifier, SwiperModifier, WaterFlowModifier, ButtonModifier, CounterModifier, TextPickerModifier, TimePickerModifier, ToggleModifier, CalendarPickerModifier, CheckboxModifier, CheckboxGroupModifier, DatePickerModifier, RadioModifier, RatingModifier, SelectModifier, SliderModifier, PatternLockModifier, SpanModifier, RichEditorModifier, RefreshModifier, SearchModifier, TextAreaModifier, TextModifier, TextInputModifier, ImageSpanModifier, ImageAnimatorModifier, ImageModifier, VideoModifier, DataPanelModifier, GaugeModifier, LoadingProgressModifier, MarqueeModifier, ProgressModifier, QRCodeModifier, TextClockModifier, TextTimerModifier, LineModifier, PathModifier, PolygonModifier, PolylineModifier, RectModifier, ShapeModifier, AlphabetIndexerModifier, HyperlinkModifier, MenuModifier, MenuItemModifier, PanelModifier, SymbolGlyphModifier, AttributeUpdater, ContainerSpanModifier, SymbolSpanModifier, ParticleModifier, StepperModifier, UIPickerComponentModifier, ModifierUtils } from '@kit.ArkUI';
```

## endPoint

```TypeScript
endPoint(value: Array<any>)
```

Sets the coordinates (relative coordinates) of the end point of the line. This attribute can be dynamically set using attributeModifier. Invalid values are treated as the default value.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineAttribute-endPoint(value: Array<any>): LineAttribute--><!--Device-LineAttribute-endPoint(value: Array<any>): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;any&gt; | Yes | Coordinates (relative coordinates) of the end point of the line, in vp.<br>Default value: **[0, 0]**<br>The **undefined** and **null** values are treated as the default value. |

## startPoint

```TypeScript
startPoint(value: Array<any>)
```

Sets the coordinates (relative coordinates) of the start point of the line. This attribute can be dynamically set using attributeModifier. Invalid values are treated as the default value.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineAttribute-startPoint(value: Array<any>): LineAttribute--><!--Device-LineAttribute-startPoint(value: Array<any>): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;any&gt; | Yes | Coordinates (relative coordinates) of the start point of the line, in vp.<br>Default value: **[0, 0]**<br>The **undefined** and **null** values are treated as the default value. |

