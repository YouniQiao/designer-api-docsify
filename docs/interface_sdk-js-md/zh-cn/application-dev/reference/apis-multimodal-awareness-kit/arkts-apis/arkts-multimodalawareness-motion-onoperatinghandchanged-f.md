# onOperatingHandChanged

## 导入模块

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## onOperatingHandChanged

```TypeScript
function onOperatingHandChanged(callback: Callback<OperatingHandStatus>): void
```

订阅触控操作手变化事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACTIVITY_MOTION 或 ohos.permission.DETECT_GESTURE

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../errorcode-motion.md#31500001-服务异常) |
| [31500002](../errorcode-motion.md#31500002-订阅失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import motion from '@ohos.multimodalAwareness.motion';

callback(data:motion.OperatingHandStatus) {
    console.info('callback success' + data);
};

try {
    motion.onOperatingHandChanged(this.callback);  
    console.info("on succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed on and err code is " + error.code);
}
```
