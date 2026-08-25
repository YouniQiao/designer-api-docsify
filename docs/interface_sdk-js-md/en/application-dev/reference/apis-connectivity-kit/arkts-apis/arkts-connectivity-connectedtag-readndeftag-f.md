# readNdefTag

## Modules to Import

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## readNdefTag

```TypeScript
function readNdefTag(): Promise<string>
```

Reads the content of this active tag. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [uninitialize](arkts-connectivity-connectedtag-uninitialize-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [read](arkts-connectivity-connectedtag-read-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |


## readNdefTag

```TypeScript
function readNdefTag(callback: AsyncCallback<string>): void
```

Reads the content of this active tag. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [uninitialize](arkts-connectivity-connectedtag-uninitialize-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [read](arkts-connectivity-connectedtag-read-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |
