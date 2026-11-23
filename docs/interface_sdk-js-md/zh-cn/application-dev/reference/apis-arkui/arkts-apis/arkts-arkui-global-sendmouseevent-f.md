# sendMouseEvent

## 导入模块

```TypeScript
```

## sendMouseEvent

```TypeScript
export declare function sendMouseEvent(event: MouseEvent): boolean
```

发送鼠标事件。此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用此接口。由于耗时长，不建议使用。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare function sendMouseEvent(event: MouseEvent): boolean--><!--Device-unnamed-export declare function sendMouseEvent(event: MouseEvent): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**测试接口：** 此接口仅在自动化测试脚本中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | MouseEvent](../arkts-components/arkts-arkui-common-comp-mouseevent-i.md) | 是 | 鼠标事件，event参数见[MouseEvent介绍。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |
