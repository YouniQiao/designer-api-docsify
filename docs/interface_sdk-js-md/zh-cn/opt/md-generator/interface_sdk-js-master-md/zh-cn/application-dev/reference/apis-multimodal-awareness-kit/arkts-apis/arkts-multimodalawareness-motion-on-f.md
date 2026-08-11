# on

## on('operatingHandChanged')

```TypeScript
function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void
```

订阅触控操作手感知事件。调用on()订阅事件后，建议在使用完毕后调用off()取消订阅以释放资源，避免多余的性能功耗开销。相关方法：off('operatingHandChanged')：取消订阅触控操作手感知事件。

如果设备不支持此功能，将返回801错误码。

**起始版本：** 15

**需要权限：** 
- API版本20+：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE
- API版本15 - 19：ohos.permission.ACTIVITY_MOTION

<!--Device-motion-function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void--><!--Device-motion-function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'operatingHandChanged' | 是 |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;OperatingHandStatus&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-订阅失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callback:Callback<motion.OperatingHandStatus> = (data:motion.OperatingHandStatus) => {
    console.info('operatingHandStatus: ' + data);
};

try {
    motion.on('operatingHandChanged', callback);  
    console.info('on succeeded');
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to subscribe operatingHandChanged. Code: ${error.code}, message: ${error.message}`);
}
```


## on('holdingHandChanged')

```TypeScript
function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void
```

订阅握持手状态变化感知事件。调用on()订阅事件后，建议在使用完毕后调用off()取消订阅以释放资源，避免多余的性能功耗开销。相关方法：off('holdingHandChanged')：取消订阅握持手状态变化感知事件。

**起始版本：** 20

**需要权限：** ohos.permission.DETECT_GESTURE

<!--Device-motion-function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void--><!--Device-motion-function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'holdingHandChanged' | 是 |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;HoldingHandStatus&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-订阅失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callback:Callback<motion.HoldingHandStatus> = (data:motion.HoldingHandStatus) => {
  console.info('holdingHandStatus: ' + data);
};

try {
  motion.on('holdingHandChanged', callback);
  console.info('on succeeded');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to subscribe holdingHandChanged. Code: ${error.code}, message: ${error.message}`);
}
```
