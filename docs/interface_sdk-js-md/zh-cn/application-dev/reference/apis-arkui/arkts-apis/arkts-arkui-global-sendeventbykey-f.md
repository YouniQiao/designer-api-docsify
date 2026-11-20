# sendEventByKey

## 导入模块

```TypeScript
```

## sendEventByKey

```TypeScript
export declare function sendEventByKey(id: string, action: number, params: string): boolean
```

给指定id的组件发送事件。此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用此接口。由于耗时长，不建议使用。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare function sendEventByKey(id: string, action: number, params: string): boolean--><!--Device-unnamed-export declare function sendEventByKey(id: string, action: number, params: string): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**测试接口：** 此接口仅在自动化测试脚本中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 要触发事件的组件的id。 |
| action | number | 是 | 要触发的事件类型，目前支持取值：<br>- 点击事件Click: 10。<br>- 长按事件LongClick: 11。 |
| params | string | 是 | 事件参数。当前支持的事件类型（Click和LongClick）均无需额外参数，请传空字符串 ""。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 找不到指定id的组件时返回false，其余情况返回true。 |
