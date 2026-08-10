# @ohos.nfc.cardEmulation

Provides methods to operate or manage NFC card emulation.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace cardEmulation--><!--Device-unnamed-declare namespace cardEmulation-End-->

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md#hashcecapability) | Checks whether Host Card Emulation(HCE) capability is supported. |
| [isDefaultService](arkts-connectivity-cardemulation-isdefaultservice-f.md#isdefaultservice) | Checks whether a service is default for given type. |
| [isSupported](arkts-connectivity-cardemulation-issupported-f.md#issupported) | Checks whether a specified type of card emulation is supported.&lt;p&gt;This method is used to check Whether the host or secure element supports card emulation. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getPaymentServices](arkts-connectivity-cardemulation-getpaymentservices-f-sys.md#getpaymentservices) | Gets all payment services. |
<!--DelEnd-->

### 类

| 名称 | 说明 |
| --- | --- |
| [HceService](arkts-connectivity-cardemulation-hceservice-c.md) | A class for NFC host application.&lt;p&gt;The NFC host application use this class, then Nfc service can access the application installation information and connect to services of the application. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [CardType](arkts-connectivity-cardemulation-cardtype-e.md) | Define the card emulation type, payment or other. |
| [FeatureType](arkts-connectivity-cardemulation-featuretype-e.md) | Defines the capability type. |

