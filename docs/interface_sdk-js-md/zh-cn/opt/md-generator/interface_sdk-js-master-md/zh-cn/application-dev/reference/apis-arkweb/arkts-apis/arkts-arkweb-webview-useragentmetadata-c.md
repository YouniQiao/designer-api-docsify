# UserAgentMetadata

Holds User-Agent metadata information and uses to generate User-Agent client hints.

**起始版本：** 24

<!--Device-webview-class UserAgentMetadata--><!--Device-webview-class UserAgentMetadata-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getArchitecture

```TypeScript
getArchitecture(): string
```

Gets the value for sec-ch-ua-architecture.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getArchitecture(): string--><!--Device-UserAgentMetadata-getArchitecture(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getBitness

```TypeScript
getBitness(): string
```

Gets the value for the sec-ch-ua-bitness.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getBitness(): string--><!--Device-UserAgentMetadata-getBitness(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getBrandVersionList

```TypeScript
getBrandVersionList(): Array<UserAgentBrandVersion>
```

Returns the current list of UserAgentBrandVersion which are used to generate the User-Agent client hints sec-ch-ua and sec-ch-ua-full-version-list.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>--><!--Device-UserAgentMetadata-getBrandVersionList(): Array<UserAgentBrandVersion>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; |

## getFormFactors

```TypeScript
getFormFactors(): Array<UserAgentFormFactor>
```

Gets the value for the sec-ch-ua-form-factors.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>--><!--Device-UserAgentMetadata-getFormFactors(): Array<UserAgentFormFactor>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; |

## getFullVersion

```TypeScript
getFullVersion(): string
```

Gets the value for the sec-ch-ua-full-version.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getFullVersion(): string--><!--Device-UserAgentMetadata-getFullVersion(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getMobile

```TypeScript
getMobile(): boolean
```

Gets the value for the sec-ch-ua-mobile.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getMobile(): boolean--><!--Device-UserAgentMetadata-getMobile(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## getModel

```TypeScript
getModel(): string
```

Gets the value for the sec-ch-ua-model.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getModel(): string--><!--Device-UserAgentMetadata-getModel(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getPlatform

```TypeScript
getPlatform(): string
```

Gets the value for the sec-ch-ua-platform.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getPlatform(): string--><!--Device-UserAgentMetadata-getPlatform(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getPlatformVersion

```TypeScript
getPlatformVersion(): string
```

Gets the value for the sec-ch-ua-platform-version.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getPlatformVersion(): string--><!--Device-UserAgentMetadata-getPlatformVersion(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getWow64

```TypeScript
getWow64(): boolean
```

Gets the value for the sec-ch-ua-wow64.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-getWow64(): boolean--><!--Device-UserAgentMetadata-getWow64(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## setArchitecture

```TypeScript
setArchitecture(arch: string): void
```

Sets User-Agent metadata architecture.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty string which means the system default value will be used.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setArchitecture(arch: string): void--><!--Device-UserAgentMetadata-setArchitecture(arch: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arch | string | 是 |

## setBitness

```TypeScript
setBitness(bitness: string): void
```

Sets User-Agent metadata bitness default is "".

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setBitness(bitness: string): void--><!--Device-UserAgentMetadata-setBitness(bitness: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bitness | string | 是 |

## setBrandVersionList

```TypeScript
setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void
```

Sets User-Agent metadata brands and their versions.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is an empty list which means the system default User-Agent metadata brands and versions will be used to generate the User-Agent client hints.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void--><!--Device-UserAgentMetadata-setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brandVersionList | Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; | 是 |

## setFormFactors

```TypeScript
setFormFactors(formFactors: Array<UserAgentFormFactor>): void
```

Sets User-Agent metadata form factors.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty list which means the system default value will be used.Form factor value should be one or more of DESKTOP, AUTOMOTIVE, MOBILE, TABLET, XR, EINK, WATCH.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setFormFactors(formFactors: Array<UserAgentFormFactor>): void--><!--Device-UserAgentMetadata-setFormFactors(formFactors: Array<UserAgentFormFactor>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formFactors | Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; | 是 |

## setFullVersion

```TypeScript
setFullVersion(fullVersion: string): void
```

Sets User-Agent metadata full version.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty string which means the system default value will be used.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setFullVersion(fullVersion: string): void--><!--Device-UserAgentMetadata-setFullVersion(fullVersion: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullVersion | string | 是 |

## setMobile

```TypeScript
setMobile(isMobile: boolean): void
```

Sets User-Agent metadata mobile, default is true.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setMobile(isMobile: boolean): void--><!--Device-UserAgentMetadata-setMobile(isMobile: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMobile | boolean | 是 |

## setModel

```TypeScript
setModel(model: string): void
```

Sets User-Agent metadata model.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty string which means the system default value will be used.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setModel(model: string): void--><!--Device-UserAgentMetadata-setModel(model: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| model | string | 是 |

## setPlatform

```TypeScript
setPlatform(platform: string): void
```

Sets User-Agent metadata platform.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty string which means the system default value will be used.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setPlatform(platform: string): void--><!--Device-UserAgentMetadata-setPlatform(platform: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| platform | string | 是 |

## setPlatformVersion

```TypeScript
setPlatformVersion(platformVersion: string): void
```

Sets User-Agent metadata platform version.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The default value is empty string which means the system default value will be used.&lt;/p&gt;

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setPlatformVersion(platformVersion: string): void--><!--Device-UserAgentMetadata-setPlatformVersion(platformVersion: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| platformVersion | string | 是 |

## setWow64

```TypeScript
setWow64(isWow64: boolean): void
```

Sets User-Agent metadata wow64, default is false.

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void--><!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isWow64 | boolean | 是 |
