# hasSmsCapability

## 导入模块

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## hasSmsCapability

```TypeScript
function hasSmsCapability(): boolean
```

检查当前设备是否具备短信发送和接收能力，该方法是同步方法。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { sms } from '@kit.TelephonyKit';

let result = sms.hasSmsCapability(); 
console.info(`hasSmsCapability: ${JSON.stringify(result)}`);
```
