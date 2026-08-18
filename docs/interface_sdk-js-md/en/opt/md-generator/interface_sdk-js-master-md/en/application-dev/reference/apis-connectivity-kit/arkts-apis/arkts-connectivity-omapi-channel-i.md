# Channel

Channel represents an [ISO 7816-4] channel opened to a SE. It can be either a logical channel or the basic channel.

**Since:** 10

<!--Device-omapi-export interface Channel--><!--Device-omapi-export interface Channel-End-->

**System capability:** SystemCapability.Communication.SecureElement

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes this channel to the SE. If the method is called when the channel is already closed, this method SHALL be ignored.

**Since:** 10

<!--Device-Channel-close(): void--><!--Device-Channel-close(): void-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
try {
    seChannel.close();
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'close exception %{public}s', JSON.stringify(exception));
}
```

## getSelectResponse

```TypeScript
getSelectResponse(): number[]
```

Returns the data as received from the application select command, including the status word received at applet selection.

**Since:** 10

<!--Device-Channel-getSelectResponse(): number[]--><!--Device-Channel-getSelectResponse(): number[]-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
try {
    let response = seChannel.getSelectResponse();
    hilog.info(0x0000, 'testTag', 'response = %{public}s', JSON.stringify(response));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'getSelectResponse exception %{public}s', JSON.stringify(exception));
}
```

## getSession

```TypeScript
getSession(): Session
```

Get the session that has opened this channel.

**Since:** 10

<!--Device-Channel-getSession(): Session--><!--Device-Channel-getSession(): Session-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Session](../../apis-camera-kit/arkts-apis/arkts-camera-camera-session-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;

// Initialize seChannel before using it.

try {
    seSession = seChannel.getSession();
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'getSession exception %{public}s', JSON.stringify(exception));
}
```

## isBasicChannel

```TypeScript
isBasicChannel(): boolean
```

Checks whether this channel is the basic channel.

**Since:** 10

<!--Device-Channel-isBasicChannel(): boolean--><!--Device-Channel-isBasicChannel(): boolean-End-->

**System capability:** SystemCapability.Communication.SecureElement

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
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
try {
    let isBasic = seChannel.isBasicChannel();
    hilog.info(0x0000, 'testTag', 'isBasic = %{public}s', JSON.stringify(isBasic));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'isBasicChannel exception %{public}s', JSON.stringify(exception));
}
```

## isClosed

```TypeScript
isClosed(): boolean
```

Checks if this channel is closed.

**Since:** 10

<!--Device-Channel-isClosed(): boolean--><!--Device-Channel-isClosed(): boolean-End-->

**System capability:** SystemCapability.Communication.SecureElement

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
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
try {
    let isClosed = seChannel.isClosed();
    hilog.info(0x0000, 'testTag', 'isClosed = %{public}s', JSON.stringify(isClosed));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'isClosed exception %{public}s', JSON.stringify(exception));
}
```

## transmit

```TypeScript
transmit(command: number[]): Promise<number[]>
```

Transmit an APDU command (as per ISO/IEC 7816) to the SE.

**Since:** 10

<!--Device-Channel-transmit(command: number[]): Promise<number[]>--><!--Device-Channel-transmit(command: number[]): Promise<number[]>-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
try {
    seChannel.transmit(cmdData).then((response) => {
        // If the chip captures an exception, an all zero value is returned for response.
        hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
    }).catch((error : BusinessError) => {
        hilog.error(0x0000, 'testTag', 'transmit error = %{public}s.', JSON.stringify(error));
    });
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'transmit exception = %{public}s.', JSON.stringify(exception));
}
```

## transmit

```TypeScript
transmit(command: number[], callback: AsyncCallback<number[]>): void
```

Transmit an APDU command (as per ISO/IEC 7816) to the SE.

**Since:** 10

<!--Device-Channel-transmit(command: number[], callback: AsyncCallback<number[]>): void--><!--Device-Channel-transmit(command: number[], callback: AsyncCallback<number[]>): void-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// Initialize seChannel before using it.
let cmdData = [0x01, 0x02, 0x03, 0x04]; // Set command data correctly.
try {
    seChannel.transmit(cmdData, (error, response) => {
    if (error) {
        hilog.error(0x0000, 'testTag', 'transmit error %{public}s', JSON.stringify(error));
    } else {
        // If the chip captures an exception, an all zero value is returned for response.
        hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
    }
    });
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'transmit exception %{public}s', JSON.stringify(exception));
}
```
