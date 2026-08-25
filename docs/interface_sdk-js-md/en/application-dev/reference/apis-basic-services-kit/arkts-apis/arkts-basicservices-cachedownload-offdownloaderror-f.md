# offDownloadError

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## offDownloadError

```TypeScript
function offDownloadError(url: string, callback?: Callback<DownloadError>): void
```

Unsubscribes from the pre-download error events. This API uses an asynchronous callback to return the result.

**Since:** 23

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[DownloadError](arkts-basicservices-cachedownload-downloaderror-i.md)&gt; | No |
