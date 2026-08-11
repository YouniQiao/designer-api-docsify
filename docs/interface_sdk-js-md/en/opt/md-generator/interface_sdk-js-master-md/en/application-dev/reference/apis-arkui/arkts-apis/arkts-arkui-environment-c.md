# Environment

For details about how to use environment parameters, see  
[Environment: Device Environment Query](../../../ui/state-management/arkts-environment.md).

## Built-in Environment Variables

| key | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Description |
| -------------------- | --------------- | ------------------------------------------------------------ |
| accessibilityEnabled | string | Whether to enable accessibility. If there is no value of **accessibilityEnabled** in the environment variables, the default value passed through APIs such as **envProp** and **envProps** is added to AppStorage.|
| colorMode | [ColorMode](#ColorMode) | Color mode. The options are as follows:&lt;br&gt;- **ColorMode.LIGHT**: light mode.&lt;br&gt;- **ColorMode.DARK**: dark mode.|
| fontScale | number | Font scale. |
| fontWeightScale | number | Font weight ratio. |
| layoutDirection | [LayoutDirection](arkts-arkui-layoutdirection-e.md) | Layout direction. The options are as follows:&lt;br&gt;- **LayoutDirection.LTR**: from left to right.&lt;br&gt;- **LayoutDirection.RTL**: from right to left.&lt;br&gt;- **Auto**: follows the system settings.|
| languageCode | string | Current system language, which is in lowercase letters, for example, **zh**.

**Since:** 7

<!--Device-unnamed-declare class Environment--><!--Device-unnamed-declare class Environment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EnvProp

```TypeScript
static EnvProp<S>(key: string, value: S): boolean
```

Stores the built-in environment variable key from [Environment](../../../ui/state-management/arkts-environment.md)into [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of the environment variable key is not found in AppStorage, the default value is used and stored in AppStorage. If the value is successfully stored, **true** is returned. If the value of the environment variable key already exists in AppStorage, **false**is returned.

You are advised to call this API when the application is started.

It is incorrect to use AppStorage to read environment variables without calling **EnvProp** first.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [Environment#envProp](arkts-arkui-environment-c.md#envprop)

<!--Device-Environment-static EnvProp<S>(key: string, value: S): boolean--><!--Device-Environment-static EnvProp<S>(key: string, value: S): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | S | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## EnvProps

```TypeScript
static EnvProps(
    props: {
      key: string;
      defaultValue: any;
    }[],
  ): void
```

Works in a way similar to the [EnvProp](arkts-arkui-environment-c.md#envprop) API, with the difference that it allows for initialization of multiple attributes in batches. It is recommended that this API be called during application startup to store system environment variables to [AppStorage](../../../ui/state-management/arkts-appstorage.md) in batches.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [Environment#envProps](arkts-arkui-environment-c.md#envprops)

<!--Device-Environment-static EnvProps(    props: {      key: string;      defaultValue: any;    }[],  ): void--><!--Device-Environment-static EnvProps(    props: {      key: string;      defaultValue: any;    }[],  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| props | {
       key: string;
       defaultValue: any;
     }[] | Yes |  |

## Keys

```TypeScript
static Keys(): Array<string>
```

Returns the property key array of environment variables.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [Environment#keys](arkts-arkui-environment-c.md#keys)

<!--Device-Environment-static Keys(): Array<string>--><!--Device-Environment-static Keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |

## envProp

```TypeScript
static envProp<S>(key: string, value: S): boolean
```

Stores the built-in environment variable key from [Environment](../../../ui/state-management/arkts-environment.md)into [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of the environment variable key is not found in AppStorage, the default value is used and stored in AppStorage. If the value is successfully stored, **true** is returned. If the value of the environment variable key already exists in AppStorage, **false**is returned.

You are advised to call this API when the application is started.

It is incorrect to use AppStorage to read environment variables without calling **envProp** first.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Environment-static envProp<S>(key: string, value: S): boolean--><!--Device-Environment-static envProp<S>(key: string, value: S): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | S | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## envProps

```TypeScript
static envProps(props: EnvPropsOptions[]): void
```

Works in a way similar to the [envProp](arkts-arkui-environment-c.md#envprop) API, with the difference that it allows for initialization of multiple attributes in batches. It is recommended that this API be called during application startup to store system environment variables to [AppStorage](../../../ui/state-management/arkts-appstorage.md) in batches.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Environment-static envProps(props: EnvPropsOptions[]): void--><!--Device-Environment-static envProps(props: EnvPropsOptions[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| props | [EnvPropsOptions](arkts-arkui-envpropsoptions-i.md)[] | Yes |

## keys

```TypeScript
static keys(): Array<string>
```

Returns the property key array of environment variables.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Environment-static keys(): Array<string>--><!--Device-Environment-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |
