# WebDownloadDelegate

The download state is notified through this delegate.

**Since:** 11

<!--Device-webview-class WebDownloadDelegate--><!--Device-webview-class WebDownloadDelegate-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## onBeforeDownload

```TypeScript
onBeforeDownload(callback: Callback<WebDownloadItem>): void
```

Callback will be triggered before web download start.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onBeforeDownload(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onBeforeDownload(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebDownloadItem&gt; | Yes |

## onDownloadFailed

```TypeScript
onDownloadFailed(callback: Callback<WebDownloadItem>): void
```

Callback will be triggered when web download is interrupted or canceled.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadFailed(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadFailed(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebDownloadItem&gt; | Yes |

## onDownloadFinish

```TypeScript
onDownloadFinish(callback: Callback<WebDownloadItem>): void
```

Callback will be triggered when web download is completed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadFinish(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadFinish(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebDownloadItem&gt; | Yes |

## onDownloadUpdated

```TypeScript
onDownloadUpdated(callback: Callback<WebDownloadItem>): void
```

Callback will be triggered when web download is processing.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadUpdated(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadUpdated(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WebDownloadItem&gt; | Yes |
