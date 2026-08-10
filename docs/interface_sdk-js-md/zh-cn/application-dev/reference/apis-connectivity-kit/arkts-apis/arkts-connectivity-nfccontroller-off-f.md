# off

## 导入模块

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## off('nfcStateChange')

```TypeScript
function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void
```

unregister nfc state changed event.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-nfcController-function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void--><!--Device-nfcController-function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'nfcStateChange' | 是 | The type to unregister. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NfcState&gt; | 否 | Callback used to listen to the nfc state changed event. |

