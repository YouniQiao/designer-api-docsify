# UserAgentMetadata

UserAgentMetadata是ArkWeb框架中用于配置User-Agent Client Hints（UA客户端提示）完整元数据的类。User-Agent Client Hints是一种现代化的HTTP请求标头机制，通过一 组Sec-CH-UA系列标头向服务器报告客户端信息，替代传统User-Agent字符串实现更安全、更细粒度的浏览器身份标识。通过UserAgentMetadata，应用可以自定义Web组件向服务器报告的所有客户端信息字段。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getArchitecture

```TypeScript
getArchitecture(): string
```

获取平台的架构类型。不调用对应的[setArchitecture](#setarchitecture)设置时，架构类型默认值：""。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getBitness

```TypeScript
getBitness(): string
```

获取平台的位数类型。不调用对应的[setBitness](#setbitness)设置时，位数类型默认值：Desktop："64"，其他设备：""。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getBrandVersionList

```TypeScript
getBrandVersionList(): Array<UserAgentBrandVersion>
```

获取品牌和版本信息列表。不调用对应的[setBrandVersionList](#setbrandversionlist)进行设置时，列表默认值： [{"brand":"Chromium","version":[ChromeCompatibleVersion](../../../web/web-default-userAgent.md#默认user-agent结构)}, {"brand":"ArkWeb","version":[OSVersion](../../../web/web-default-userAgent.md#默认user-agent结构)}]。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getFormFactors

```TypeScript
getFormFactors(): Array<UserAgentFormFactor>
```

获取设备形态信息，如手机、平板等。不调用对应的[setFormFactors](#setformfactors)进行设置时，形态信息默认值：手机："Mobile"、 手表："Watch"、车机："Automotive"、PC："Desktop"、平板："Tablet"。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getFullVersion

```TypeScript
getFullVersion(): string
```

获取完整版本号。不调用对应的[setFullVersion](#setfullversion)设置时，版本号默认值：""。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getMobile

```TypeScript
getMobile(): boolean
```

获取是否为移动设备。不调用对应的[setMobile](#setmobile)设置时，默认值：手机: true，手表、车机、平板、大屏: false。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getModel

```TypeScript
getModel(): string
```

获取设备型号。不调用对应的[setModel](#setmodel)设置时，型号默认值：手机根据const.product.model取设备型号；手表、大屏、车机、 PC、平板：""。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getPlatform

```TypeScript
getPlatform(): string
```

获取操作系统名称。不调用对应的[setPlatform](#setplatform)设置时，名称默认值："OpenHarmony" 。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getPlatformVersion

```TypeScript
getPlatformVersion(): string
```

获取操作系统版本号。不调用对应的[setPlatformVersion](#setplatformversion)设置时，版本号默认值：按OpenHarmony平台 版本号规则，同const.product.os.dist.version。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## getWow64

```TypeScript
getWow64(): boolean
```

获取二进制文件是否是在64位Windows上以32位模式运行。不调用对应的[setWow64](#setwow64)设置时，默认值为false。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setArchitecture

```TypeScript
setArchitecture(arch: string): void
```

设置平台的架构类型。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arch | string | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setBitness

```TypeScript
setBitness(bitness: string): void
```

设置平台的位数类型。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bitness | string | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setBrandVersionList

```TypeScript
setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void
```

设置品牌和版本信息。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brandVersionList | Array&lt;[UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md)&gt; | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setFormFactors

```TypeScript
setFormFactors(formFactors: Array<UserAgentFormFactor>): void
```

设置设备形态信息，如手机、平板等。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formFactors | Array&lt;[UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md)&gt; | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setFullVersion

```TypeScript
setFullVersion(fullVersion: string): void
```

设置完整版本号。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullVersion | string | 是 |

**示例**

完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setMobile

```TypeScript
setMobile(isMobile: boolean): void
```

设置是否为移动设备。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMobile | boolean | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setModel

```TypeScript
setModel(model: string): void
```

设置设备型号。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| model | string | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setPlatform

```TypeScript
setPlatform(platform: string): void
```

设置操作系统名称。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| platform | string | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setPlatformVersion

```TypeScript
setPlatformVersion(platformVersion: string): void
```

设置操作系统版本号。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| platformVersion | string | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。

## setWow64

```TypeScript
setWow64(isWow64: boolean): void
```

设置二进制文件是否在64位Windows上以32位模式运行。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isWow64 | boolean | 是 |

**示例**

ArkTS-Dyn的完整示例代码参考[setUserAgentClientHintsEnabled](./arkts-apis-webview-WebviewController.md#setuseragentclienthintsenabled)。
