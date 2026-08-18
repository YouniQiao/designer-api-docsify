# HceService

A class for NFC host application. &lt;p&gt;The NFC host application use this class, then Nfc service can access the application installation information and connect to services of the application.

**Since:** 23

<!--Device-cardEmulation-export class HceService--><!--Device-cardEmulation-export class HceService-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

## Modules to Import

```TypeScript
```

## offHceCmd

```TypeScript
offHceCmd(callback?: AsyncCallback<number[]>): void
```

Unsubscribe the event to receive the APDU data.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void--><!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## off_hceCmd

```TypeScript
off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void
```

Unsubscribe the event to receive the APDU data.

**Since:** 18

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void--><!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hceCmd' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
// Applicable to devices other than lite wearables
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { bundleManager, AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: bundleManager.ElementName;
const apduCallback: AsyncCallback<number[]> = (err, data) => {
  // Implement data processing and handle exceptions.
  console.info("AsyncCallback got apdu data");
};

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.off('hceCmd', apduCallback);
    hceService.stop(element);
  }
  // Other functions in the lifecycle
}
```

## onHceCmd

```TypeScript
onHceCmd(callback: AsyncCallback<number[]>): void
```

register HCE event to receive the APDU data.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void--><!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## on_hceCmd

```TypeScript
on(type: 'hceCmd', callback: AsyncCallback<number[]>): void
```

register HCE event to receive the APDU data.

**Since:** 12

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void--><!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hceCmd' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## sendResponse

```TypeScript
sendResponse(responseApdu: number[]): void
```

Sends a response APDU to the remote device. &lt;p&gt;This method is used by a host application when swiping card.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [transmit](#transmit)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-sendResponse(responseApdu: number[]): void--><!--Device-HceService-sendResponse(responseApdu: number[]): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| responseApdu | number[] | Yes |

## start

```TypeScript
start(elementName: ElementName, aidList: string[]): void
```

Starts the HCE, register more aids and allows this application to be preferred while in foreground.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-start(elementName: ElementName, aidList: string[]): void--><!--Device-HceService-start(elementName: ElementName, aidList: string[]): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| aidList | string[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## startHCE

```TypeScript
startHCE(aidList: string[]): boolean
```

start HCE

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [start](#start)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-startHCE(aidList: string[]): boolean--><!--Device-HceService-startHCE(aidList: string[]): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aidList | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## stop

```TypeScript
stop(elementName: ElementName): void
```

Stops the HCE, and unset the preferred service while in foreground.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-stop(elementName: ElementName): void--><!--Device-HceService-stop(elementName: ElementName): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## stopHCE

```TypeScript
stopHCE(): boolean
```

stop HCE

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stop](#stop)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-stopHCE(): boolean--><!--Device-HceService-stopHCE(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## transmit

```TypeScript
transmit(response: number[]): Promise<void>
```

Sends a response APDU to the remote device.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-transmit(response: int[]): Promise<void>--><!--Device-HceService-transmit(response: int[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
const responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // Process the promise.
  console.info("transmit Promise success.");
}).catch((err: BusinessError) => {
  console.error("transmit Promise error:", err);
});
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
let responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // Process the promise.
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```

## transmit

```TypeScript
transmit(response: number[], callback: AsyncCallback<void>): void
```

Sends a response APDU to the remote device.

**Since:** 23

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void--><!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
try {
  const responseData = [0x1, 0x2];

  hceService.transmit(responseData, (err : BusinessError)=> {
    if (err) {
      console.error(`transmit AsyncCallback err Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info("transmit AsyncCallback success.");
    }
  });
} catch (error) {
  console.error(`transmit AsyncCallback catch Code: ${(error as BusinessError).code}, ` +
    `message: ${(error as BusinessError).message}`);
}
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
let responseData = [0x1, 0x2];
hceService.transmit(responseData, () => {
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```
