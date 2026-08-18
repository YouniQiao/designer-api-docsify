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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | Yes |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| label | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| options | [ButtonOptions](arkts-arkui-buttonoptions-i.md) | No |

## Summary

- [ButtonConfiguration](arkts-arkui-buttonconfiguration-i.md)
- [ButtonOptions](arkts-arkui-buttonoptions-i.md)
- [LabelStyle](arkts-arkui-labelstyle-i.md)
- [ButtonTriggerClickCallback](arkts-arkui-buttontriggerclickcallback-t.md)
- [ButtonRole](arkts-arkui-buttonrole-e.md)
- [ButtonStyleMode](arkts-arkui-buttonstylemode-e.md)
- [ButtonType](arkts-arkui-buttontype-e.md)
- [ControlSize](arkts-arkui-controlsize-e.md)
