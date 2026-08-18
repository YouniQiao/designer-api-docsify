# UserAgentMetadata

UserAgentMetadata is a class in the ArkWeb framework used to configure the complete metadata for User-Agent Client Hints. User-Agent Client Hints is a modern HTTP request header mechanism that reports client information to the server through a set of Sec-CH-UA series headers, replacing the traditional User-Agent string to achieve more secure and more granular browser identity identification. Through UserAgentMetadata, apps can customize all client information fields reported by the Web component to the server.

**Since:** 24

<!--Device-webview-class UserAgentMetadata--><!--Device-webview-class UserAgentMetadata-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## getArchitecture

```TypeScript
getArchitecture(): string
```

Obtains the architecture type of the platform. If the corresponding [setArchitecture](#setarchitecture) is not called for configuration, the default value of the architecture type is: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getArchitecture(): string--><!--Device-UserAgentMetadata-getArchitecture(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getBitness

```TypeScript
getBitness(): string
```

Obtains the bitness type of the platform. If the corresponding [setBitness](#setbitness) is not called for configuration, the default value of the bitness type is: Desktop: "64", other devices: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getBitness(): string--><!--Device-UserAgentMetadata-getBitness(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getBrandVersionList

```TypeScript
getBrandVersionList(): Array<UserAgentBrandVersion>
```

Obtains the brand and version information list. If the corresponding [setBrandVersionList](#setbrandversionlist) is not called for configuration, the default value of the list is: [{"brand":"Chromium","version":[ChromeCompatibleVersion](../../../web/web-default-userAgent.md#default-user-agent-structure)}, {"brand":"ArkWeb","version":[OSVersion](../../../web/web-default-userAgent.md#default-user-agent-structure)}].

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>--><!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; |

## getFormFactors

```TypeScript
getFormFactors(): Array<UserAgentFormFactor>
```

Obtains the device form factor information, such as phone and tablet. If the corresponding [setFormFactors](#setformfactors) is not called for configuration, the default value of the form factor information is: Phone: "Mobile", Watch: "Watch", Automotive: "Automotive", PC: "Desktop" , Tablet: "Tablet".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>--><!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; |

## getFullVersion

```TypeScript
getFullVersion(): string
```

Obtains the full version number. If the corresponding [setFullVersion](#setfullversion) is not called for configuration, the default value of the version number is: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getFullVersion(): string--><!--Device-UserAgentMetadata-getFullVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMobile

```TypeScript
getMobile(): boolean
```

Obtains whether the device is a mobile device. If the corresponding [setMobile](#setmobile) is not called for configuration, the default value is: Phone: true, Watch, Automotive, Tablet, Large screen: false.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getMobile(): boolean--><!--Device-UserAgentMetadata-getMobile(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getModel

```TypeScript
getModel(): string
```

Obtains the device model. If the corresponding [setModel](#setmodel) is not called for configuration, the default value of the model is: Phone: obtains the device model based on const.product.model; Watch, Large screen, Automotive, PC, Tablet: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getModel(): string--><!--Device-UserAgentMetadata-getModel(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPlatform

```TypeScript
getPlatform(): string
```

Obtains the operating system name. If the corresponding [setPlatform](#setplatform) is not called for configuration, the default value of the name is: "OpenHarmony".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getPlatform(): string--><!--Device-UserAgentMetadata-getPlatform(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPlatformVersion

```TypeScript
getPlatformVersion(): string
```

Obtains the operating system version number. If the corresponding [setPlatformVersion](#setplatformversion) is not called for configuration, the default value of the version number is: follows the OpenHarmony platform version number rules, same as const.product.os.dist.version.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getPlatformVersion(): string--><!--Device-UserAgentMetadata-getPlatformVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getWow64

```TypeScript
getWow64(): boolean
```

Obtains whether the binary file is running in 32-bit mode on 64-bit Windows. If the corresponding [setWow64](#setwow64) is not called for configuration, the default value is false.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getWow64(): boolean--><!--Device-UserAgentMetadata-getWow64(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setArchitecture

```TypeScript
setArchitecture(arch: string): void
```

Sets the architecture type of the platform.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setArchitecture(arch: string): void--><!--Device-UserAgentMetadata-setArchitecture(arch: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arch | string | Yes |

## setBitness

```TypeScript
setBitness(bitness: string): void
```

Sets the bitness type of the platform.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setBitness(bitness: string): void--><!--Device-UserAgentMetadata-setBitness(bitness: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bitness | string | Yes |

## setBrandVersionList

```TypeScript
setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void
```

Sets the brand and version information.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void--><!--Device-UserAgentMetadata-setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brandVersionList | Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; | Yes |

## setFormFactors

```TypeScript
setFormFactors(formFactors: Array<UserAgentFormFactor>): void
```

Sets the device form, such as the mobile phone or tablet.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setFormFactors(formFactors: Array<UserAgentFormFactor>): void--><!--Device-UserAgentMetadata-setFormFactors(formFactors: Array<UserAgentFormFactor>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formFactors | Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; | Yes |

## setFullVersion

```TypeScript
setFullVersion(fullVersion: string): void
```

Sets the full version number.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setFullVersion(fullVersion: string): void--><!--Device-UserAgentMetadata-setFullVersion(fullVersion: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullVersion | string | Yes |

## setMobile

```TypeScript
setMobile(isMobile: boolean): void
```

Sets whether the device is a mobile device.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setMobile(isMobile: boolean): void--><!--Device-UserAgentMetadata-setMobile(isMobile: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMobile | boolean | Yes |

## setModel

```TypeScript
setModel(model: string): void
```

Sets the device model.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setModel(model: string): void--><!--Device-UserAgentMetadata-setModel(model: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | string | Yes |

## setPlatform

```TypeScript
setPlatform(platform: string): void
```

Sets the OS name.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setPlatform(platform: string): void--><!--Device-UserAgentMetadata-setPlatform(platform: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| platform | string | Yes |

## setPlatformVersion

```TypeScript
setPlatformVersion(platformVersion: string): void
```

Sets the OS version.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setPlatformVersion(platformVersion: string): void--><!--Device-UserAgentMetadata-setPlatformVersion(platformVersion: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| platformVersion | string | Yes |

## setWow64

```TypeScript
setWow64(isWow64: boolean): void
```

Sets whether the binary file runs in 32-bit mode on a 64-bit Windows.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void--><!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isWow64 | boolean | Yes |
