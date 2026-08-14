# HceService

A class for NFC host application. &lt;p&gt;The NFC host application use this class, then Nfc service can access the application installation information and connect to services of the application.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cardEmulation-export class HceService--><!--Device-cardEmulation-export class HceService-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

## Modules to Import

```TypeScript
import { cardEmulation } from 'cardEmulation';
```

## offHceCmd

```TypeScript
offHceCmd(callback?: AsyncCallback<int[]>): void
```

Unsubscribe the event to receive the APDU data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void--><!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | No | The callback used to listen for the event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## off_hceCmd

```TypeScript
off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void
```

Unsubscribe the event to receive the APDU data.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void--><!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hceCmd' | Yes | The type to unregister event. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | No | The callback used to listen for the event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
// Applicable to devices other than lite wearables
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;
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
  // Implement other lifecycle functions as demanded.
}
```

## onHceCmd

```TypeScript
onHceCmd(callback: AsyncCallback<int[]>): void
```

register HCE event to receive the APDU data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void--><!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | Yes | Callback used to listen to HCE data that local device received. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## on_hceCmd

```TypeScript
on(type: 'hceCmd', callback: AsyncCallback<int[]>): void
```

register HCE event to receive the APDU data.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void--><!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hceCmd' | Yes | The type to register. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | Yes | Callback used to listen to HCE data that local device received. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
// Applicable to devices other than lite wearables
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    const apduCallback: AsyncCallback<number[]> = (err, data) => {
      // Implement data processing and handle exceptions.
      console.info("got apdu data");
    };
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.stop(element);
  }
  // Implement other lifecycle functions as demanded.
}
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";

export default {
  data:{
    fontSize: '30px',
    fontColor: '#50609f',
    hide: 'show',
    headCon: appName,
    paymentAid: ["A0000000041010", "A0000000041012"]
  },
  onCreate() {
    console.info('onCreate');
  },
  onReady() {
    cardEmulation.hasHceCapability();
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.OTHER);
    let HceService = new cardEmulation.HceService();

    HceService.start(appName, this.paymentAid);
    HceService.on("hceCmd", (data) => {
      console.info('data:' + data);
      // Data to be sent by the application. The following data is for reference only.
      let responseData = [0x1, 0x2];
      HceService.transmit(responseData, () => {
        console.info('sendResponse start');
      });
      console.info('sendResponse end');
    });
  },
  onDestroy() {
  }
  // Implement other lifecycle functions as demanded.
}
```

## sendResponse

```TypeScript
sendResponse(responseApdu: number[]): void
```

Sends a response APDU to the remote device. &lt;p&gt;This method is used by a host application when swiping card.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [transmit](#transmit)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-sendResponse(responseApdu: number[]): void--><!--Device-HceService-sendResponse(responseApdu: number[]): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| responseApdu | number[] | Yes | Indicates the response, which is a byte array. |

## start

```TypeScript
start(elementName: ElementName, aidList: string[]): void
```

Starts the HCE, register more aids and allows this application to be preferred while in foreground.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-start(elementName: ElementName, aidList: string[]): void--><!--Device-HceService-start(elementName: ElementName, aidList: string[]): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of the service ability |
| aidList | string[] | Yes | The aid list to be registered by this service, allowed to be empty. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) | Card emulation running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## startHCE

```TypeScript
startHCE(aidList: string[]): boolean
```

start HCE

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [start](#start)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-startHCE(aidList: string[]): boolean--><!--Device-HceService-startHCE(aidList: string[]): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aidList | string[] | Yes | The aid list to be registered by this service |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if HCE is enabled or has been enabled; returns false otherwise. |

## stop

```TypeScript
stop(elementName: ElementName): void
```

Stops the HCE, and unset the preferred service while in foreground.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-stop(elementName: ElementName): void--><!--Device-HceService-stop(elementName: ElementName): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of the service ability |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) | Card emulation running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## stopHCE

```TypeScript
stopHCE(): boolean
```

stop HCE

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [stop](#stop)

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-HceService-stopHCE(): boolean--><!--Device-HceService-stopHCE(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if HCE is disabled or has been disabled; returns false otherwise. |

## Examples

For details, see the example of on.

## transmit

```TypeScript
transmit(response: int[]): Promise<void>
```

Sends a response APDU to the remote device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-transmit(response: int[]): Promise<void>--><!--Device-HceService-transmit(response: int[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | int[] | Yes | Indicates the response to send, which is a byte array. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) | Card emulation running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

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
transmit(response: int[], callback: AsyncCallback<void>): void
```

Sends a response APDU to the remote device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void--><!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | int[] | Yes | Indicates the response to send, which is a byte array. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100301](../errorcode-nfc.md#3100301-abnormal-nfc-card-emulation-status) | Card emulation running state is abnormal in service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

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

