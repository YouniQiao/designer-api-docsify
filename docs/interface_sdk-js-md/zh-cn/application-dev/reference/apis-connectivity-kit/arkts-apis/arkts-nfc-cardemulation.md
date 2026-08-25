# @ohos.nfc.cardEmulation(标准NFC-cardEmulation)

本模块主要提供NFC卡模拟业务，包括判断支持哪种卡模拟类型，HCE卡模拟的业务实现等。HCE(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，应用程序模拟NFC卡片，可以通过NFC服务和NFC读卡器通信。HCE卡模拟和AID列表的声明定义开发HCE卡模拟相关应用时，需要在应用的属性配置文件中，声明与NFC相关的属性值，比如，在module.json5文件中，声明下面属性值：

> **注意：**&gt;
> 1. 声明"actions"字段的内容填写，必须包含"ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"，不能更改。&gt;
> 2. 声明aid（参考ISO/IEC 7816-4规范）时，name必须为payment-aid或者other-aid。填写错误会造成解析失败。&gt;
> 3. 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC_CARD_EMULATION"，不能更改。&gt;
> 4. 轻量级智能穿戴产品不同于其他设备，仅支持[FA模型](../../../application-models/ability-terminology.md#fa模型)，属性配置和接口调用方式与其他设备有所区别，详见示例。

**起始版本：** 6

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [hasHceCapability(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-hashcecapability-f.md) |
| [isDefaultService(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-isdefaultservice-f.md) |
| [isSupported(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-issupported-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getPaymentServices(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-getpaymentservices-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [HceService(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-hceservice-c.md) |

### 枚举

| 名称 |
| --- |
| [CardType(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-cardtype-e.md) |
| [FeatureType(标准NFC-cardEmulation)](arkts-connectivity-cardemulation-featuretype-e.md) |
