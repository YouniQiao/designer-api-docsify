# off

## off('operatingHandChanged')

```TypeScript
function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void
```

取消订阅触控操作手感知事件。若未调用on()就调用off()，该方法会抛出异常。相关方法：on('operatingHandChanged')：订阅触控操作手感知事件。

**起始版本：** 15

**需要权限：** 
- API版本20+：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE
- API版本15 - 19：ohos.permission.ACTIVITY_MOTION

<!--Device-motion-function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void--><!--Device-motion-function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'operatingHandChanged' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-motion.md#31500003-取消订阅失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    motion.off('operatingHandChanged');
    console.info('off succeeded');
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to unsubscribe operatingHandChanged. Code: ${error.code}, message: ${error.message}`);
}
```


## off('holdingHandChanged')

```TypeScript
function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void
```

取消订阅握持手状态变化感知事件。若未调用on()就调用off()，该方法会抛出异常。相关方法：on('holdingHandChanged')：订阅握持手状态变化感知事件。

**起始版本：** 20

**需要权限：** ohos.permission.DETECT_GESTURE

<!--Device-motion-function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void--><!--Device-motion-function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'holdingHandChanged' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-motion.md#31500003-取消订阅失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  motion.off('holdingHandChanged'); // 移除所有同类订阅
  console.info('off succeeded');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to unsubscribe holdingHandChanged. Code: ${error.code}, message: ${error.message}`);
}
```
