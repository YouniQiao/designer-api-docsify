# writeNdefTag

## Modules to Import

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## writeNdefTag

```TypeScript
function writeNdefTag(data: string): Promise<void>
```

Writes the NDEF Data.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.connectedTag/connectedTag#write

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function writeNdefTag(data: string): Promise<void>--><!--Device-connectedTag-function writeNdefTag(data: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```


## writeNdefTag

```TypeScript
function writeNdefTag(data: string, callback: AsyncCallback<void>): void
```

Writes the NDEF Data.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.connectedTag/connectedTag#write

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function writeNdefTag(data: string, callback: AsyncCallback<void>): void--><!--Device-connectedTag-function writeNdefTag(data: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```
