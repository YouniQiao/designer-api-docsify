# isSimActive

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## isSimActive

```TypeScript
function isSimActive(slotId: number, callback: AsyncCallback<boolean>): void
```

获取指定卡槽SIM卡是否激活。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isSimActive

```TypeScript
function isSimActive(slotId: number): Promise<boolean>
```

获取指定卡槽SIM卡是否激活。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
