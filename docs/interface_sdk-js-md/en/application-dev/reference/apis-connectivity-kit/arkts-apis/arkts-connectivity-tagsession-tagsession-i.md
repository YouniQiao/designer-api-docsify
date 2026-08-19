# TagSession

Controls tag read and write. &lt;p&gt;Classes for different types of tags inherit from this abstract class to control connections to tags, read data from tags, and write data to tags.

**Since:** 23

<!--Device-unnamed-export interface TagSession--><!--Device-unnamed-export interface TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

Connects to a tag. Must be called before data is read from or written to the tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-connect(): void--><!--Device-TagSession-connect(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    tag.getIsoDep(tagInfo).connect(); 
    console.info("tag connect success");
} catch (businessError) {
    console.error("tag connect businessError: " + businessError);
}
```

## connectTag

```TypeScript
connectTag(): boolean
```

Connects to a tag. &lt;p&gt;This method must be called before data is read from or written to the tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connect

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-connectTag(): boolean--><!--Device-TagSession-connectTag(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let connectStatus : boolean = tag.getIsoDep(tagInfo).connectTag();
console.info("connectStatus: " + connectStatus);
```

## getMaxSendLength

```TypeScript
getMaxSendLength(): number
```

Queries the maximum length of data that can be sent to a tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getMaxTransmitSize](#getmaxtransmitsize)

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getMaxSendLength(): number--><!--Device-TagSession-getMaxSendLength(): number-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the maximum length of the data to be sent to the tag. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let maxSendLen = tag.getIsoDep(tagInfo).getMaxSendLength(); 
console.info("tag maxSendLen: " + maxSendLen);
```

## getMaxTransmitSize

```TypeScript
getMaxTransmitSize(): int
```

Obtains the maximum length of data that can be sent to a tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-getMaxTransmitSize(): int--><!--Device-TagSession-getMaxTransmitSize(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the maximum length of the data to be sent to the tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let maxTransmitSize = tag.getIsoDep(tagInfo).getMaxTransmitSize(); 
    console.info("tag maxTransmitSize = " + maxTransmitSize);
} catch (businessError) {
    console.error("tag getMaxTransmitSize businessError: " + businessError);
}
```

## getSendDataTimeout

```TypeScript
getSendDataTimeout(): number
```

Queries the timeout duration (ms) for sending data to a tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getTimeout](#gettimeout)

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getSendDataTimeout(): number--><!--Device-TagSession-getSendDataTimeout(): number-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the timeout duration. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let sendDataTimeout = tag.getIsoDep(tagInfo).getSendDataTimeout(); 
console.info("tag sendDataTimeout: " + sendDataTimeout);
```

## getTagInfo

```TypeScript
getTagInfo(): tag.TagInfo
```

Obtains the tag information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md)

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getTagInfo(): tag.TagInfo--><!--Device-TagSession-getTagInfo(): tag.TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| tag.TagInfo | Returns the tag information, which is a { |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let tagInfo : TagInfo = tag.getIsoDep(tagInfo).getTagInfo();
console.info("tag tagInfo: " + tagInfo);
```

## getTimeout

```TypeScript
getTimeout(): int
```

Obtains the timeout duration (ms) for sending data to a tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-getTimeout(): int--><!--Device-TagSession-getTimeout(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the timeout duration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let timeout = tag.getIsoDep(tagInfo).getTimeout(); 
    console.info("tag timeout = " + timeout);
} catch (businessError) {
    console.error("tag getTimeout businessError: " + businessError);
}
```

## isConnected

```TypeScript
isConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-isConnected(): boolean--><!--Device-TagSession-isConnected(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if tag connected, otherwise false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let isConnected = tag.getIsoDep(tagInfo).isConnected(); 
    console.info("tag isConnected = " + isConnected);
} catch (businessError) {
    console.error("tag isConnected businessError: " + businessError);
}
```

## isTagConnected

```TypeScript
isTagConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isConnected

<!--Device-TagSession-isTagConnected(): boolean--><!--Device-TagSession-isTagConnected(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let isTagConnected = tag.getIsoDep(tagInfo).isTagConnected(); 
console.info("isTagConnected: " + isTagConnected);
```

## reset

```TypeScript
reset(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [resetConnection](#resetconnection)

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-reset(): void--><!--Device-TagSession-reset(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

tag.getIsoDep(tagInfo).reset();
```

## resetConnection

```TypeScript
resetConnection(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-resetConnection(): void--><!--Device-TagSession-resetConnection(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    tag.getIsoDep(tagInfo).resetConnection(); 
    console.info("tag resetConnection success");
} catch (businessError) {
    console.error("tag resetConnection businessError: " + businessError);
}
```

## sendData

```TypeScript
sendData(data: number[]): Promise<number[]>
```

Writes data to a tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[]): Promise<number[]>--><!--Device-TagSession-sendData(data: number[]): Promise<number[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the data to be written to the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

**Examples**

```TypeScript
import tag from '@kit.ConnectivityKit';
import { BusinessError } from '@ohos.base';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    if (!tag.getIsoDep(tagInfo).isTagConnected()) {
        if (!tag.getIsoDep(tagInfo).connectTag()) {
            console.error("tagSession connectTag failed.");
            return;
        }
    }  

    let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
    tag.getIsoDep(tagInfo).sendData(cmdData).then((response) => {
    console.info("tagSession sendData Promise response: " + response);
    }).catch((err : BusinessError)=> {
    console.error("tagSession sendData Promise err: " + err);
    });
}
```

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

Writes data to a tag.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void--><!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the data to be written to the tag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes | The callback. data fails to be written to the tag. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    if (!tag.getIsoDep(tagInfo).isTagConnected()) {
        if (!tag.getIsoDep(tagInfo).connectTag()) {
            console.error("tagSession connectTag failed.");
            return;
        }
    }

    let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
    tag.getIsoDep(tagInfo).sendData(cmdData, (err, response)=> {
        if (err) {
            console.error("tagSession sendData AsyncCallback err: " + err);
        } else {
            console.info("tagSession sendData AsyncCallback response: " + response);
        }
    });
}
```

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

Sets the timeout duration (ms) for sending data to a tag. &lt;p&gt;If data is not sent to the tag within the duration, data sending fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** setTimeout

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-setSendDataTimeout(timeout: number): boolean--><!--Device-TagSession-setSendDataTimeout(timeout: number): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | number | Yes | Indicates the timeout duration to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let timeoutMs = 700; // Set the expected timeout interval.
let setStatus = tag.getIsoDep(tagInfo).setSendDataTimeout(timeoutMs); 
console.info("tag setSendDataTimeout setStatus: " + setStatus);
```

## setTimeout

```TypeScript
setTimeout(timeout: int): void
```

Sets the timeout duration (ms) for sending data to a tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-setTimeout(timeout: int): void--><!--Device-TagSession-setTimeout(timeout: int): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | int | Yes | Indicates the timeout duration to be set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let timeoutMs = 700; // Set the expected timeout interval.
try {
    tag.getIsoDep(tagInfo).setTimeout(timeoutMs); 
    console.info("tag setTimeout success");
} catch (businessError) {
    console.error("tag setTimeout businessError: " + businessError);
}
```

## transmit

```TypeScript
transmit(data: int[]): Promise<int[]>
```

Writes data to a tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-transmit(data: int[]): Promise<int[]>--><!--Device-TagSession-transmit(data: int[]): Promise<int[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | int[] | Yes | Indicates the data to be written to the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
// Connect the tag if it has not been connected.
    try {
        if (!tag.getIsoDep(tagInfo).isConnected()) {
            tag.getIsoDep(tagInfo).connect();
        }
    } catch (businessError) {
        console.error("tag connect businessError: " + businessError);
        return;
    }

    let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
    try {
    tag.getIsoDep(tagInfo).transmit(cmdData).then((response) => {
        console.info("tagSession transmit Promise response: " + response);
    }).catch((err : BusinessError)=> {
        console.error("tagSession transmit Promise err: " + err);
    });
    } catch (businessError) {
        console.error("tag transmit businessError: " + businessError);
        return;
    }
}
```

## transmit

```TypeScript
transmit(data: int[], callback: AsyncCallback<int[]>): void
```

Writes data to a tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void--><!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | int[] | Yes | Indicates the data to be written to the tag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    try {
        if (!tag.getIsoDep(tagInfo).isConnected()) {
            tag.getIsoDep(tagInfo).connect();
        }
    } catch (businessError) {
        console.error("tag connect businessError: " + businessError);
        return;
    }

    let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
    try {
        tag.getIsoDep(tagInfo).transmit(cmdData, (err, response)=> {
            if (err) {
                console.error("tagSession transmit AsyncCallback err: " + err);
            } else {
                console.info("tagSession transmit AsyncCallback response: " + response);
            }
        });
    } catch (businessError) {
        console.error("tag transmit businessError: " + businessError);
        return;
    }
}
```

