# HceService

A class for NFC host application.&lt;p&gt;The NFC host application use this class, then Nfc service can access the application installation information and connect to services of the application.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-cardEmulation-export class HceService--><!--Device-cardEmulation-export class HceService-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## off('hceCmd')

```TypeScript
off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void
```

Unsubscribe the event to receive the APDU data.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void--><!--Device-HceService-off(type: 'hceCmd', callback?: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'hceCmd' | 是 | The type to unregister event. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 否 | The callback used to listen for the event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |

## 示例

```TypeScript
// 适用于除轻量级智能穿戴产品之外其他设备
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { bundleManager, AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: bundleManager.ElementName;
const apduCallback: AsyncCallback<number[]> = (err, data) => {
  // 处理数据和异常
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
  // 生命周期内的其他功能
}
```

## offHceCmd

```TypeScript
offHceCmd(callback?: AsyncCallback<int[]>): void
```

Unsubscribe the event to receive the APDU data.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void--><!--Device-HceService-offHceCmd(callback?: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 否 | The callback used to listen for the event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |

## on('hceCmd')

```TypeScript
on(type: 'hceCmd', callback: AsyncCallback<int[]>): void
```

register HCE event to receive the APDU data.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void--><!--Device-HceService-on(type: 'hceCmd', callback: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'hceCmd' | 是 | The type to register. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 是 | Callback used to listen to HCE data that local device received. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 201 | Permission denied. |

## 示例

ArkTS示例：

```TypeScript
// 适用于除轻量级智能穿戴产品之外其他设备
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { bundleManager, AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: bundleManager.ElementName;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    const apduCallback: AsyncCallback<number[]> = (err, data) => {
      // 处理数据和异常
      console.info("got apdu data");
    };
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.stop(element);
  }
  // 生命周期内的其他功能
}
```

JS示例：

```TypeScript
// 适用于轻量级智能穿戴设备
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
      // 应用程序实际想要发送的数据， 此处仅作为示例
      let responseData = [0x1, 0x2];
      HceService.transmit(responseData, () => {
        console.info('sendResponse start');
      });
      console.info('sendResponse end');
    });
  },
  onDestroy() {
  }
  // 生命周期内的其他功能
}
```

## onHceCmd

```TypeScript
onHceCmd(callback: AsyncCallback<int[]>): void
```

register HCE event to receive the APDU data.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void--><!--Device-HceService-onHceCmd(callback: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 是 | Callback used to listen to HCE data that local device received. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |

## sendResponse

```TypeScript
sendResponse(responseApdu: number[]): void
```

Sends a response APDU to the remote device.&lt;p&gt;This method is used by a host application when swiping card.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.nfc.cardEmulation/cardEmulation.HceService#transmit

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HceService-sendResponse(responseApdu: number[]): void--><!--Device-HceService-sendResponse(responseApdu: number[]): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| responseApdu | number[] | 是 | Indicates the response, which is a byte array. |

## 示例

JS示例：

```TypeScript
<!-- 适用于轻量级智能穿戴设备 -->
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        测试
    </text>
    <input type="button" value="sendResponse" style="width: 240px; height: 50px; margin: 5px;" onclick="onClick"></input>
</div>
```

```TypeScript
/* 适用于轻量级智能穿戴设备 */
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```TypeScript
// 适用于轻量级智能穿戴设备
// xxx.js
import cardEmulation from '@ohos.nfc.cardEmulation';

export default  {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    onClick() {
        var hceService = new cardEmulation.HceService();
        hceService.on("hceCmd", (err, res) => {
            if(err.data === 0) {
                console.info('callback => Operation hceCmd succeeded. Data: ${JSON.stringify(res)}');
                hceService.sendResponse([0x00,0xa4,0x04,0x00,
                    0x0e,0x32,0x50,0x41,0x59,0x2e,0x53,0x59,0x53,0x2e,0x44,0x44,
                    0x46,0x30,0x31,0x00]);
            } else {
                console.info('callback => Operation hceCmd failed. Cause: ${JSON.stringify(err.data)}');
            }
        })
    }
}
```

## start

```TypeScript
start(elementName: ElementName, aidList: string[]): void
```

Starts the HCE, register more aids and allows this application to be preferred while in foreground.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-start(elementName: ElementName, aidList: string[]): void--><!--Device-HceService-start(elementName: ElementName, aidList: string[]): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 | The element name of the service ability |
| aidList | string[] | 是 | The aid list to be registered by this service, allowed to be empty. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |
| 201 | Permission denied. |

## startHCE

```TypeScript
startHCE(aidList: string[]): boolean
```

start HCE

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.nfc.cardEmulation/cardEmulation.HceService#start

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HceService-startHCE(aidList: string[]): boolean--><!--Device-HceService-startHCE(aidList: string[]): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aidList | string[] | 是 | The aid list to be registered by this service |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if HCE is enabled or has been enabled; returns false otherwise. |

## 示例

JS示例：

```TypeScript
<!-- 适用于轻量级智能穿戴设备 -->
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        测试
    </text>
    <input type="button" value="startHCE" style="width: 240px; height: 50px; margin: 5px;" onclick="onClick"></input>
</div>
```

```TypeScript
/* 适用于轻量级智能穿戴设备 */
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```TypeScript
// 适用于轻量级智能穿戴设备
// xxx.js
import cardEmulation from '@ohos.nfc.cardEmulation';

export default  {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    onClick() {
        var hceService = new cardEmulation.HceService();
        hceService.startHCE([
            "F0010203040506", "A0000000041010"
        ])
    }
}
```

## stop

```TypeScript
stop(elementName: ElementName): void
```

Stops the HCE, and unset the preferred service while in foreground.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-stop(elementName: ElementName): void--><!--Device-HceService-stop(elementName: ElementName): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 | The element name of the service ability |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |
| 201 | Permission denied. |

## stopHCE

```TypeScript
stopHCE(): boolean
```

stop HCE

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.nfc.cardEmulation/cardEmulation.HceService#stop

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HceService-stopHCE(): boolean--><!--Device-HceService-stopHCE(): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if HCE is disabled or has been disabled; returns false otherwise. |

## 示例

JS示例：

```TypeScript
<!-- 适用于轻量级智能穿戴设备 -->
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        测试
    </text>
    <input type="button" value="stopHCE" style="width: 240px; height: 50px; margin: 5px;" onclick="onClick"></input>
</div>
```

```TypeScript
/* 适用于轻量级智能穿戴设备 */
/* xxx.css */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```TypeScript
// 适用于轻量级智能穿戴设备
// xxx.js
import cardEmulation from '@ohos.nfc.cardEmulation';

export default  {
    data: {
        fontSize: '30px',
        fontColor: '#FF1AFF00',
    },
    onClick() {
        var hceService = new cardEmulation.HceService();
        hceService.stopHCE();
    }
}
```

## transmit

ArkTS-Dyn:
```TypeScript
transmit(response: number[]): Promise<void>
```

ArkTS-Sta:
```TypeScript
transmit(response: int[]): Promise<void>
```

Sends a response APDU to the remote device.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-transmit(response: int[]): Promise<void>--><!--Device-HceService-transmit(response: int[]): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | Indicates the response to send, which is a byte array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |
| 201 | Permission denied. |

## 示例

```TypeScript
// 适用于除轻量级智能穿戴产品之外其他设备
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅作为示例
const responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // 处理 promise 的回调
  console.info("transmit Promise success.");
}).catch((err: BusinessError) => {
  console.error("transmit Promise error:", err);
});
```

```TypeScript
// 适用于轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅作为示例
let responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // 处理 promise 的回调
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```

## transmit

ArkTS-Dyn:
```TypeScript
transmit(response: number[], callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
transmit(response: int[], callback: AsyncCallback<void>): void
```

Sends a response APDU to the remote device.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void--><!--Device-HceService-transmit(response: int[], callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | Indicates the response to send, which is a byte array. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |
| 201 | Permission denied. |

## 示例

```TypeScript
// 适用于除轻量级智能穿戴产品之外其他设备
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅作为示例
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
// 适用于轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅作为示例
let responseData = [0x1, 0x2];
hceService.transmit(responseData, () => {
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```

