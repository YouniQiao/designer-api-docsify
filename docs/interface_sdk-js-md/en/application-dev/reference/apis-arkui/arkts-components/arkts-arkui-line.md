# Line

The **Line** component is used to draw a straight line. > **NOTE** > > This component supports dynamic constructor parameter updates using the > updateConstructorParams API of the > AttributeUpdater class since API version 20. > > **Child Components** > > None

## Line

```TypeScript
Line(options?: LineOptions)
```

Uses new to create the line. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineInterface-new (options?: LineOptions): LineAttribute--><!--Device-LineInterface-new (options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-lineoptions-i.md) | No | Line options |

## Line

```TypeScript
Line(options?: LineOptions)
```

Defines the constructor of Line component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LineInterface-(options?: LineOptions): LineAttribute--><!--Device-LineInterface-(options?: LineOptions): LineAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LineOptions](arkts-arkui-lineoptions-i.md) | No | Options of the line.<br>The **undefined** and **null** values are treated as invalid and will not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [LineOptions](arkts-arkui-lineoptions-i.md) | Describes the options of the line. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element's &gt; @since version number is higher than inner elements'. This does not affect interface usability. |

