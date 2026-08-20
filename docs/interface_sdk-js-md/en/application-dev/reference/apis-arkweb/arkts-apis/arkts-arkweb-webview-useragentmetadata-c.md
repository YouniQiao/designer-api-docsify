# UserAgentMetadata

UserAgentMetadata is a class in the ArkWeb framework used to configure the complete metadata for User-Agent Client Hints. User-Agent Client Hints is a modern HTTP request header mechanism that reports client information to the server through a set of Sec-CH-UA series headers, replacing the traditional User-Agent string to achieve more secure and more granular browser identity identification. Through UserAgentMetadata, apps can customize all client information fields reported by the Web component to the server.

**Since:** 24

<!--Device-webview-class UserAgentMetadata--><!--Device-webview-class UserAgentMetadata-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getArchitecture

```TypeScript
getArchitecture(): string
```

Obtains the architecture type of the platform. If the corresponding [setArchitecture](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setarchitecture) is not called for configuration, the default value of the architecture type is: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getArchitecture(): string--><!--Device-UserAgentMetadata-getArchitecture(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Platform architecture type. |

## getBitness

```TypeScript
getBitness(): string
```

Obtains the bitness type of the platform. If the corresponding [setBitness](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setbitness) is not called for configuration, the default value of the bitness type is: Desktop: "64", other devices: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getBitness(): string--><!--Device-UserAgentMetadata-getBitness(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Bitness type of the platform. |

## getBrandVersionList

```TypeScript
getBrandVersionList(): Array<UserAgentBrandVersion>
```

Obtains the brand and version information list. If the corresponding [setBrandVersionList](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setbrandversionlist) is not called for configuration, the default value of the list is: [{"brand":"Chromium","version":[ChromeCompatibleVersion](../../../web/web-default-userAgent.md#default-user-agent-structure)}, {"brand":"ArkWeb","version":[OSVersion](../../../web/web-default-userAgent.md#default-user-agent-structure)}].

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>--><!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[UserAgentBrandVersion](../../apis-default/arkts-apis/arkts-webview-useragentbrandversion-c.md)&gt; | Brand and version information list. |

## getFormFactors

```TypeScript
getFormFactors(): Array<UserAgentFormFactor>
```

Obtains the device form factor information, such as phone and tablet. If the corresponding [setFormFactors](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setformfactors) is not called for configuration, the default value of the form factor information is: Phone: "Mobile", Watch: "Watch", Automotive: "Automotive", PC: "Desktop" , Tablet: "Tablet".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>--><!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[UserAgentFormFactor](../../apis-default/arkts-apis/arkts-webview-useragentformfactor-e.md)&gt; | Device form information. |

## getFullVersion

```TypeScript
getFullVersion(): string
```

Obtains the full version number. If the corresponding [setFullVersion](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setfullversion) is not called for configuration, the default value of the version number is: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getFullVersion(): string--><!--Device-UserAgentMetadata-getFullVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Full version number. |

## getMobile

```TypeScript
getMobile(): boolean
```

Obtains whether the device is a mobile device. If the corresponding [setMobile](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setmobile) is not called for configuration, the default value is: Phone: true, Watch, Automotive, Tablet, Large screen: false.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getMobile(): boolean--><!--Device-UserAgentMetadata-getMobile(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the device is a mobile device. **true** means yes; **false** otherwise. |

## getModel

```TypeScript
getModel(): string
```

Obtains the device model. If the corresponding [setModel](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setmodel) is not called for configuration, the default value of the model is: Phone: obtains the device model based on const.product.model; Watch, Large screen, Automotive, PC, Tablet: "".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getModel(): string--><!--Device-UserAgentMetadata-getModel(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Device model. |

## getPlatform

```TypeScript
getPlatform(): string
```

Obtains the operating system name. If the corresponding [setPlatform](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setplatform) is not called for configuration, the default value of the name is: "OpenHarmony".

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getPlatform(): string--><!--Device-UserAgentMetadata-getPlatform(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | OS name. |

## getPlatformVersion

```TypeScript
getPlatformVersion(): string
```

Obtains the operating system version number. If the corresponding [setPlatformVersion](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setplatformversion) is not called for configuration, the default value of the version number is: follows the OpenHarmony platform version number rules, same as const.product.os.dist.version.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getPlatformVersion(): string--><!--Device-UserAgentMetadata-getPlatformVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | OS version. |

## getWow64

```TypeScript
getWow64(): boolean
```

Obtains whether the binary file is running in 32-bit mode on 64-bit Windows. If the corresponding [setWow64](../../apis-default/arkts-apis/arkts-webview-useragentmetadata-c.md#setwow64) is not called for configuration, the default value is false.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentMetadata-getWow64(): boolean--><!--Device-UserAgentMetadata-getWow64(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the binary file runs in 32-bit mode on a 64-bit Windows. **true** means yes; **false** otherwise. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arch | string | Yes | Sec-CH-UA-Arch** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bitness | string | Yes | Corresponds to the Sec-CH-UA-Bitness request header. If empty, the default value of ArkWeb is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brandVersionList | Array&lt;[UserAgentBrandVersion](../../apis-default/arkts-apis/arkts-webview-useragentbrandversion-c.md)&gt; | Yes | Sec-CH-UA-Full-Version-List** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formFactors | Array&lt;[UserAgentFormFactor](../../apis-default/arkts-apis/arkts-webview-useragentformfactor-e.md)&gt; | Yes | Sec-CH-UA-Form-Factor** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullVersion | string | Yes | Sec-CH-UA-Full-Version** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isMobile | boolean | Yes | Whether the device is a mobile device. Corresponds to the Sec-CH-UA-Mobile request header. The value true means the device is a mobile device, and false means the opposite. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | Value of the Sec-CH-UA-Model request header. If empty, the default value of ArkWeb is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| platform | string | Yes | Sec-CH-UA-Platform** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| platformVersion | string | Yes | Sec-CH-UA-Platform-Version** of the request header. If this parameter is left empty, the default ArkWeb value is used. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isWow64 | boolean | Yes | Corresponds to the Sec-CH-UA-WoW64 request header. Whether the binary file is running in 32-bit mode on 64-bit Windows. The value **true** means yes, and **false** means no. |

