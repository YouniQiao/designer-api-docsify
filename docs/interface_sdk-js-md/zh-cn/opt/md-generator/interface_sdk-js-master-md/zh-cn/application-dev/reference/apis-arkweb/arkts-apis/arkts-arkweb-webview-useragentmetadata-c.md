# UserAgentMetadata

UserAgentMetadata是ArkWeb框架中用于配置User-Agent Client Hints（UA客户端提示）完整元数据的类。User-Agent Client Hints是一种现代化的HTTP请求标头机制，通过一 组Sec-CH-UA系列标头向服务器报告客户端信息，替代传统User-Agent字符串实现更安全、更细粒度的浏览器身份标识。通过UserAgentMetadata，应用可以自定义Web组件向服务器报告的所有客户端信息字段。

**起始版本：** 24

<!--Device-webview-class UserAgentMetadata--><!--Device-webview-class UserAgentMetadata-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## getArchitecture

```TypeScript
getArchitecture(): string
```

获取平台的架构类型。不调用对应的[setArchitecture](#setarchitecture)设置时，架构类型默认值：""。

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

获取平台的位数类型。不调用对应的[setBitness](#setbitness)设置时，位数类型默认值：Desktop："64"，其他设备：""。

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

获取品牌和版本信息列表。不调用对应的[setBrandVersionList](#setbrandversionlist)进行设置时，列表默认值： [{"brand":"Chromium","version":[ChromeCompatibleVersion](../../../web/web-default-userAgent.md#默认user-agent结构)}, {"brand":"ArkWeb","version":[OSVersion](../../../web/web-default-userAgent.md#默认user-agent结构)}]。

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

获取设备形态信息，如手机、平板等。不调用对应的[setFormFactors](#setformfactors)进行设置时，形态信息默认值：手机："Mobile"、 手表："Watch"、车机："Automotive"、PC："Desktop"、平板："Tablet"。

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

获取完整版本号。不调用对应的[setFullVersion](#setfullversion)设置时，版本号默认值：""。

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

获取是否为移动设备。不调用对应的[setMobile](#setmobile)设置时，默认值：手机: true，手表、车机、平板、大屏: false。

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

获取设备型号。不调用对应的[setModel](#setmodel)设置时，型号默认值：手机根据const.product.model取设备型号；手表、大屏、车机、 PC、平板：""。

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

获取操作系统名称。不调用对应的[setPlatform](#setplatform)设置时，名称默认值："OpenHarmony" 。

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

获取操作系统版本号。不调用对应的[setPlatformVersion](#setplatformversion)设置时，版本号默认值：按OpenHarmony平台 版本号规则，同const.product.os.dist.version。

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

获取二进制文件是否是在64位Windows上以32位模式运行。不调用对应的[setWow64](#setwow64)设置时，默认值为false。

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

设置平台的架构类型。

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

设置平台的位数类型。

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

设置品牌和版本信息。

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

设置设备形态信息，如手机、平板等。

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

设置完整版本号。

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

设置是否为移动设备。

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

设置设备型号。

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

设置操作系统名称。

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

设置操作系统版本号。

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

设置二进制文件是否在64位Windows上以32位模式运行。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void--><!--Device-UserAgentMetadata-setWow64(isWow64: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isWow64 | boolean | 是 |
