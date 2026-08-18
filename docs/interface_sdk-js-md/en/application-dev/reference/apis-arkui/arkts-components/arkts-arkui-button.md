# Button

The **Button** component can be used to create different types of buttons. > **NOTE**

## Child Components This component can contain only one child component.

## Button

```TypeScript
Button()
```

Creates an empty button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(): ButtonAttribute--><!--Device-ButtonInterface-(): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Button

```TypeScript
Button(options: ButtonOptions)
```

Creates a button that can contain a single child component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(options: ButtonOptions): ButtonAttribute--><!--Device-ButtonInterface-(options: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | Yes | Button settings. |

## Button

```TypeScript
Button(label: ResourceStr, options?: ButtonOptions)
```

Creates a button based on text content. In this case, the component cannot contain child components. By default, the text content is displayed in a one line.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonInterface-(label: ResourceStr, options?: ButtonOptions): ButtonAttribute--><!--Device-ButtonInterface-(label: ResourceStr, options?: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | ResourceStr | Yes | Button text.<br>Note: If the text is longer than the width of the button, it is truncated. |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | No | Button settings. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ButtonConfiguration](arkts-arkui-buttonconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from CommonConfiguration. |
| [ButtonOptions](arkts-arkui-buttonoptions-i.md) | Describes the button style. |
| [LabelStyle](arkts-arkui-labelstyle-i.md) | Label text and font style of the button. |

### Types

| Name | Description |
| --- | --- |
| [ButtonTriggerClickCallback](arkts-arkui-buttontriggerclickcallback-t.md) | Defines the callback type used in **ButtonConfiguration**. |

### Enums

| Name | Description |
| --- | --- |
| [ButtonRole](arkts-arkui-buttonrole-e.md) | Role of the button. |
| [ButtonStyleMode](arkts-arkui-buttonstylemode-e.md) | Enumerates the button importance levels. |
| [ButtonType](arkts-arkui-buttontype-e.md) | Enumerates the button types. > **NOTE：**> > - The corner radius of the rounded rectangle button is set using the universal attribute > borderRadius. > > - For a button of the **Capsule** type, the **borderRadius** settings do not take effect, and the radius of its > rounded corner is always half of the button height or width, whichever is smaller. > > - For a button of the **Circle** type: (1) If both its width and height are set, **borderRadius** does not take > effect, and the button radius is half of the width or height (whichever is smaller). (2) If either its width or > height is set, **borderRadius** does not take effect, and the button radius is half of the set width or height. (3) > If neither its width nor height is set, the button radius is as specified by **borderRadius**; if **borderRadius** > is set to a negative value, the value **0** will be used. > > - The button text is set using [fontSize](arkts-arkui-button-attribute.md#fontsize), > [fontColor](arkts-arkui-button-attribute.md#fontcolor), [fontStyle](arkts-arkui-button-attribute.md#fontstyle), > [fontFamily](arkts-arkui-button-attribute.md#fontfamily), and [fontWeight](arkts-arkui-button-attribute.md#fontweight). > > - Before setting the gradient color, you need to set > backgroundColor to transparent. > > - When **borderRadius** is not set, the corner radius of the rounded rectangle button remains at the default value. > In this case, the corner radius does not change with the button height and is subject to the **controlSize** > property. When **controlSize** is **NORMAL**, the corner radius is 20 vp; when **controlSize** is **SMALL**, the > corner radius is 14 vp. > > - When border is set for the > button, a default > borderRadius value is > automatically applied. When both **border** and **borderRadius** attributes are used, **borderRadius** must be > specified after **border** to prevent the border radius from being overridden by the default radius value in the > border style. |
| [ControlSize](arkts-arkui-controlsize-e.md) | Button size. |

