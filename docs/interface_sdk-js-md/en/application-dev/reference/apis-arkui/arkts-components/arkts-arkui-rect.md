# Rect

The **Rect** component is used to draw a rectangle. > **NOTE** > > This component supports dynamic constructor parameter updates using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md) class since API version 20. > > **Child Components** > > None

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Use new function to create Rect. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Rect options |

## Rect

```TypeScript
Rect(
    options?: RectOptions | RoundedRectOptions,
  )
```

Defines the constructor of Rect component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectOptions](arkts-arkui-rectoptions-i.md) \| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | No | Options of the rectangle.  The **undefined** and **null** values are treated as invalid and will not take effect. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RectOptions](arkts-arkui-rectoptions-i.md) | Describes the options of the rectangle. |
| [RoundedRectOptions](arkts-arkui-roundedrectoptions-i.md) | Describes the options of the rounded rectangle. |
