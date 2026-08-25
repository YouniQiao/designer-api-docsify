# ResourceManager

Provides the capability of accessing application resources and system resources. The accessible resources include the resources in the HAP/HSP module corresponding to the current context and all system resources.

> **NOTE：**&gt;
> - The methods involved in **ResourceManager** are applicable only to the TypeScript-based declarative
> development paradigm.&gt;
> - Resource files are defined in the **resources** directory of the project. You can obtain resource values such
> as strings, string arrays, and colors based on the specified **resName**, **resId**, or **Resource** object.
> **resName** indicates the resource name, **resId** indicates the resource ID, which can be obtained through
> `\$r(*resource-address*).id`, for example, `\$r('app.string.test').id`.&gt;
> - No matter whether resources are in the same HAP or different HAPs or HSPs, you are advised to use the API with
> **resName** or **resId** specified. Using the **Resource** object will take a longer time. If the resources are
> in different HAPs or HSPs, you first need to use
> [createModuleContext](../../apis-ability-kit/arkts-apis/arkts-ability-application-createmodulecontext-f.md) to create the context
> of the corresponding module and then call the API with **resName** or **resId** specified. For more information,
> see [Accessing Resources](../../../quick-start/resource-categories-and-access.md#accessing-resources).&gt;
> - In API version 22 and earlier versions, an exception is thrown due to an invalid ID when the intermediate-code
> HAR or bytecode HAR accesses resources through resource ID-related APIs. From API version 23, the intermediate-
> code HAR or bytecode HAR can properly access resources through resource ID-related APIs. For details, see
> [Accessing Resources](../../../quick-start/resource-categories-and-access.md#accessing-resources).

**Since:** 6

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## addResource

```TypeScript
addResource(path: string) : void
```

Loads the specified overlay resource during application runtime to implement theme switching or resource overriding.

> **NOTE：**&gt;
> Resource overwriting is not supported for the **rawfile** and **resfile** directories.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001010](../errorcode-resource-manager.md#9001010-invalid-overlay-path) |

## closeRawFd

```TypeScript
closeRawFd(path: string, callback: _AsyncCallback<void>): void
```

Closes the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | _AsyncCallback & lt;void & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## closeRawFd

```TypeScript
closeRawFd(path: string): Promise<void>
```

Closes the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## closeRawFdSync

```TypeScript
closeRawFdSync(path: string): void
```

Closes the file descriptor (fd) of the HAP where the **rawfile** file in the **resources/rawfile** directory is located. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## closeRawFileDescriptor

```TypeScript
closeRawFileDescriptor(path: string, callback: AsyncCallback<void>): void
```

Closes the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [closeRawFd](#closerawfd)(path: string, callback: _AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | AsyncCallback & lt;void & gt; | Yes |

## closeRawFileDescriptor

```TypeScript
closeRawFileDescriptor(path: string): Promise<void>
```

Closes the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [closeRawFd](#closerawfd)(path: string)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## getBoolean

```TypeScript
getBoolean(resId: number): boolean
```

Obtains a Boolean value based on the specified resource ID. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getBoolean

```TypeScript
getBoolean(resource: Resource): boolean
```

Obtains a Boolean value based on the specified resource object. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getBoolean](#getboolean)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getBooleanByName

```TypeScript
getBooleanByName(resName: string): boolean
```

Obtains a Boolean value based on the specified resource name. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColor

```TypeScript
getColor(resId: number, callback: _AsyncCallback<number>): void
```

Obtains the color value corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | _AsyncCallback & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColor

```TypeScript
getColor(resId: number): Promise<number>
```

Obtains the color value corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColor

```TypeScript
getColor(resource: Resource, callback: _AsyncCallback<number>): void
```

Obtains the color value corresponding to the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getColor](#getcolor)(resId: long, callback: _AsyncCallback&lt;long&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| callback | _AsyncCallback & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColor

```TypeScript
getColor(resource: Resource): Promise<number>
```

Obtains the color value corresponding to the specified resource object. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getColor](#getcolor)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColorByName

```TypeScript
getColorByName(resName: string, callback: _AsyncCallback<number>): void
```

Obtains the color value corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| callback | _AsyncCallback & lt;number & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColorByName

```TypeScript
getColorByName(resName: string): Promise<number>
```

Obtains the color value corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColorByNameSync

```TypeScript
getColorByNameSync(resName: string) : number
```

Obtains a color value based on the specified resource name. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColorSync

```TypeScript
getColorSync(resId: number) : number
```

Obtains a color value based on the specified resource ID. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getColorSync

```TypeScript
getColorSync(resource: Resource) : number
```

Obtains a color value based on the specified resource object. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getColorSync](#getcolorsync)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getConfiguration

```TypeScript
getConfiguration(callback: _AsyncCallback<Configuration>): void
```

Obtains the configuration of a device. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | _AsyncCallback & lt;Configuration & gt; | Yes |

## getConfiguration

```TypeScript
getConfiguration(): Promise<Configuration>
```

Obtains the configuration of a device. This API uses a promise to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Configuration & gt; |

## getConfigurationSync

```TypeScript
getConfigurationSync(): Configuration
```

Obtains the device configuration. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) |

## getDeviceCapability

```TypeScript
getDeviceCapability(callback: _AsyncCallback<DeviceCapability>): void
```

Obtains the device capabilities of a device. This API uses an asynchronous callback to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | _AsyncCallback & lt;DeviceCapability & gt; | Yes |

## getDeviceCapability

```TypeScript
getDeviceCapability(): Promise<DeviceCapability>
```

Obtains the device capabilities of a device. This API uses a promise to return the result.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DeviceCapability & gt; |

## getDeviceCapabilitySync

```TypeScript
getDeviceCapabilitySync(): DeviceCapability
```

Obtains the device capability. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceCapability](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-partneragent-devicecapability-i.md) |

## getDoublePluralStringByNameSync

```TypeScript
getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource name, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).&gt;
> - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
> example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001008](../errorcode-resource-manager.md#9001008-failed-to-format-the-resource-obtained-based-on-resname) |

## getDoublePluralStringValueSync

```TypeScript
getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource ID, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).&gt;
> - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
> example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getDoublePluralStringValueSync

```TypeScript
getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource object, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [getDoublePluralStringValueSync](#getdoublepluralstringvaluesync)(resId: number, num: number, ...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getDrawableDescriptor

```TypeScript
getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor
```

Obtains the **DrawableDescriptor** object for icon display corresponding to the specified resource ID. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | No |
| type | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getDrawableDescriptor

```TypeScript
getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor
```

Obtains a **DrawableDescriptor** object for icon display based on the specified resource object. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getDrawableDescriptor](#getdrawabledescriptor)(resId: long, density?: int, type?: int)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | No |
| type | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getDrawableDescriptorByName

```TypeScript
getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor
```

Obtains the **DrawableDescriptor** object for icon display corresponding to the specified resource name. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | No |
| type | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getIntPluralStringByNameSync

```TypeScript
getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource name, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).&gt;
> - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
> example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001008](../errorcode-resource-manager.md#9001008-failed-to-format-the-resource-obtained-based-on-resname) |

## getIntPluralStringValueSync

```TypeScript
getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource ID, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).&gt;
> - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
> example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getIntPluralStringValueSync

```TypeScript
getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string
```

Obtains the [plural](../../../internationalization/l10n-singular-plural.md) string corresponding to the specified resource object, and replaces the format placeholders in the string in sequence using the **args** parameters. This API returns the result synchronously.

> **NOTE：**&gt;
> - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| num | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getLocales

```TypeScript
getLocales(includeSystem?: boolean): Array<string>
```

Obtains the language list of an application.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| includeSystem | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getMedia

```TypeScript
getMedia(resId: number, callback: AsyncCallback<Uint8Array>): void
```

Obtains the content of the media file corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long, callback: _AsyncCallback&lt;Uint8Array&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | AsyncCallback & lt;Uint8Array & gt; | Yes |

## getMedia

```TypeScript
getMedia(resId: number): Promise<Uint8Array>
```

Obtains the content of the media file corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## getMediaBase64

```TypeScript
getMediaBase64(resId: number, callback: AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | AsyncCallback & lt;string & gt; | Yes |

## getMediaBase64

```TypeScript
getMediaBase64(resId: number): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, density: number, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource for the specified screen density corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaBase64ByName

```TypeScript
getMediaBase64ByName(resName: string, density: number): Promise<string>
```

Obtains the Base64 encoding of the image resource for the specified screen density corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaBase64ByNameSync

```TypeScript
getMediaBase64ByNameSync(resName: string, density?: number): string
```

Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource name. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the content of the media file corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, density: number, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the media file content for the specified screen density based on the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaByName

```TypeScript
getMediaByName(resName: string): Promise<Uint8Array>
```

Obtains the content of the media file corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaByName

```TypeScript
getMediaByName(resName: string, density: number): Promise<Uint8Array>
```

Obtains the media file content for the specified screen density based on the specified resource name. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaByNameSync

```TypeScript
getMediaByNameSync(resName: string, density?: number): Uint8Array
```

Obtains the media file content for the default or specified screen density based on the specified resource name. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the content of the media file corresponding to the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long, callback: _AsyncCallback&lt;Uint8Array&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, density: number, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the media file content for the specified screen density based on the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long, density: int, callback: _AsyncCallback&lt;Uint8Array&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource): Promise<Uint8Array>
```

Obtains the content of the media file corresponding to the specified resource object. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resource: Resource, density: number): Promise<Uint8Array>
```

Obtains the media file content for the specified screen density based on the specified resource object. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContent](#getmediacontent)(resId: long, density: int)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the content of the media file corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, density: number, callback: _AsyncCallback<Uint8Array>): void
```

Obtains the media file content for the specified screen density based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resId: number): Promise<Uint8Array>
```

Obtains the content of the media file corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContent

```TypeScript
getMediaContent(resId: number, density: number): Promise<Uint8Array>
```

Obtains the media file content for the specified screen density based on the specified resource ID. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, density: number, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource object and the specified screen density. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long, density: int, callback: _AsyncCallback&lt;string&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource object. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resource: Resource, density: number): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource object and the specified screen density. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContentBase64](#getmediacontentbase64)(resId: long, density: int)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, density: number, callback: _AsyncCallback<string>): void
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID and the specified screen density. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64

```TypeScript
getMediaContentBase64(resId: number, density: number): Promise<string>
```

Obtains the Base64 encoding of the image resource corresponding to the specified resource ID and the specified screen density. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64Sync

```TypeScript
getMediaContentBase64Sync(resId: number, density?: number): string
```

Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource ID. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentBase64Sync

```TypeScript
getMediaContentBase64Sync(resource: Resource, density?: number): string
```

Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource object. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContentBase64Sync](#getmediacontentbase64sync)(resId: long, density?: int)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentSync

```TypeScript
getMediaContentSync(resId: number, density?: number): Uint8Array
```

Obtains the media file content for the default or specified screen density based on the specified resource ID. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getMediaContentSync

```TypeScript
getMediaContentSync(resource: Resource, density?: number): Uint8Array
```

Obtains the media file content for the default or specified screen density based on the specified resource object. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getMediaContentSync](#getmediacontentsync)(resId: long, density?: int)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| density | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |

## getNumber

```TypeScript
getNumber(resId: number): number
```

Obtains an integer or float number based on the specified resource ID. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getNumber

```TypeScript
getNumber(resource: Resource): number
```

Obtains an integer or float number based on the specified resource object. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getNumber](#getnumber)(resId: number)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getNumberByName

```TypeScript
getNumberByName(resName: string): number
```

Obtains an integer or float number based on the specified resource name. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getOverrideConfiguration

```TypeScript
getOverrideConfiguration(): Configuration
```

Obtains the configuration of differentiated resources. This API returns the result synchronously.For both the common resource management object and the differentiated resource management object obtained through the [getOverrideResourceManager](#getoverrideresourcemanager) API, this API returns the same configuration information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) |

## getOverrideResourceManager

```TypeScript
getOverrideResourceManager(configuration?: Configuration): ResourceManager
```

Obtains a **ResourceManager** object for loading differentiated resources. This API returns the result synchronously.The resource configuration (including the language, color mode, resolution, and orientation) obtained by a common **ResourceManager** object is determined by the system. With this API, an application can obtain resources of the specified configuration (that is, differentiated resources), for example, dark color resources in light color mode.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configuration | [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getPluralString

```TypeScript
getPluralString(resId: number, num: number, callback: AsyncCallback<string>): void
```

Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getPluralStringValue](#getpluralstringvalue)(resId: number, num: number, callback: _AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |
| callback | AsyncCallback & lt;string & gt; | Yes |

## getPluralString

```TypeScript
getPluralString(resId: number, num: number): Promise<string>
```

Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses a promise to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getPluralStringValue](#getpluralstringvalue)(resId: number, num: number)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getPluralStringByName

```TypeScript
getPluralStringByName(resName: string, num: number, callback: _AsyncCallback<string>): void
```

Obtains the plural string based on the specified resource name and the specified resource quantity. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| num | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringByName

```TypeScript
getPluralStringByName(resName: string, num: number): Promise<string>
```

Obtains the plural string based on the specified resource name and the specified resource quantity. This API uses a promise to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringByNameSync

```TypeScript
getPluralStringByNameSync(resName: string, num: number): string
```

Obtains singular/plural strings based on the specified quantity and resource name. This API returns the result synchronously.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringByNameSync](#getintpluralstringbynamesync)(resName: string, num: number, ...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resource: Resource, num: number, callback: _AsyncCallback<string>): void
```

Obtains the plural string based on the specified resource information and the specified resource quantity. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| num | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resource: Resource, num: number): Promise<string>
```

Obtains the plural string based on the specified resource information and the specified resource quantity. This API uses a promise to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resId: number, num: number, callback: _AsyncCallback<string>): void
```

Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValue

```TypeScript
getPluralStringValue(resId: number, num: number): Promise<string>
```

Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses a promise to return the result.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValueSync

```TypeScript
getPluralStringValueSync(resId: number, num: number): string
```

Obtains singular/plural strings based on the specified resource ID and quantity. This API returns the result synchronously.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getPluralStringValueSync

```TypeScript
getPluralStringValueSync(resource: Resource, num: number): string
```

Obtains singular/plural strings based on the specified quantity and resource object. This API returns the result synchronously.

> **NOTE：**&gt;
> Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
> [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [getIntPluralStringValueSync](#getintpluralstringvaluesync)(resId: number, num: number,...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getRawFd

```TypeScript
getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>): void
```

Obtains the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> To prevent resource leakage, call [closeRawFdSync](#closerawfdsync) or
> [closeRawFd](#closerawfd)
> to close the fd after use.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | _AsyncCallback & lt;RawFileDescriptor & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFd

```TypeScript
getRawFd(path: string): Promise<RawFileDescriptor>
```

Obtains the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses a promise to return the result.

> **NOTE：**&gt;
> To prevent resource leakage, call [closeRawFdSync](#closerawfdsync) or
> [closeRawFd](#closerawfd)
> to close the fd after use.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;RawFileDescriptor & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFdSync

```TypeScript
getRawFdSync(path: string): RawFileDescriptor
```

Obtains the file descriptor (fd) of the HAP where the rawfile file in the resources/rawfile directory is located. This API is called in synchronous mode.

> **NOTE：**&gt;
> To prevent resource leakage, call [closeRawFdSync](#closerawfdsync) or
> [closeRawFd](#closerawfd)
> to close the fd after use.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFile

```TypeScript
getRawFile(path: string, callback: AsyncCallback<Uint8Array>): void
```

Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRawFileContent](#getrawfilecontent)(path: string, callback: _AsyncCallback&lt;Uint8Array&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | AsyncCallback & lt;Uint8Array & gt; | Yes |

## getRawFile

```TypeScript
getRawFile(path: string): Promise<Uint8Array>
```

Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRawFileContent](#getrawfilecontent)(path: string)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## getRawFileContent

```TypeScript
getRawFileContent(path: string, callback: _AsyncCallback<Uint8Array>): void
```

Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | _AsyncCallback & lt;Uint8Array & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFileContent

```TypeScript
getRawFileContent(path: string): Promise<Uint8Array>
```

Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFileContentSync

```TypeScript
getRawFileContentSync(path: string): Uint8Array
```

Obtains the content of a rawfile in the **resources/rawfile** directory. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFileDescriptor

```TypeScript
getRawFileDescriptor(path: string, callback: AsyncCallback<RawFileDescriptor>): void
```

Obtains the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRawFd](#getrawfd)(path: string, callback: _AsyncCallback&lt;RawFileDescriptor&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | AsyncCallback & lt;RawFileDescriptor & gt; | Yes |

## getRawFileDescriptor

```TypeScript
getRawFileDescriptor(path: string): Promise<RawFileDescriptor>
```

Obtains the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRawFd](#getrawfd)(path: string)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;RawFileDescriptor & gt; |

## getRawFileList

```TypeScript
getRawFileList(path: string, callback: _AsyncCallback<Array<string>>): void
```

Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
> directory, the list of the folders and files is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFileList

```TypeScript
getRawFileList(path: string): Promise<Array<string>>
```

Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API uses a promise to return the result.

> **NOTE：**&gt;
> If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
> directory, the list of the folders and files is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getRawFileListSync

```TypeScript
getRawFileListSync(path: string): Array<string>
```

Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API returns the result synchronously.

> **NOTE：**&gt;
> If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
> directory, the list of the folders and files is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## getResourceName

```TypeScript
getResourceName(resId: number): string
```

Obtains the resource name corresponding to the specified resource ID.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |

## getString

```TypeScript
getString(resId: number, callback: AsyncCallback<string>): void
```

Obtains the string corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getStringValue](#getstringvalue)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | AsyncCallback & lt;string & gt; | Yes |

## getString

```TypeScript
getString(resId: number): Promise<string>
```

Obtains the string corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getStringValue](#getstringvalue)(resId: long)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getStringArray

```TypeScript
getStringArray(resId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains the string array corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getStringArrayValue](#getstringarrayvalue)(resId: long, callback: _AsyncCallback&lt;Array&lt;string&gt;&gt;)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | AsyncCallback & lt;Array & lt;string & gt; & gt; | Yes |

## getStringArray

```TypeScript
getStringArray(resId: number): Promise<Array<string>>
```

Obtains the string array corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getStringArrayValue](#getstringarrayvalue)(resId: long)

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getStringArrayByName

```TypeScript
getStringArrayByName(resName: string, callback: _AsyncCallback<Array<string>>): void
```

Obtains the string array corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayByName

```TypeScript
getStringArrayByName(resName: string): Promise<Array<string>>
```

Obtains the string array corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayByNameSync

```TypeScript
getStringArrayByNameSync(resName: string): Array<string>
```

Obtains the string array corresponding to the specified resource name. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resource: Resource, callback: _AsyncCallback<Array<string>>): void
```

Obtains the string array corresponding to the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getStringArrayValue](#getstringarrayvalue)(resId: long, callback: _AsyncCallback&lt;Array&lt;string&gt;&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resource: Resource): Promise<Array<string>>
```

Obtains the string array corresponding to the specified resource object. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getStringArrayValue](#getstringarrayvalue)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resId: number, callback: _AsyncCallback<Array<string>>): void
```

Obtains the string array corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | _AsyncCallback & lt;Array & lt;string & gt; & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValue

```TypeScript
getStringArrayValue(resId: number): Promise<Array<string>>
```

Obtains the string array corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValueSync

```TypeScript
getStringArrayValueSync(resId: number): Array<string>
```

Obtains the string array corresponding to the specified resource ID. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringArrayValueSync

```TypeScript
getStringArrayValueSync(resource: Resource): Array<string>
```

Obtains a string array based on the specified resource object. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getStringArrayValueSync](#getstringarrayvaluesync)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringByName

```TypeScript
getStringByName(resName: string, callback: _AsyncCallback<string>): void
```

Obtains the string corresponding to the specified resource name. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringByName

```TypeScript
getStringByName(resName: string): Promise<string>
```

Obtains the string corresponding to the specified resource name. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringByNameSync

```TypeScript
getStringByNameSync(resName: string): string
```

Obtains the string corresponding to the specified resource name. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringByNameSync

```TypeScript
getStringByNameSync(resName: string, ...args: Array<string | number>): string
```

Obtains the string corresponding to the specified resource name, and replaces the format placeholders in the string in sequence using the **args** parameter. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001008](../errorcode-resource-manager.md#9001008-failed-to-format-the-resource-obtained-based-on-resname) |

## getStringSync

```TypeScript
getStringSync(resId: number): string
```

Obtains the string corresponding to the specified resource ID. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringSync

```TypeScript
getStringSync(resId: number, ...args: Array<string | number>): string
```

Obtains the string corresponding to the specified resource ID, and replaces the format placeholders in the string in sequence using the **args** parameter. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getStringSync

```TypeScript
getStringSync(resource: Resource): string
```

Obtains a string based on the specified resource object. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getStringSync](#getstringsync)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringSync

```TypeScript
getStringSync(resource: Resource, ...args: Array<string | number>): string
```

Obtains the string corresponding to the specified resource object, and replaces the format placeholders in the string in sequence using the **args** parameter. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getStringSync](#getstringsync)(resId: number, ...args: Array&lt;string | number&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |
| [9001007](../errorcode-resource-manager.md#9001007-failed-to-format-the-resource-obtained-based-on-the-current-id) |

## getStringValue

```TypeScript
getStringValue(resource: Resource, callback: _AsyncCallback<string>): void
```

Obtains the string corresponding to the specified resource object. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getStringValue](#getstringvalue)(resId: long, callback: _AsyncCallback&lt;string&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringValue

```TypeScript
getStringValue(resource: Resource): Promise<string>
```

Obtains the string corresponding to the specified resource object. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 20

**Substitutes:** [getStringValue](#getstringvalue)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringValue

```TypeScript
getStringValue(resId: number, callback: _AsyncCallback<string>): void
```

Obtains the string corresponding to the specified resource ID. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |
| callback | _AsyncCallback & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getStringValue

```TypeScript
getStringValue(resId: number): Promise<string>
```

Obtains the string corresponding to the specified resource ID. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getSymbol

```TypeScript
getSymbol(resId: number) : number
```

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource ID. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getSymbol

```TypeScript
getSymbol(resource: Resource) : number
```

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource object. This API returns the result synchronously.

**Since:** 11

**Deprecated since:** 20

**Substitutes:** [getSymbol](#getsymbol)(resId: long)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001001](../errorcode-resource-manager.md#9001001-invalid-resource-id) |
| [9001002](../errorcode-resource-manager.md#9001002-matching-resource-not-found-based-on-the-current-resource-id) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## getSymbolByName

```TypeScript
getSymbolByName(resName: string) : number
```

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource name. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001003](../errorcode-resource-manager.md#9001003-invalid-resource-name) |
| [9001004](../errorcode-resource-manager.md#9001004-matching-resource-not-found-based-on-the-passed-resource-name) |
| [9001006](../errorcode-resource-manager.md#9001006-circular-reference-in-resources) |

## isRawDir

```TypeScript
isRawDir(path: string): boolean
```

Checks whether a path is a subdirectory in the **rawfile** directory. This API returns the result synchronously.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001005](../errorcode-resource-manager.md#9001005-invalid-relative-path) |

## release

```TypeScript
release()
```

Releases an **resourceManager **object. This API is not supported currently. Calling this API does not have any effect.

**Since:** 7

**Deprecated since:** 12

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

## removeResource

```TypeScript
removeResource(path: string) : void
```

Removes the specified overlay resource during application runtime and restores the original resource before the override.

> **NOTE：**&gt;
> Resource overwriting is not supported for the **rawfile** and **resfile** directories.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9001010](../errorcode-resource-manager.md#9001010-invalid-overlay-path) |

## updateOverrideConfiguration

```TypeScript
updateOverrideConfiguration(configuration: Configuration): void
```

Updates the configuration of a differentiated resource management object.This API updates the configuration of the differentiated resource management object, regardless of whether it is called on the common resource management object or on the differentiated one obtained via [getOverrideResourceManager](#getoverrideresourcemanager).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configuration | [Configuration](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
