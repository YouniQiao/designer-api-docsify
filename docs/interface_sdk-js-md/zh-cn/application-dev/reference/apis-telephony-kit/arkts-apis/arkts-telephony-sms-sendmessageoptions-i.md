# SendMessageOptions

Provides the options (including callbacks) for sending an SMS message.

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-sms-export interface SendMessageOptions--><!--Device-sms-export interface SendMessageOptions-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## content

```TypeScript
content: string | Array<int>
```

If the content is a string, this is a short message. If the content is a byte array, this is a data message.

**类型：** ArkTS-Dyn: string \| Array&lt;number&gt;  <br>ArkTS-Sta：string \| Array&lt;int&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-content: string | Array<int>--><!--Device-SendMessageOptions-content: string | Array<int>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## deliveryCallback

```TypeScript
deliveryCallback?: AsyncCallback<IDeliveryShortMessageCallback>
```

Indicates the callback invoked after the SMS message is delivered.

**类型：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;IDeliveryShortMessageCallback&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-deliveryCallback?: AsyncCallback<IDeliveryShortMessageCallback>--><!--Device-SendMessageOptions-deliveryCallback?: AsyncCallback<IDeliveryShortMessageCallback>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## destinationHost

```TypeScript
destinationHost: string
```

Indicates the address to which the SMS message is sent.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-destinationHost: string--><!--Device-SendMessageOptions-destinationHost: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## destinationPort

```TypeScript
destinationPort?: int
```

If send data message, destinationPort is mandatory. Otherwise is optional.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-destinationPort?: int--><!--Device-SendMessageOptions-destinationPort?: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## sendCallback

```TypeScript
sendCallback?: AsyncCallback<ISendShortMessageCallback>
```

Indicates the callback invoked after the SMS message is sent.

**类型：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ISendShortMessageCallback&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-sendCallback?: AsyncCallback<ISendShortMessageCallback>--><!--Device-SendMessageOptions-sendCallback?: AsyncCallback<ISendShortMessageCallback>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## serviceCenter

```TypeScript
serviceCenter?: string
```

Indicates the SMSC address. If the value is {@code null}, the default SMSC address of the SIM card.

**类型：** string

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-serviceCenter?: string--><!--Device-SendMessageOptions-serviceCenter?: string-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

## slotId

```TypeScript
slotId: int
```

Indicates the ID of the SIM card slot used for sending the SMS message.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

<!--Device-SendMessageOptions-slotId: int--><!--Device-SendMessageOptions-slotId: int-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

