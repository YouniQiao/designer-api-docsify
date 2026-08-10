# IDeliveryShortMessageCallback

Provides the callback for the SMS message delivery report.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface IDeliveryShortMessageCallback--><!--Device-sms-export interface IDeliveryShortMessageCallback-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## pdu

```TypeScript
pdu: Array<int>
```

Indicates the SMS delivery report.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-IDeliveryShortMessageCallback-pdu: Array<int>--><!--Device-IDeliveryShortMessageCallback-pdu: Array<int>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

