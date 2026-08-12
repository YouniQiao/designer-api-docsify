# write

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## write

```TypeScript
function write(data: number[]): Promise<void>
```

Writes the NDEF data to the connected NFC tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function write(data: number[]): Promise<void>--><!--Device-connectedTag-function write(data: number[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3200101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.write Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.write Promise err: " + err);
});
```


## write

```TypeScript
function write(data: number[], callback: AsyncCallback<void>): void
```

Writes the NDEF data to the connected NFC tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function write(data: number[], callback: AsyncCallback<void>): void--><!--Device-connectedTag-function write(data: number[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3200101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.write AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.write AsyncCallback success.");
    }
});
```
