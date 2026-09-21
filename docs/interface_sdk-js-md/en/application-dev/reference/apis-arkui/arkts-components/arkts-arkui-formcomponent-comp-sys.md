# FormComponent (System API)

Defines FormComponent Component.

## FormComponent

```TypeScript
FormComponent(value: FormInfo)
```

Set a new value of form info.

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FormInfo](arkts-arkui-formcomponent-comp-forminfo-i-sys.md) | Yes |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ErrorInformation](arkts-arkui-formcomponent-comp-errorinformation-i-sys.md) | Provides the widget error information. |
| [FormCallbackInfo](arkts-arkui-formcomponent-comp-formcallbackinfo-i-sys.md) | Represents the parameters for obtaining a widget ID (**formId**) when querying or uninstalling a widget. |
| [FormInfo](arkts-arkui-formcomponent-comp-forminfo-i-sys.md) | Provides the widget information. |
| [FormSize](arkts-arkui-formcomponent-comp-formsize-i-sys.md) | Provides the widget size information. |

### Enums

| Name | Description |
| --- | --- |
| [FormColorMode](arkts-arkui-formcomponent-comp-formcolormode-e-sys.md) | Enumerates the card color modes. |
| [FormDimension](arkts-arkui-formcomponent-comp-formdimension-e-sys.md) | Enumerates widget sizes. |
| [FormRenderingMode](arkts-arkui-formcomponent-comp-formrenderingmode-e-sys.md) | Enumerates the widget rendering modes. |
| [FormShape](arkts-arkui-formcomponent-comp-formshape-e-sys.md) | Defines the FormShape enum. |

## Examples

```TypeScript
Widget example

This example creates a 2 x 2 widget and registers event callbacks.
```
