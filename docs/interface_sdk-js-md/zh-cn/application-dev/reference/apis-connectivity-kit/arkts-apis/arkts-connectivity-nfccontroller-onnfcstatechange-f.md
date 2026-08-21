# onNfcStateChange

## 导入模块

```TypeScript
import { nfcController } from '@kit.ConnectivityKit';
```

## onNfcStateChange

```TypeScript
function onNfcStateChange(callback: Callback<NfcState>): void
```

register nfc state changed event.

**起始版本：** 23

<!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void--><!--Device-nfcController-function onNfcStateChange(callback: Callback<NfcState>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NfcState](arkts-connectivity-nfccontroller-nfcstate-e.md)&gt; | 是 | Callback used to listen to the nfc state changed event. |

