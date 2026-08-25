# getSignalInformationSync

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getSignalInformationSync

```TypeScript
function getSignalInformationSync(slotId: number): Array<SignalInformation>
```

获取指定SIM卡槽对应的注册网络信号强度信息列表。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;SignalInformation & gt; |
