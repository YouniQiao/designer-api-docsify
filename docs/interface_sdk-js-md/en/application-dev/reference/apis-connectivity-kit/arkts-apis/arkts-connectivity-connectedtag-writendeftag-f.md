# writeNdefTag

## Modules to Import

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## writeNdefTag

```TypeScript
function writeNdefTag(data: string): Promise<void>
```

Writes data to this active tag. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [connectedTag.write](arkts-connectivity-connectedtag-write-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [write](arkts-connectivity-connectedtag-write-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## writeNdefTag

```TypeScript
function writeNdefTag(data: string, callback: AsyncCallback<void>): void
```

Writes data to this active tag. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. Use
> [connectedTag.write](arkts-connectivity-connectedtag-write-f.md) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [write](arkts-connectivity-connectedtag-write-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
