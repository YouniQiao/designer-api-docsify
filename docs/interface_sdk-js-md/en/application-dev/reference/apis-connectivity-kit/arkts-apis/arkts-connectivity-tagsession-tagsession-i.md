# TagSession

The **tagSession** module provides common APIs for establishing connections and transferring data.

> **NOTE：**&gt;
> If an error is reported while importing the tag module editor, the capabilities of a specific device model may
> exceed the capability set defined for the default device. To use these capabilities, configure a custom SysCap by
> following instructions in
> [SystemCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap).

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

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

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.connect](#connect) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** connect

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

Obtains the maximum length of the data that can be sent to this tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.getMaxTransmitSize](#getmaxtransmitsize) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getMaxTransmitSize](#getmaxtransmitsize)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let maxSendLen = tag.getIsoDep(tagInfo).getMaxSendLength(); 
console.info("tag maxSendLen: " + maxSendLen);
```

## getMaxTransmitSize

ArkTS-Dyn:
```TypeScript
getMaxTransmitSize(): number
```

ArkTS-Sta:
```TypeScript
getMaxTransmitSize(): int
```

Obtains the maximum length of the data that can be sent to this tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

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

Obtains the timeout period for sending data to this tag, in milliseconds.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.getTimeout](#gettimeout) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getTimeout](#gettimeout)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

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

Obtains the **tagInfo** object provided by the NFC service when the tag is dispatched.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tag.getTagInfo](arkts-connectivity-tag-gettaginfo-f.md) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| tag.TagInfo |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag. 
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let tagInfo : TagInfo = tag.getIsoDep(tagInfo).getTagInfo();
console.info("tag tagInfo: " + tagInfo);
```

## getTimeout

ArkTS-Dyn:
```TypeScript
getTimeout(): number
```

ArkTS-Sta:
```TypeScript
getTimeout(): int
```

Obtains the timeout period for sending data to this tag, in milliseconds.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

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

Checks whether the tag is connected. If you receive a message indicating that the tag has not been connected, call [tagSession.connect](#connect) to connect the tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

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

Checks whether the tag is connected.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.isConnected](#isconnected) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** isConnected

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

Resets the connection to this tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.resetConnection](#resetconnection) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [resetConnection](#resetconnection)

**Required permissions:** ohos.permission.NFC_TAG

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

Resets the connection to this tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

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

Sends data to the tag. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.transmit](#transmit) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

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

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

Sends data to the tag. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This parameter is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.transmit](#transmit) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Examples**

See [sendData](#senddata)

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

Sets the maximum time allowed for sending data to this tag, in ms.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.setTimeout](#settimeout) instead.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** setTimeout

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

ArkTS-Dyn:
```TypeScript
setTimeout(timeout: number): void
```

ArkTS-Sta:
```TypeScript
setTimeout(timeout: int): void
```

Sets the maximum time allowed for sending data to this tag, in ms.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

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

ArkTS-Dyn:
```TypeScript
transmit(data: number[]): Promise<number[]>
```

ArkTS-Sta:
```TypeScript
transmit(data: int[]): Promise<int[]>
```

Sends data to the tag. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArkTS-Dyn: number[]<br>ArkTS-Sta：int[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: Promise & lt;number[] & gt;<br>ArkTS-Sta：Promise & lt;int[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

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

## transmit

ArkTS-Dyn:
```TypeScript
transmit(data: number[], callback: AsyncCallback<number[]>): void
```

ArkTS-Sta:
```TypeScript
transmit(data: int[], callback: AsyncCallback<int[]>): void
```

Sends data to the tag. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArkTS-Dyn: number[]<br>ArkTS-Sta：int[] | Yes |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

**Examples**

See [transmit](#transmit)
