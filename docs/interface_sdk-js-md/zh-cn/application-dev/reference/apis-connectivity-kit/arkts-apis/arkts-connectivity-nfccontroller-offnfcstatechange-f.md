# offNfcStateChange

## 导入模块

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## offNfcStateChange

```TypeScript
function offNfcStateChange(callback?: Callback<NfcState>): void
```

unregister nfc state changed event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-nfcController-function offNfcStateChange(callback?: Callback<NfcState>): void--><!--Device-nfcController-function offNfcStateChange(callback?: Callback<NfcState>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NfcState&gt; | 否 | Callback used to listen to the nfc state changed event. |

