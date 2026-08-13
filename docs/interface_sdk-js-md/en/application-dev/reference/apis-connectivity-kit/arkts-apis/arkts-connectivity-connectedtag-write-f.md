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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function write(data: number[]): Promise<void>--><!--Device-connectedTag-function write(data: number[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the NDEF data to send, which is a byte array. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```


## write

```TypeScript
function write(data: number[], callback: AsyncCallback<void>): void
```

Writes the NDEF data to the connected NFC tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function write(data: number[], callback: AsyncCallback<void>): void--><!--Device-connectedTag-function write(data: number[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the NDEF data to send, which is a byte array. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

