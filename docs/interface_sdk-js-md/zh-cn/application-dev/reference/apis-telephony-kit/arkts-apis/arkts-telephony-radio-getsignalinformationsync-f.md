# getSignalInformationSync

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getSignalInformationSync

```TypeScript
function getSignalInformationSync(slotId: int): Array<SignalInformation>
```

获取指定SIM卡槽对应的注册网络信号强度信息列表。

**起始版本：** 23

<!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>--><!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | int | 是 | 卡槽ID。<br/>- 0：卡槽1。<br/>- 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;SignalInformation&gt; | 返回网络信号强度[SignalInformation]{ |

**示例**

```TypeScript
let slotId: number = 0;
let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
console.info(`signal information size is:` + signalInfo.length);
```

