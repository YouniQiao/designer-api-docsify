# UserAgentBrandVersion

Class that holds brand name, major version and full version. Brand name and major version used to generated User-Agent client hints sec-cu-ua. Brand name and full version used to generated user-agent client hint sec-ch-ua-full-version-list.

**Since:** 24

**Deprecated since:** -1

<!--Device-webview-class UserAgentBrandVersion--><!--Device-webview-class UserAgentBrandVersion-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getBrand

```TypeScript
getBrand(): string
```

Get the brand info.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-getBrand(): string--><!--Device-UserAgentBrandVersion-getBrand(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getFullVersion

```TypeScript
getFullVersion(): string
```

Get the full version.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-getFullVersion(): string--><!--Device-UserAgentBrandVersion-getFullVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMajorVersion

```TypeScript
getMajorVersion(): string
```

Get the major version.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-getMajorVersion(): string--><!--Device-UserAgentBrandVersion-getMajorVersion(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setBrand

```TypeScript
setBrand(brand: string): void
```

Sets the brand. Should not be blank.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-setBrand(brand: string): void--><!--Device-UserAgentBrandVersion-setBrand(brand: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brand | string | Yes |

## setFullVersion

```TypeScript
setFullVersion(fullVersion: string): void
```

Sets the full version. Should not be blank.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-setFullVersion(fullVersion: string): void--><!--Device-UserAgentBrandVersion-setFullVersion(fullVersion: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullVersion | string | Yes |

## setMajorVersion

```TypeScript
setMajorVersion(majorVersion: string): void
```

Sets the major version. Should not be blank.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAgentBrandVersion-setMajorVersion(majorVersion: string): void--><!--Device-UserAgentBrandVersion-setMajorVersion(majorVersion: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [majorVersion](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-deviceinfo-con.md) | string | Yes |
