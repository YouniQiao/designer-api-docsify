# isSimActive

## isSimActive

```TypeScript
function isSimActive(slotId: number, callback: AsyncCallback<boolean>): void
```

Checks whether the SIM card in a specified slot is activated.

**起始版本：** 7

<!--Device-sim-function isSimActive(slotId: int, callback: AsyncCallback<boolean>): void--><!--Device-sim-function isSimActive(slotId: int, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## isSimActive

```TypeScript
function isSimActive(slotId: number): Promise<boolean>
```

Checks whether the SIM card in a specified slot is activated.

**起始版本：** 7

<!--Device-sim-function isSimActive(slotId: int): Promise<boolean>--><!--Device-sim-function isSimActive(slotId: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0).then((data: boolean) => {
    console.info(`isSimActive success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isSimActive failed, promise: err->${JSON.stringify(err)}`);
});
```
