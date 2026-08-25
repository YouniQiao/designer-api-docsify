# Navigator properties/events

Declare navigator properties.

**Inheritance/Implementation:** NavigatorAttribute extends CommonMethod<NavigatorAttribute>

**Since:** 7

**Deprecated since:** 13

**Substitutes:** Navigation

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## active

```TypeScript
active(value: boolean)
```

Sets whether the **Navigator** component is activated. If the component is activated, the corresponding navigation takes effect.

**Since:** 7

**Deprecated since:** 13

**Substitutes:** Navigation

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## params

```TypeScript
params(value: object)
```

Sets the data that needs to be passed to the target page during redirection.

**Since:** 7

**Deprecated since:** 13

**Substitutes:** param

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | object | Yes |

## target

```TypeScript
target(value: string)
```

Sets the path of the target page to be redirected to. The target page must be added to the **main_pages.json** file.

**Since:** 7

**Deprecated since:** 13

**Substitutes:** Navigation

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## type

```TypeScript
type(value: NavigationType)
```

Sets the navigation type.

**Since:** 7

**Deprecated since:** 13

**Substitutes:** Navigation

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NavigationType](arkts-arkui-navigationtype-e.md) | Yes |
