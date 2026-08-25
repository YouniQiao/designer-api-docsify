# getDefaultCellularDataSlotId

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getDefaultCellularDataSlotId

```TypeScript
function getDefaultCellularDataSlotId(callback: AsyncCallback<number>): void
```

获取默认移动数据的SIM卡，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getDefaultCellularDataSlotId

```TypeScript
function getDefaultCellularDataSlotId(): Promise<number>
```

获取默认移动数据的SIM卡，使用Promise方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.CellularData

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
