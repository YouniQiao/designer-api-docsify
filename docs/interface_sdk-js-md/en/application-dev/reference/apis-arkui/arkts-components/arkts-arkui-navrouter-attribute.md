# NavRouter properties/events

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** NavRouterAttribute extends CommonMethod<NavRouterAttribute>

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 13

**Substitutes:** NavPathStack

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## mode

```TypeScript
mode(mode: NavRouteMode)
```

Sets the route mode used for redirecting the user from the **NavRouter** component to the specified navigation destination page.

> **NOTE：**

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Deprecated since:** 13

**Substitutes:** LaunchMode

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mode](#mode) | [NavRouteMode](arkts-arkui-navroutemode-e.md) | Yes |

## onStateChange

```TypeScript
onStateChange(callback: (isActivated: boolean) => void)
```

Called when the component activation status changes. **onStateChange(true)** is called when the **NavRouter** component is activated and its **NavDestination** child component is loaded. **onStateChange(false)** is called when the **NavDestination** child component is not displayed.

> **NOTE：**

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 13

**Substitutes:** onShown

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (isActivated: boolean) = & gt; void | Yes |
