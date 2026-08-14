# read

## Modules to Import

```TypeScript
import { connectedTag } from 'connectedTag';
```

## read

```TypeScript
function read(): Promise<number[]>
```

Reads the NDEF data from the connected NFC tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function read(): Promise<number[]>--><!--Device-connectedTag-function read(): Promise<number[]>-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number[]&gt; | The reponse NDEF data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function read(callback: AsyncCallback<number[]>): void--><!--Device-connectedTag-function read(callback: AsyncCallback<number[]>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes | The callback to receive the data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3200101](../errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

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

