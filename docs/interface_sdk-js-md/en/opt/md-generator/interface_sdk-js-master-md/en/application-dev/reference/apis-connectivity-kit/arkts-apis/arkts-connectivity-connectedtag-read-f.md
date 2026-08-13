# read

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## read

```TypeScript
function read(): Promise<number[]>
```

Reads the NDEF data from the connected NFC tag.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function read(): Promise<number[]>--><!--Device-connectedTag-function read(): Promise<number[]>-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.read().then((data) => {
    console.info("connectedTag read Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag read Promise err: " + err);
});
```


## read

```TypeScript
function read(callback: AsyncCallback<number[]>): void
```

Reads the NDEF data from the connected NFC tag.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function read(callback: AsyncCallback<number[]>): void--><!--Device-connectedTag-function read(callback: AsyncCallback<number[]>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.read((err, data)=> {
    if (err) {
        console.error("connectedTag read AsyncCallback err: " + err);
    } else {
        console.info("connectedTag read AsyncCallback data: " + data);
    }
});
```
